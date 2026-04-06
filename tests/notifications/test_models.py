from django.test import TestCase
from django.contrib.auth import get_user_model
from plants.models import Plant
from notifications.models import Notification
from common.choices import ActionPlantChoices

User = get_user_model()


class NotificationModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='notif@test.com', password='password123')
        self.plant = Plant.objects.create(
            plant_name='Thirsty Fern',
            city='Sofia',
            user=self.user,
            watering_frequency=30
        )

    def test_notification_str(self):
        notif = Notification.objects.create(
            user=self.user,
            plant=self.plant,
            action_type=ActionPlantChoices.WATERING
        )
        self.assertEqual(str(notif), f'{ActionPlantChoices.WATERING} alert for Thirsty Fern')