from django.contrib import admin
from notifications.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'plant', 'action_type', 'created_at')
    list_filter = ('action_type',)

    readonly_fields = ('user', 'plant', 'action_type', 'created_at')
