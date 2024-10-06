from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import UserProfile, Notification
from django.contrib.auth.models import User

# Registration and Login Views
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

# User Profile Management
@login_required
def swipe_profiles(request):
    current_user_profile = request.user.userprofile
    all_profiles = UserProfile.objects.exclude(user=request.user)

    # Get swiped profiles
    swiped_profiles = current_user_profile.liked_users.all() | current_user_profile.disliked_users.all()
    available_profiles = all_profiles.difference(swiped_profiles)

    if not available_profiles.exists():
        return render(request, 'users/no_more_profiles.html')

    # Show one profile at a time
    profile_to_show = available_profiles.first()
    return render(request, 'users/swipe.html', {'profile': profile_to_show})

@login_required
def like_profile(request, user_id):
    liked_profile = get_object_or_404(UserProfile, user_id=user_id)
    current_user_profile = request.user.userprofile
    current_user_profile.liked_users.add(liked_profile)

    # Check for a match
    if request.user in liked_profile.liked_users.all():
        current_user_profile.matches.add(liked_profile)
        liked_profile.matches.add(current_user_profile)

    return redirect('swipe_profiles')

@login_required
def dislike_profile(request, user_id):
    disliked_profile = get_object_or_404(UserProfile, user_id=user_id)
    current_user_profile = request.user.userprofile
    current_user_profile.disliked_users.add(disliked_profile)
    return redirect('swipe_profiles')

# User List and Profile Views
def user_list(request):
    users = UserProfile.objects.exclude(user=request.user)  # Exclude current user
    return render(request, 'users/user_list.html', {'users': users})

def profile_view(request, username):
    profile = get_object_or_404(UserProfile, user__username=username)
    return render(request, 'users/profile.html', {'profile': profile})

# Like and Dislike User Functionality
def like_user(request, user_id):
    target_user = get_object_or_404(UserProfile, id=user_id)
    request.user.userprofile.liked_users.add(target_user)
    Notification.objects.create(user=target_user.user, message=f"{request.user.username} liked you!")
    return redirect('user_list')

def dislike_user(request, user_id):
    target_user = get_object_or_404(UserProfile, id=user_id)
    request.user.userprofile.disliked_users.add(target_user)
    return redirect('user_list')

# Notification View
def notification_view(request):
    notifications = Notification.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'users/notifications.html', {'notifications': notifications})
