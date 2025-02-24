from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('room', views.RoomView.as_view()),
    path('create-room', views.CreateRoomView.as_view())
]
