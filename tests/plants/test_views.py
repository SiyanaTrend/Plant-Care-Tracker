from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from plants.models import Plant, Tag

User = get_user_model()


class PlantViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', password='password123')
        self.client.login(email='test@test.com', password='password123')

    def test_catalogue_view_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse('catalogue'))
        self.assertEqual(response.status_code, 302)

    def test_create_plant_post(self):
        url = reverse('create-plant')
        data = {
            'plant_name': 'Cactus Jack',
            'city': 'Plovdiv',
            'watering_frequency': 1,
            'fertilizing_frequency': 1,
            'pruning_frequency': 0,
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Plant.objects.filter(plant_name='Cactus Jack').exists())

    def test_edit_plant_with_image(self):
        plant = Plant.objects.create(
            plant_name='Initial Name',
            city='Sofia',
            user=self.user,
            watering_frequency=1
        )
        url = reverse('edit-plant', kwargs={'plant_slug': plant.slug})
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9'
            b'\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00'
            b'\x00\x02\x02\x4c\x01\x00\x3b'
        )
        test_image = SimpleUploadedFile('test.gif', small_gif, content_type='image/gif')

        data = {
            'plant_name': 'Updated Photo Plant',
            'city': 'Plovdiv',
            'watering_frequency': 5,
            'fertilizing_frequency': 0,
            'pruning_frequency': 0,
            'image': test_image,
        }

        response = self.client.post(url, data=data)

        if response.status_code != 302:
            print(response.context['form'].errors)

        self.assertEqual(response.status_code, 302)
        plant.refresh_from_db()
        self.assertTrue(plant.image)

    def test_plant_favourite_toggle(self):
        plant = Plant.objects.create(plant_name='Fern', city='Varna', user=self.user)
        url = reverse('favourite-plant', kwargs={'plant_slug': plant.slug})

        self.client.get(url)
        self.assertIn(self.user, plant.favourite_by.all())

        self.client.get(url)
        self.assertNotIn(self.user, plant.favourite_by.all())

    def test_suggest_tag_view(self):
        url = reverse('suggest-tag')
        response = self.client.post(url, {'tag_name': 'Super New Tag'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Tag.objects.filter(tag_name='Super New Tag').exists())
