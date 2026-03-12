from django.urls import path

from gardeners import views

urlpatterns = [
    path('', views.GardenerCreateView.as_view(), name='create-gardener'),
]
