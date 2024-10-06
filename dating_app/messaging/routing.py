from django.urls import path
from .consumers import MessagingConsumer
from . import consumers

websocket_urlpatterns = [
    path('ws/messaging/', MessagingConsumer.as_asgi()),
    path('ws/messaging/chat/<str:room_name>/', consumers.ChatConsumer.as_asgi()),
]

