from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from notifications.models import Notification
from notifications.services import update_notifications


class NotificationListView(LoginRequiredMixin, ListView):
    model = Notification
    template_name = 'notifications/notifications-list.html'
    context_object_name = 'notifications'

    def get_queryset(self):
        update_notifications(self.request.user)
        return Notification.objects.filter(user=self.request.user)
