from django.urls import path

from gardeners import views

urlpatterns = [
    path('', views.GardenerCreateView.as_view(), name='create-gardener'),
    path('edit/', views.GardenerEditView.as_view(), name='edit-gardener'),
]