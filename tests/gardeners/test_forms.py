from django.test import TestCase
from django.contrib.auth import get_user_model
from gardeners.forms import GardenerEditForm
from gardeners.models import Gardener

User = get_user_model()


class GardenerFormsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='test@test.com', password='password123')
        self.gardener = Gardener.objects.get(user=self.user)

    def test_gardener_edit_form_valid_data(self):
        form = GardenerEditForm(data={
            'nickname': 'GreenMaster',
            'first_name': 'Ivan',
            'last_name': 'Ivanov',
            'is_pro': True,
            'about_me': 'Testing bio section'
        }, instance=self.gardener)

        self.assertTrue(form.is_valid())

    def test_gardener_form_labels(self):
        form = GardenerEditForm()
        self.assertEqual(form.fields['nickname'].label, 'Nickname:')
        self.assertEqual(form.fields['is_pro'].label, 'Are you a professional gardener?')

    def test_gardener_form_excluded_fields(self):
        form = GardenerEditForm()
        self.assertNotIn('user', form.fields)

    def test_gardener_edit_form_invalid_nickname(self):
        form = GardenerEditForm(data={
            'nickname': 'Invalid_Name!',
            'first_name': 'Ivan'
        }, instance=self.gardener)

        self.assertFalse(form.is_valid())
        self.assertIn('nickname', form.errors)
