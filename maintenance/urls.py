from django.urls import path, include

from maintenance import views

urlpatterns = [
    path('plant/<slug:plant_slug>/', include([
        path('', views.MaintenanceDetailsView.as_view(), name='maintenance-details'),
        path('create/', views.MaintenanceCreateView.as_view(), name='create-maintenance'),
    ])),
    path('<int:maintenance_pk>/', include([
        path('edit/', views.MaintenanceEditView.as_view(), name='edit-maintenance'),
        path('delete/', views.MaintenanceDeleteView.as_view(), name='delete-maintenance'),
    ])),
]
