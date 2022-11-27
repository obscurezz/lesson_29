"""homework_29 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from basics.views.cats_views import CategoriesViewSet
from basics.views.locs_views import LocationsViewSet


router = SimpleRouter()
router.register('locations', LocationsViewSet)
router.register('categories', CategoriesViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('ads/', include('homework_29.urls_paths.ads_urls')),
    path('user/', include('homework_29.urls_paths.users_urls')),
    path('selection/', include('homework_29.urls_paths.selections_urls'))
] + router.urls
