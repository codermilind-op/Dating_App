from django.urls import path
from . import views
from .views import user_list, notification_view,profile_view, like_user, dislike_user

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('swipe/', views.swipe_profiles, name='swipe_profiles'),
    path('like/<int:user_id>/', views.like_profile, name='like_profile'),
    path('dislike/<int:user_id>/', views.dislike_profile, name='dislike_profile'),
    path('list/', user_list, name='user_list'),
    path('profile/<str:username>/', profile_view, name='profile_view'),
    path('like/<int:user_id>/', like_user, name='like_user'),
    path('dislike/<int:user_id>/', dislike_user, name='dislike_user'),
    path('notifications/', notification_view, name='notification_view'),

]



