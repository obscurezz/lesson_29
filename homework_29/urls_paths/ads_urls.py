from django.urls import path

from ads.views.ads_views import AdsListView, AdsRetrieveView, AdsCreateView, AdsUpdateView, AdsDeleteView

urlpatterns = [
    path('', AdsListView.as_view()),
    path('create/', AdsCreateView.as_view()),
    path('<int:pk>/', AdsRetrieveView.as_view()),
    path('<int:pk>/delete/', AdsDeleteView.as_view()),
    path('<int:pk>/update/', AdsUpdateView.as_view()),
]
