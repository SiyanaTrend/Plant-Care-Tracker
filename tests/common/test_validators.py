from django.test import TestCase
from django.core.exceptions import ValidationError
from common.validators import FileSizeValidator


class MockFile:
    def __init__(self, size):
        self.size = size


class ValidatorTests(TestCase):
    def test_file_size_validator_raises_error_when_too_large(self):
        validator = FileSizeValidator(5)
        large_file = MockFile(6 * 1024 * 1024 + 1)

        with self.assertRaises(ValidationError) as cm:
            validator(large_file)
        self.assertEqual(cm.exception.message, "File size must be less than 5MB!")

    def test_file_size_validator_passes_when_valid(self):
        validator = FileSizeValidator(5)
        small_file = MockFile(4 * 1024 * 1024)

        try:
            validator(small_file)
        except ValidationError:
            self.fail("FileSizeValidator raised ValidationError unexpectedly!")
