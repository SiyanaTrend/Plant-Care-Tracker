from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core import mail
from gardeners.models import Gardener

User = get_user_model()


class AppUserModelTests(TestCase):
    def test_create_user_successful(self):
        email='testuser@example.com'
        password = 'password123'
        user = User.objects.create_user(email=email, password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_superuser_successful(self):
        user = User.objects.create_superuser(email='admin@test.com', password='adminpassword')
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

    def test_create_user_no_email_raises_error(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email=None, password='password123')

    def test_gardener_profile_created_on_registration(self):
        user = User.objects.create_user(email='newgardener@test.com', password='password')
        self.assertTrue(Gardener.objects.filter(user=user).exists())

    def test_welcome_email_sent_on_registration(self):
        User.objects.create_user(email='emailtest@test.com', password='password')
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "New account created")
