from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from plants.models import Plant, Tag
from plants.validators import PlantNameValidator

User = get_user_model()


class PlantModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', password='password123')

    def test_plant_creation_and_slug(self):
        plant = Plant.objects.create(
            plant_name='My Monstera',
            city='Sofia',
            user=self.user,
            watering_frequency=4
        )
        self.assertTrue(plant.slug.startswith('my-monstera'))
        self.assertEqual(str(plant), f'My Monstera - Sofia (None)')

    def test_plant_name_validator_invalid_chars(self):
        validator = PlantNameValidator()
        with self.assertRaises(ValidationError):
            validator('Rose@Flower')

    def test_tag_normalization(self):
        tag = Tag.objects.create(tag_name='  unique-tropical  ')
        self.assertEqual(tag.tag_name, 'Unique-Tropical')
