from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import RoomSerializer
from . import models

# Create your views here.


def main(request):
    return HttpResponse("Backend")


class RoomView(generics.ListAPIView):
    queryset = models.Room.objects.all()
    serializer_class = RoomSerializer
