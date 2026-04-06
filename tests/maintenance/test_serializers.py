from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from plants.models import Plant
from maintenance.models import MaintenanceRecord
from maintenance.serializers import MaintenanceRecordSerializer
from common.choices import ActionPlantChoices

User = get_user_model()


class MaintenanceSerializerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='api@test.com', password='password123')
        self.client.login(email='api@test.com', password='password123')
        self.plant = Plant.objects.create(
            plant_name='Ferny',
            city='Sofia',
            user=self.user,
            watering_frequency=3
        )
        self.today = timezone.now().date()

    def test_api_maintenance_validation(self):
        yesterday = self.today - timedelta(days=1)
        data = {
            'plant': self.plant.id,
            'action': ActionPlantChoices.WATERING,
            'date': yesterday,
            'notes': 'API test',
        }
        serializer = MaintenanceRecordSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('date', serializer.errors)

    def test_api_list_queryset_isolation(self):
        other_user = User.objects.create_user(email='other@test.com', password='password123')
        other_plant = Plant.objects.create(plant_name='Not Mine', city='Varna', user=other_user)
        MaintenanceRecord.objects.create(plant=other_plant, action=ActionPlantChoices.WATERING, date=self.today)
        MaintenanceRecord.objects.create(plant=self.plant, action=ActionPlantChoices.WATERING, date=self.today)

        url = reverse('api-maintenance-list')
        response = self.client.get(url)
        self.assertEqual(len(response.data), 1)