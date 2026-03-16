from django import forms

from common.mixins import ReadOnlyMixin, HiddenHelpText
from plants.models import Plant


class PlantBaseForm(forms.ModelForm):
    class Meta:
        model = Plant
        exclude = ['gardener']

        labels = {
            'plant_name': 'Plant Name:',
            'species': 'Species:',
            'description': 'Description:',
            'image_url': 'Plant Image:',
            'city': 'City:',
            'address': 'Address:',
            'watering_frequency': 'Watering Frequency (monthly):',
            'fertilizing_frequency': 'Fertilizing Frequency (yearly):',
            'pruning_frequency': 'Pruning Frequency (yearly):',
            'tags': 'Tags:',
        }

        help_texts = {
            'tags': '*Hold Ctrl (or Cmd) to select more than one.',
        }

        widgets = {
            'plant_name': forms.TextInput(attrs={'placeholder': 'example: Monstera Deliciosa'}),
            'species': forms.TextInput(attrs={'placeholder': 'example: Monstera'}),
            'description': forms.Textarea(attrs={
                'placeholder': 'Share more about your green friend...',
                'rows': 3,
            }),
            'image_url': forms.URLInput(attrs={'placeholder': 'https://...'}),
            'city': forms.TextInput(),
            'address': forms.TextInput(),
            'tags': forms.SelectMultiple(attrs={'class': 'tags-select'})
        }

        error_messages = {
            'image_url': {
                'invalid': 'This URL is not valid. Please enter a valid image link!',
            }
        }


class PlantCreateForm(PlantBaseForm):
    class Meta(PlantBaseForm.Meta):
        exclude = ['gardener', 'species', 'image_url', 'watering_frequency', 'fertilizing_frequency',
                   'pruning_frequency']
        pass


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(ReadOnlyMixin, HiddenHelpText, PlantBaseForm):
    read_only_fields = ['plant_name', 'city', 'address']

    class Meta(PlantBaseForm.Meta):
        exclude = ['gardener', 'species', 'description', 'image_url', 'watering_frequency', 'fertilizing_frequency',
                   'pruning_frequency', 'tags']
