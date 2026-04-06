from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from gardeners.models import Gardener
from gardeners.validators import LettersDigitsOnlyValidator, FirstAndLastNameValidator

User = get_user_model()


class GardenerModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(email='gardener@test.com', password='password123')
        self.gardener = Gardener.objects.get(user=self.user)

    def test_full_name_method(self):
        self.gardener.nickname = 'Greeny'
        self.assertEqual(self.gardener.full_name(), 'Greeny')

        self.gardener.first_name = 'Ivan'
        self.gardener.last_name = 'Ivanov'
        self.assertEqual(self.gardener.full_name(), 'Ivan Ivanov')

    def test_letters_digits_validator_invalid(self):
        validator = LettersDigitsOnlyValidator()
        with self.assertRaises(ValidationError):
            validator('Green_Thumb!')

    def test_letters_digits_validator_valid(self):
        validator = LettersDigitsOnlyValidator()
        try:
            validator('Gardener123')
        except ValidationError:
            self.fail("LettersDigitsOnlyValidator raised ValidationError unexpectedly!")

    def test_name_validator_capital_letter(self):
        validator = FirstAndLastNameValidator()
        with self.assertRaises(ValidationError):
            validator('ivan')

    def test_name_validator_invalid_chars(self):
        validator = FirstAndLastNameValidator()
        with self.assertRaises(ValidationError):
            validator('Ivan123')

    def test_name_validator_valid_hyphen(self):
        validator = FirstAndLastNameValidator()
        try:
            validator('Anna-Maria')
        except ValidationError:
            self.fail("FirstAndLastNameValidator raised ValidationError for hyphenated name!")
