from django.shortcuts import render
from rest_framework import viewsets
from Fashion_API.serializers import UserSerializers
from django.contrib.auth.models import User


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializers