from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from maintenance.forms import MaintenanceCreateForm
from plants.models import Plant
from django.contrib.auth import get_user_model
from common.choices import ActionPlantChoices

User = get_user_model()


class MaintenanceFormsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', password='password123')
        self.plant = Plant.objects.create(
            plant_name='Test Plant',
            city='Sofia',
            user=self.user
        )
        self.today = timezone.now().date()

    def test_maintenance_create_form_valid_data(self):
        form = MaintenanceCreateForm(data={
            'action': ActionPlantChoices.WATERING,
            'date': self.today,
            'notes': 'Everything is fine'
        })
        form.instance.plant = self.plant
        self.assertTrue(form.is_valid())

    def test_maintenance_form_clean_date_before_plant_creation(self):
        yesterday = self.today - timedelta(days=1)
        form = MaintenanceCreateForm(data={
            'action': ActionPlantChoices.WATERING,
            'date': yesterday,
            'notes': 'Should fail'
        })
        form.instance.plant = self.plant

        self.assertFalse(form.is_valid())
        self.assertIn('date', form.errors)
        expected_error = f"Date cannot be before plant creation date ({self.today})."
        self.assertEqual(form.errors['date'][0], expected_error)

    def test_maintenance_form_missing_required_fields(self):
        from maintenance.models import MaintenanceRecord
        instance = MaintenanceRecord(plant=self.plant)

        form = MaintenanceCreateForm(data={}, instance=instance)

        self.assertFalse(form.is_valid())
        self.assertIn('action', form.errors)
        self.assertIn('date', form.errors)
