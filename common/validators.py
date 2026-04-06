from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class FileSizeValidator:
    def __init__(self, max_size_mb):
        self.max_size_mb = max_size_mb

    def __call__(self, value):
        if not hasattr(value, 'size'):
            return

        if value.size > self.max_size_mb * 1024 * 1024:
            raise ValidationError(f'File size must be less than {self.max_size_mb}MB!')

    def __eq__(self, other):
        return (
                isinstance(other, FileSizeValidator) and
                self.max_size_mb == other.max_size_mb
        )
