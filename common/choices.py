from django.db import models


class ActionPlantChoices(models.TextChoices):
    WATERING = 'Watering', 'Watering'
    FERTILIZING = 'Fertilizing', 'Fertilizing'
    PRUNING = 'Pruning', 'Pruning'
    REPOTTING = 'Repotting', 'Repotting'
    OTHER = 'Other', 'Other'
