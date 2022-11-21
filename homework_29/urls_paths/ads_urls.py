from django.urls import path

from ads.views.ads_views import AdsListView, AdsRetrieveView

urlpatterns = [
    path('ads/', AdsListView.as_view()),
    path('ads/<int:pk>/', AdsRetrieveView.as_view()),
]
