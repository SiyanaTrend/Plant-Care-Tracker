import random
from django.conf import settings
from django.core.validators import MinLengthValidator, MinValueValidator, MaxValueValidator, ValidationError
from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from plants.validators import PlantNameValidator


class Tag(models.Model):
    tag_name = models.CharField(
        max_length=60,
        unique=True,
    )
    is_approved = models.BooleanField(
        default=False
    )

    def _normalize_name(self):
        return self.tag_name.strip().title()

    def clean(self):
        normalized = self._normalize_name()

        if Tag.objects.filter(tag_name__iexact=normalized).exclude(pk=self.pk).exists():
            raise ValidationError({'tag_name': 'That tag is already registered!'})

    def save(self, *args, **kwargs):
        self.tag_name = self._normalize_name()
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['tag_name']

    def __str__(self):
        return self.tag_name


class Plant(models.Model):
    plant_name = models.CharField(
        max_length=100,
        validators=[
            MinLengthValidator(3, 'The plant name must be at least 3 chars long!'),
            PlantNameValidator(),
        ],
        help_text='*Allowed plant names can contain letters, digits, spaces and hyphens.'
    )
    species = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    image = CloudinaryField(
        'image',
        null=True,
        blank=True,
    )
    city = models.CharField(
        max_length=50,
        help_text='*The city where the plant is located.'
    )
    address = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        help_text='*Optional: apartment, floor, or specific spot (e.g., "Balcony").'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    watering_frequency = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(60),
        ],
        help_text='*Share how many times per month the plant needs watering.',
    )
    fertilizing_frequency = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(24),
        ],
        help_text='*How many times per year should this plant be fertilized?'
    )
    pruning_frequency = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(12),
        ],
        help_text='*How many times per year should this plant be pruned?'
    )
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='plants',
    )
    tags = models.ManyToManyField(
        to='Tag',
        related_name='plants',
        blank=True,
    )
    favourite_by = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        related_name='favourite_plants',
        blank=True,
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=False,
    )

    class Meta:
        ordering = ['plant_name']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = f"{slugify(self.plant_name)}-{random.randint(1, 1000)}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.plant_name} - {self.city} ({self.address})'
