from django.contrib import admin

from gardeners.models import Gardener


@admin.register(Gardener)
class GardenerAdmin(admin.ModelAdmin):
    list_display = ('nickname', 'first_name', 'last_name', 'is_pro')
    list_editable = ('is_pro',)
    search_fields = ('nickname', 'first_name', 'last_name')
    list_filter = ('is_pro',)
