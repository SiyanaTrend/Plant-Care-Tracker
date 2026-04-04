from django.urls import path

from gardeners import views

urlpatterns = [
    path('details/', views.GardenerDetailsView.as_view(), name='gardener-details'),
    path('edit/', views.GardenerEditView.as_view(), name='edit-gardener'),
    path('delete/', views.GardenerDeleteView.as_view(), name='delete-gardener'),
]