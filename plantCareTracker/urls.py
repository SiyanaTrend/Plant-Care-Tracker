"""
URL configuration for plantCareTracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path, include
from plants.views import PlantListCreateAPIView, PlantDetailAPIView
from maintenance.views import MaintenanceListCreateAPIView, MaintenanceDetailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('common.urls')),
    path('accounts/', include('accounts.urls')),
    path('profile/', include('gardeners.urls')),
    path('plants/', include('plants.urls')),
    path('maintenance/', include('maintenance.urls')),
    path('notifications/', include('notifications.urls')),
    path('api/plants/', PlantListCreateAPIView.as_view(), name='api-plant-list'),
    path('api/plants/<slug:slug>/', PlantDetailAPIView.as_view(), name='api-plant-detail'),
    path('api/maintenance/', MaintenanceListCreateAPIView.as_view(), name='api-maintenance-list'),
    path('api/maintenance/<int:pk>/', MaintenanceDetailAPIView.as_view(), name='api-maintenance-detail'),
]
