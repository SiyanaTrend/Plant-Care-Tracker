from django.test import TestCase
from accounts.forms import AppUserCreationForm, AppUserChangeForm
from django.contrib.auth import get_user_model

User = get_user_model()


class AccountFormsTests(TestCase):

    def test_user_creation_form_valid_data(self):
        form = AppUserCreationForm(data={
            'email': 'newuser@test.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!',
        })
        self.assertTrue(form.is_valid(), form.errors)

    def test_user_creation_form_invalid_email(self):
        form = AppUserCreationForm(data={
            'email': 'not-an-email',
            'password1': 'password123',
            'password2': 'password123',
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_user_change_form_meta_model(self):
        form = AppUserChangeForm()
        self.assertEqual(form.Meta.model, User)
        self.assertEqual(form.Meta.fields, ['email'])
