from django.test import TestCase
from common.choices import ActionPlantChoices


class ChoicesTests(TestCase):
    def test_action_plant_choices(self):
        self.assertEqual(ActionPlantChoices.WATERING, 'Watering')
        self.assertEqual(ActionPlantChoices.FERTILIZING, 'Fertilizing')
        self.assertEqual(ActionPlantChoices.PRUNING, 'Pruning')
        self.assertEqual(ActionPlantChoices.REPOTTING, 'Repotting')
        self.assertEqual(ActionPlantChoices.OTHER, 'Other')
