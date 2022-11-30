from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

from ads.models import Selection
from ads.permissions import SelectionOwnerPermission
from ads.serializers.selections_serilaziers import SelectionsListSerializer, SelectionsDetailSerializer, \
    SelectionsCreateSerializer, SelectionsUpdateDeleteSerializer


class SelectionsListView(ListAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionsListSerializer
    permission_classes = [AllowAny]


class SelectionsRetrieveView(RetrieveAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionsDetailSerializer
    permission_classes = [IsAuthenticated, SelectionOwnerPermission]


class SelectionsCreateView(CreateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionsCreateSerializer
    permission_classes = [IsAuthenticated]


class SelectionsUpdateView(UpdateAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionsUpdateDeleteSerializer
    permission_classes = [IsAuthenticated, SelectionOwnerPermission]


class SelectionsDeleteView(DestroyAPIView):
    queryset = Selection.objects.all()
    serializer_class = SelectionsUpdateDeleteSerializer
    permission_classes = [IsAuthenticated, SelectionOwnerPermission]
