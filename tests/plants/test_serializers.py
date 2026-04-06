from django.test import TestCase
from django.contrib.auth import get_user_model
from plants.models import Plant
from plants.serializers import PlantSerializer

User = get_user_model()


class PlantSerializerTests(TestCase):
    def test_plant_serializer_fields(self):
        user = User.objects.create_user(email='api@test.com', password='123')
        plant = Plant.objects.create(plant_name='API Plant', city='Sofia', user=user)
        serializer = PlantSerializer(instance=plant)

        self.assertIn('has_pending_alerts', serializer.data)
        self.assertIn('slug', serializer.data)