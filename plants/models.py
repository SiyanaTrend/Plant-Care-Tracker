from django.core.validators import MinLengthValidator
from django.db import models

from plants.validators import PlantNameValidator


class Tag(models.Model):
    tag_name = models.CharField(
        max_length=60,
        unique=True,
        error_messages={
            'unique': 'That tag is already registered!'
        },
    )

    class Meta:
        ordering = ['tag_name']

    def __str__(self):
        return self.tag_name


class Plant(models.Model):
    plant_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(5, 'The plant name must be at least 5 chars long!'),
            PlantNameValidator(),
        ],
    )
    species = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    description = models.TextField()

    image_url = models.URLField(
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=50,
        help_text='The city where the plant is located.'
    )

    address = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='Optional: Apartment, floor, or specific spot (e.g., "Balcony").'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    gardener = models.ForeignKey(
        to='gardeners.Gardener',
        on_delete=models.CASCADE,
        related_name='plants',
    )

    tags = models.ManyToManyField(
        to='Tag',
        related_name='plants',
        blank=True,
    )

    class Meta:
        ordering = ['plant_name']

    def __str__(self):
        return self.plant_name
