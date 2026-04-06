from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from gardeners.models import Gardener

User = get_user_model()


class GardenerViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='view@test.com', password='password123')
        self.client.login(email='view@test.com', password='password123')
        self.gardener = Gardener.objects.get(user=self.user)

    def test_gardener_details_view(self):
        url = reverse('gardener-details')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'gardeners/gardener-details.html')

    def test_gardener_edit_post(self):
        url = reverse('edit-gardener')
        data = {
            'nickname': 'MasterGardener',
            'first_name': 'George',
            'last_name': 'Green',
            'is_pro': True,
            'about_me': 'I love plants!'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)

        self.gardener.refresh_from_db()
        self.assertEqual(self.gardener.nickname, 'MasterGardener')
        self.assertTrue(self.gardener.is_pro)

    def test_gardener_edit_profile_picture(self):
        url = reverse('edit-gardener')
        small_gif = (
            b'\x47\x49\x46\x38\x39\x61\x01\x00\x01\x00\x00\x00\x00\x21\xf9'
            b'\x04\x01\x0a\x00\x01\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00'
            b'\x00\x02\x02\x4c\x01\x00\x3b'
        )
        test_image = SimpleUploadedFile('profile.gif', small_gif, content_type='image/gif')

        data = {
            'nickname': 'NewNick',
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'profile_picture': test_image,
        }

        response = self.client.post(url, data=data)

        self.assertEqual(response.status_code, 302)
        self.gardener.refresh_from_db()
        self.assertTrue(self.gardener.profile_picture)
