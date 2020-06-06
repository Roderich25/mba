from django.urls import path
from .views import IndexView, RoomView


app_name = 'chat_app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<str:room_name>/', RoomView.as_view(), name='room'),
]
