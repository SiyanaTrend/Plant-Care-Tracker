from django.urls import path

from notifications import views

urlpatterns = [
    path('', views.NotificationListView.as_view(), name='notifications-list'),
]