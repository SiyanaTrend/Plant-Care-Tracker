from django.test import TestCase
from django.contrib.auth import get_user_model
from plants.models import Plant
from plants.templatetags.garden_extras import garden_health_details

User = get_user_model()


class GardenTemplateTagsTests(TestCase):
    def test_garden_health_score_calculation(self):
        user = User.objects.create_user(email='tags@test.com', password='123')
        Plant.objects.create(plant_name='Healthy Plant', city='Sofia', user=user, watering_frequency=4)
        plants_queryset = Plant.objects.filter(user=user)

        result = garden_health_details(plants_queryset)
        self.assertEqual(result['score'], 100)
