from django.urls import path, include

from plants import views

urlpatterns = [
    path('', views.PlantsListView.as_view(), name='catalogue'),
]