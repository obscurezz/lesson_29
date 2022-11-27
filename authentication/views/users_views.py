from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from authentication.models import User
from authentication.serializers.users_serializer import UsersListSerializer, UsersRetrieveSerializer, \
    UsersCreateSerializer, UsersDeleteUpdateSerializer


class UsersListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersListSerializer


class UsersRetrieveView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UsersRetrieveSerializer


class UsersCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersCreateSerializer


class UsersUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersDeleteUpdateSerializer


class UsersDestroyView(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UsersDeleteUpdateSerializer
