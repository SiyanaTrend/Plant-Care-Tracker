from rest_framework import serializers
from .models import MaintenanceRecord


class MaintenanceRecordSerializer(serializers.ModelSerializer):
    plant_name = serializers.ReadOnlyField(source='plant.plant_name')

    class Meta:
        model = MaintenanceRecord
        fields = [
            'id', 'action', 'date', 'notes', 'plant', 'plant_name',
        ]

        read_only_fields = ['plant_name']

    def validate(self, data):
        plant = data.get('plant')
        date = data.get('date')

        if plant and date and date < plant.created_at.date():
            raise serializers.ValidationError({
                'date': f'Date cannot be before plant creation date ({plant.created_at.date()}).'
            })
        return data
