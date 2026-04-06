from django.db import models
from django.conf import settings
from plants.models import Plant
from common.choices import ActionPlantChoices


class Notification(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='notifications',
    )

    plant = models.ForeignKey(
        to='plants.Plant',
        on_delete=models.CASCADE,
        related_name='notifications',
    )

    action_type = models.CharField(
        max_length=20,
        choices=ActionPlantChoices.choices,
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
    )

    class Meta:
        ordering = ['-created_at']

    @property
    def last_action_date(self):
        return self.plant.get_last_date_for_action(self.action_type)

    def __str__(self):
        return f'{self.action_type} alert for {self.plant.plant_name}'
