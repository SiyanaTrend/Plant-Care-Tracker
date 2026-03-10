from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class PlantNameValidator:
    def __init__(self, message: str = 'А plant name can only contain letters, digits, spaces and hyphens!'):
        self.message = message

    def __call__(self, value: str, *args, **kwargs):
        for char in value:
            if not (char.isalpha() or char.isdigit() or char in [' ', '-']):
                raise ValidationError(self.message)
