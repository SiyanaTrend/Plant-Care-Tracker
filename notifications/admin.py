from django.contrib import admin
from notifications.models import Notification


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'plant', 'action_type', 'is_read', 'created_at')
    list_filter = ('is_read', 'action_type')

    readonly_fields = ('user', 'plant', 'action_type', 'created_at')
