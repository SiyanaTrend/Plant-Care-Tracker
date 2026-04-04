from django.contrib import admin

from plants.models import Plant, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('tag_name',)
    search_fields = ('tag_name',)


@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('plant_name', 'species', 'city', 'watering_frequency', 'user', 'created_at')
    list_filter = ('city', 'tags', 'user', 'watering_frequency')
    search_fields = ('plant_name', 'species', 'city')
    filter_horizontal = ('tags', 'favourite_by')

    readonly_fields = ('slug', 'created_at')

    fieldsets = (
        ('Basic Information', {
            'fields': ('plant_name', 'slug', 'species', 'description', 'image')
        }),
        ('Location & Ownership', {
            'fields': ('city', 'address', 'user')
        }),
        ('Care Schedule', {
            'fields': ('watering_frequency', 'fertilizing_frequency', 'pruning_frequency')
        }),
        ('Tags & Community', {
            'fields': ('tags', 'favourite_by')
        }),
    )
    list_editable = ('watering_frequency',)
