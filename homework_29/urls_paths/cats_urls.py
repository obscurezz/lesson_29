from django.urls import path

from ads.views.cats_views import CategoriesListView, CategoriesRetrieveView

urlpatterns = [
    path('categories/', CategoriesListView.as_view()),
    path('categories/<int:pk>/', CategoriesRetrieveView.as_view()),
]
