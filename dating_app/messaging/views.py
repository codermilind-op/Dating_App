from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatMessage
from django.db.models import Q

@login_required
def chat_room(request, room_name):
    user = request.user
    messages = ChatMessage.objects.filter(
        (Q(sender=user) | Q(receiver=user)) & (Q(sender__id=room_name) | Q(receiver__id=room_name))
    ).order_by('timestamp')

    return render(request, 'messaging/chat_room.html', {
        'room_name': room_name,
        'messages': messages
    })
