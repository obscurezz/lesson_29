from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView

from authentication.views.users_views import UsersListView, UsersRetrieveView, UsersCreateView, UsersUpdateView, \
    UsersDestroyView

urlpatterns = [
    path('', UsersListView.as_view()),
    path('<int:pk>/', UsersRetrieveView.as_view()),
    path('create/', UsersCreateView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('logout/', TokenBlacklistView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('<int:pk>/update/', UsersUpdateView.as_view()),
    path('<int:pk>/delete/', UsersDestroyView.as_view()),
]
