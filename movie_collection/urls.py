"""
URL configuration for movie_collection project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CollectionViewSet, fetch_movies, RegisterView

router = DefaultRouter()
router.register(r'collection', CollectionViewSet)

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('movies/', fetch_movies, name='fetch_movies'),
    path('', include(router.urls)),
]
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('collections.urls')),
   # path('request-count/', request_count, name='request_count'),
]
from django.urls import path
from .views import fetch_movies  # Import your fetch_movies function

urlpatterns = [
    path('movies/', fetch_movies, name='fetch_movies'),  # Add this line
    # Other URL patterns...
]
