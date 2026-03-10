from django.core.validators import MinLengthValidator
from django.db import models

from gardeners.validators import LettersDigitsOnlyValidator, FirstAndLastNameValidator


class Gardener(models.Model):
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
    )
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(2, 'Your name must be at least 2 chars long!'),
            FirstAndLastNameValidator(),
        ],
        help_text='*Starts with a capital letter. Letters and hyphens only.',
    )
    last_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(2, 'Your name must be at least 2 chars long!'),
            FirstAndLastNameValidator(),
        ],
        help_text='*Starts with a capital letter. Letters and hyphens only.',
    )
    email = models.EmailField(
        max_length=40,
        unique=True,
        error_messages={
            'unique': 'That email is already registered!'
        },
    )
    about_me = models.TextField(
        null=True,
        blank=True,
    )
    profile_picture = models.URLField(
        null=True,
        blank=True,
    )
    is_pro = models.BooleanField(
        default=False,
    )

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.nickname

