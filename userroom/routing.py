from django.urls import re_path

from userroom.consumers.room_comsumer import RoomConsumer


websocket_urlpatterns = [
    re_path(r'^ws/rooms/(?P<room_id>[a-zA-Z0-9\-]+)/$', RoomConsumer.as_asgi()),  # Используйте room_id
]
