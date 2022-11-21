from django.urls import path

from ads.views.users_views import UsersListView, UsersRetrieveView, UsersCreateView, UsersUpdateView, UsersDestroyView

urlpatterns = [
    path('users/', UsersListView.as_view()),
    path('users/<int:pk>/', UsersRetrieveView.as_view()),
    path('users/<int:pk>/create/', UsersCreateView.as_view()),
    path('users/<int:pk>/update/', UsersUpdateView.as_view()),
    path('users/<int:pk>/delete/', UsersDestroyView.as_view()),
]
