from django.urls import path, include

from plants import views

urlpatterns = [
    path('', views.PlantsListView.as_view(), name='catalogue'),
    path('create/', views.PlantCreateView.as_view(), name='create-plant'),
    path('<int:plant_pk>/', include([
        path('details/', views.PlantDetailsView.as_view(), name='plant-details'),
        path('edit/', views.PlantEditView.as_view(), name='edit-plant'),
        path('delete/', views.PlantDeleteView.as_view(), name='delete-plant'),
    ])),
]