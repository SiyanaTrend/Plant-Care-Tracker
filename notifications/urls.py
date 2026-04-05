from django.urls import path

from notifications import views

urlpatterns = [
    path('', views.NotificationListView.as_view(), name='notifications-list'),
    path('read/<int:pk>/', views.mark_as_read, name='mark-notification-read'),
]