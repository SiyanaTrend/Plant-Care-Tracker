from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class LettersDigitsOnlyValidator:
    def __init__(self, message: str = 'The nickname must contain only letters and digits!'):
        self.message = message

    def __call__(self, value: str, *args, **kwargs):
        if not value.isalnum():
            raise ValidationError(self.message)


@deconstructible
class FirstAndLastNameValidator:
    def __init__(self, message: str = 'The name must start with a capital letter and contain only letters and hyphens!'):
        self.message = message

    def __call__(self, value: str, *args, **kwargs):
        if not value[0].isupper():
            raise ValidationError(self.message)

        for char in value:
            if not (char.isalpha() or char == '-'):
                raise ValidationError(self.message)
