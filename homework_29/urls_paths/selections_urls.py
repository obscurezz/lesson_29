from django.urls import path

from ads.views.selections_views import SelectionsListView, SelectionsRetrieveView, SelectionsCreateView, \
    SelectionsUpdateView, SelectionsDeleteView

urlpatterns = [
    path('', SelectionsListView.as_view()),
    path('<int:pk>/', SelectionsRetrieveView.as_view()),
    path('create/', SelectionsCreateView.as_view()),
    path('<int:pk>/update/', SelectionsUpdateView.as_view()),
    path('<int:pk>/delete/', SelectionsDeleteView.as_view()),
]
