from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date
from plants.models import Plant
from maintenance.models import MaintenanceRecord
from notifications.models import Notification
from gardeners.models import Gardener

User = get_user_model()


class CommonViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='stats@test.com', password='password123')
        self.client.login(email='stats@test.com', password='password123')

        Gardener.objects.update_or_create(user=self.user, defaults={'nickname': 'StatsMaster'})
        self.plant = Plant.objects.create(plant_name='Star Plant', city='Sofia', user=self.user)

        MaintenanceRecord.objects.create(
            plant=self.plant,
            action='Watering',
            date=date.today()
        )

    def test_notification_count_context_processor(self):
        Notification.objects.create(user=self.user, plant=self.plant, action_type='Watering')
        response = self.client.get(reverse('home'))
        self.assertEqual(response.context['unread_count'], 1)

    def test_notification_count_anonymous_user(self):
        self.client.logout()
        response = self.client.get(reverse('home'))
        self.assertEqual(response.context['unread_count'], 0)

    def test_statistics_view_calculations(self):
        url = reverse('statistics')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['total_plants'], 1)
        self.assertEqual(response.context['total_records'], 1)

    def test_home_page_single_profile_mixin(self):
        url = reverse('home')
        response = self.client.get(url)
        gardener = Gardener.objects.get(user=self.user)
        self.assertEqual(gardener.nickname, 'StatsMaster')
        self.assertEqual(response.status_code, 200)
