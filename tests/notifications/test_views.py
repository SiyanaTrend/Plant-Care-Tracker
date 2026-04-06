from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from datetime import date, timedelta
from plants.models import Plant
from notifications.models import Notification
from maintenance.models import MaintenanceRecord
from common.choices import ActionPlantChoices

User = get_user_model()


class NotificationViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='view@test.com', password='password123')
        self.client.login(email='view@test.com', password='password123')
        self.plant = Plant.objects.create(
            plant_name='View Plant',
            city='Sofia',
            user=self.user,
            watering_frequency=30
        )

    def test_notification_list_view_status_code(self):
        url = reverse('notifications-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'notifications/notifications-list.html')

    def test_view_triggers_update_notifications(self):
        MaintenanceRecord.objects.create(
            plant=self.plant,
            action=ActionPlantChoices.WATERING,
            date=date.today() - timedelta(days=5)
        )
        url = reverse('notifications-list')
        self.client.get(url)
        self.assertTrue(Notification.objects.count() > 0)
