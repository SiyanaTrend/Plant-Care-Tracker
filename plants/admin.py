from django.contrib import admin

from plants.models import Plant, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)
    search_fields = ('tag_name',)


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('plant_name', 'species', 'city', 'watering_frequency', 'gardener', 'created_at')
    list_filter = ('city', 'tags', 'gardener', 'watering_frequency')
    ssearch_fields = ('plant_name', 'species', 'city')
    filter_horizontal = ('tags',)
    fieldsets = (
        ('Basic Information', {
            'fields': ('plant_name', 'species', 'description', 'image_url')
        }),
        ('Location Details', {
            'fields': ('city', 'address', 'gardener')
        }),
        ('Care Schedule (Frequencies)', {
            'description': 'Set the maintenance intervals for this plant.',
            'fields': ('watering_frequency', 'fertilizing_frequency', 'pruning_frequency')
        }),
        ('Tags & Metadata', {
            'fields': ('tags',)
        }),
    )
    list_editable = ('watering_frequency',)
