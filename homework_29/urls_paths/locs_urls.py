from django.urls import path

from ads.views.locs_views import LocationsListView, LocationsRetrieveView

urlpatterns = [
    path('locations/', LocationsListView.as_view()),
    path('locations/<int:pk>/', LocationsRetrieveView.as_view()),
]
