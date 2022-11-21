from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView

from ads.models import Ad
from ads.serializers.ads_serializers import AdsListSerializer, AdsRetrieveSerializer


class AdsListView(ListAPIView):
    queryset = Ad.objects.all().order_by('price')
    serializer_class = AdsListSerializer

    def get(self, request, *args, **kwargs):
        category_search = request.GET.get('category', None)
        if category_search:
            self.queryset = self.queryset.filter(category__name__icontains=category_search)

        name_search = request.GET.get('name', None)
        if name_search:
            self.queryset = self.queryset.filter(name__icontains=name_search)

        location_search = request.GET.get('location', None)
        if location_search:
            self.queryset = self.queryset.filter(author__location__name__icontains=location_search)

        price_range_search_from = request.GET.get('price_from', None)
        price_range_search_to = request.GET.get('price_to', None)

        if price_range_search_from and not price_range_search_to:
            self.queryset = self.queryset.filter(price__gte=price_range_search_from)

        if not price_range_search_from and price_range_search_to:
            self.queryset = self.queryset.filter(price__lte=price_range_search_to)

        if price_range_search_from and price_range_search_to:
            self.queryset = self.queryset.filter(price__range=[price_range_search_from, price_range_search_to])

        return super().get(request, *args, **kwargs)


class AdsRetrieveView(RetrieveAPIView):
    queryset = Ad.objects.all()
    serializer_class = AdsRetrieveSerializer
