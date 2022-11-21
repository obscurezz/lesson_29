from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from ads.models import User
from ads.serializers.users_serializer import UsersListSerializer, UsersRetrieveSerializer, UsersCUDSerializer


class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer


class UsersRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsersRetrieveSerializer


class UsersCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersCUDSerializer


class UsersUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersCUDSerializer


class UsersDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersCUDSerializer
