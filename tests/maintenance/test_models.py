from django.test import TestCase
from django.contrib.auth import get_user_model
from django.utils import timezone
from plants.models import Plant
from maintenance.models import MaintenanceRecord
from common.choices import ActionPlantChoices

User = get_user_model()


class MaintenanceModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='care@test.com', password='password123')
        self.plant = Plant.objects.create(
            plant_name='Ferny',
            city='Sofia',
            user=self.user,
            watering_frequency=3
        )
        self.today = timezone.now().date()

    def test_maintenance_record_str(self):
        record = MaintenanceRecord.objects.create(
            plant=self.plant,
            action=ActionPlantChoices.WATERING,
            date=self.today
        )
        expected_str = f'Ferny - {ActionPlantChoices.WATERING} ({self.today})'
        self.assertEqual(str(record), expected_str)
