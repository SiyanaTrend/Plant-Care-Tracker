from django.db import models
from common.choices import ActionPlantChoices


class MaintenanceRecord(models.Model):
    action = models.CharField(
        max_length=20,
        choices=ActionPlantChoices.choices,
        default=ActionPlantChoices.OTHER,
    )
    date = models.DateField(
        auto_now_add=False,
        help_text='*When was the care provided?'
    )
    notes = models.TextField(
        blank=True,
        null=True,
        help_text='*Optional: e.g., "Added 500ml water" or "Used bio-fertilizer".'
    )
    plant = models.ForeignKey(
        to='plants.Plant',
        on_delete=models.CASCADE,
        related_name='maintenance_records'
    )

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f'{self.plant.plant_name} - {self.action} ({self.date})'
