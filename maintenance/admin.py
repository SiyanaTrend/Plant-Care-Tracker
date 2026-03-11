from django.contrib import admin

from maintenance.models import MaintenanceRecord


@admin.register(MaintenanceRecord)
class MaintenanceRecordAdmin(admin.ModelAdmin):
    list_display = ('plant', 'action', 'date')
    list_filter = ('action', 'date', 'plant')
    search_fields = ('plant__plant_name', 'notes')
