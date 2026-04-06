from django.test import TestCase
from django.contrib.auth import get_user_model
from datetime import date, timedelta
from plants.models import Plant
from notifications.models import Notification
from maintenance.models import MaintenanceRecord
from notifications.services import update_notifications
from common.choices import ActionPlantChoices

User = get_user_model()


class NotificationServiceTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='service@test.com', password='password123')
        self.plant = Plant.objects.create(
            plant_name='Service Plant',
            city='Sofia',
            user=self.user,
            watering_frequency=30
        )

    def test_update_notifications_creates_alert(self):
        five_days_ago = date.today() - timedelta(days=5)
        MaintenanceRecord.objects.create(
            plant=self.plant,
            action=ActionPlantChoices.WATERING,
            date=five_days_ago
        )
        update_notifications(self.user)
        self.assertTrue(Notification.objects.filter(
            plant=self.plant,
            action_type=ActionPlantChoices.WATERING
        ).exists())

    def test_update_notifications_no_duplicate(self):
        update_notifications(self.user)
        count_before = Notification.objects.count()
        update_notifications(self.user)
        count_after = Notification.objects.count()
        self.assertEqual(count_before, count_after)

    def test_notification_not_created_if_recently_maintained(self):
        MaintenanceRecord.objects.create(
            plant=self.plant,
            action=ActionPlantChoices.WATERING,
            date=date.today()
        )
        update_notifications(self.user)
        notif_exists = Notification.objects.filter(
            plant=self.plant,
            action_type=ActionPlantChoices.WATERING
        ).exists()
        self.assertFalse(notif_exists)
