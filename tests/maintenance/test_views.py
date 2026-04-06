from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
from plants.models import Plant
from maintenance.models import MaintenanceRecord
from common.choices import ActionPlantChoices

User = get_user_model()


class MaintenanceViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='care@test.com', password='password123')
        self.client.login(email='care@test.com', password='password123')
        self.plant = Plant.objects.create(
            plant_name='Ferny',
            city='Sofia',
            user=self.user,
            watering_frequency=3
        )
        self.today = timezone.now().date()

    def test_maintenance_date_before_plant_creation(self):
        yesterday = self.today - timedelta(days=1)
        url = reverse('create-maintenance', kwargs={'plant_slug': self.plant.slug})
        data = {
            'action': ActionPlantChoices.FERTILIZING,
            'date': yesterday,
            'notes': 'Should fail'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertIn('date', form.errors)
        expected_error = f"Date cannot be before plant creation date ({self.today})."
        self.assertEqual(form.errors['date'][0], expected_error)

    def test_create_maintenance_success(self):
        url = reverse('create-maintenance', kwargs={'plant_slug': self.plant.slug})
        data = {
            'action': ActionPlantChoices.PRUNING,
            'date': self.today,
            'notes': 'Trimmed some leaves'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(MaintenanceRecord.objects.filter(action=ActionPlantChoices.PRUNING).exists())

    def test_maintenance_details_context(self):
        url = reverse('maintenance-details', kwargs={'plant_slug': self.plant.slug})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['plant'], self.plant)