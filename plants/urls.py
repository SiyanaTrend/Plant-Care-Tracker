from django.urls import path, include

from plants import views

urlpatterns = [
    path('', views.PlantsListView.as_view(), name='catalogue'),
    path('create/', views.PlantCreateView.as_view(), name='create-plant'),
    path('suggest-tag/', views.SuggestTagView.as_view(), name='suggest-tag'),
    path('<slug:plant_slug>/', include([
        path('favourite/', views.PlantFavouriteView.as_view(), name='favourite-plant'),
        path('details/', views.PlantDetailsView.as_view(), name='plant-details'),
        path('edit/', views.PlantEditView.as_view(), name='edit-plant'),
        path('delete/', views.PlantDeleteView.as_view(), name='delete-plant'),
    ])),
]
