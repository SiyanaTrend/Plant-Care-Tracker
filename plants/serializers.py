from rest_framework import serializers
from .models import Plant, Tag


class PlantSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    tags = serializers.SlugRelatedField(
        many=True,
        slug_field='tag_name',
        queryset=Tag.objects.filter(is_approved=True),
        required=False
    )
    has_pending_alerts = serializers.SerializerMethodField()

    class Meta:
        model = Plant
        fields = [
            'id', 'plant_name', 'species', 'description',
            'city', 'address', 'user', 'tags', 'has_pending_alerts', 'slug',
        ]
        read_only_fields = ['slug', 'has_pending_alerts']

    def get_has_pending_alerts(self, obj):
        return obj.notifications.exists()
