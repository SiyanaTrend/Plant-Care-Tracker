from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models
from cloudinary.models import CloudinaryField
from gardeners.validators import LettersDigitsOnlyValidator, FirstAndLastNameValidator


class Gardener(models.Model):
    user = models.OneToOneField(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    nickname = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(3, 'Your nickname must be at least 3 chars long!'),
            LettersDigitsOnlyValidator(),
        ],
        unique=True,
        error_messages={
            'unique': 'That nickname is already in use!'
        },
        help_text='*Allowed nicknames can contain only letters and digits.',
        null=True,
        blank=True,
    )
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(2, 'Your name must be at least 2 chars long!'),
            FirstAndLastNameValidator(),
        ],
        help_text='*Starts with a capital letter. Letters and hyphens only.',
        null=True,
        blank=True,
    )
    last_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(2, 'Your name must be at least 2 chars long!'),
            FirstAndLastNameValidator(),
        ],
        help_text='*Starts with a capital letter. Letters and hyphens only.',
        null=True,
        blank=True,
    )
    about_me = models.TextField(
        null=True,
        blank=True,
    )
    profile_picture = CloudinaryField(
        'image',
        null=True,
        blank=True,
    )
    is_pro = models.BooleanField(
        default=False,
    )

    def full_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        return self.nickname or 'Anonymous Gardener'

    def __str__(self):
        return self.nickname

