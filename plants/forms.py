from django import forms

from common.mixins import ReadOnlyMixin, HiddenHelpText
from plants.models import Plant, Tag


class SuggestTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['tag_name']


class PlantBaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'tags' in self.fields:
            from plants.models import Tag
            self.fields['tags'].queryset = Tag.objects.filter(is_approved=True)

    class Meta:
        model = Plant
        exclude = ['user', 'favourite_by', 'slug']

        labels = {
            'plant_name': 'Plant Name:',
            'species': 'Species:',
            'description': 'Description:',
            'image': 'Plant Image:',
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
            'city': forms.TextInput(),
            'address': forms.TextInput(),
            'tags': forms.SelectMultiple(attrs={'class': 'tags-select'})
        }


class PlantCreateForm(PlantBaseForm):
    class Meta(PlantBaseForm.Meta):
        exclude = ['user', 'favourite_by', 'slug', 'species', 'image',
                   'watering_frequency', 'fertilizing_frequency',
                   'pruning_frequency']


class PlantEditForm(PlantBaseForm):
    pass


class PlantDeleteForm(ReadOnlyMixin, HiddenHelpText, PlantBaseForm):
    read_only_fields = ['plant_name', 'city', 'address']

    class Meta(PlantBaseForm.Meta):
        fields = ['plant_name', 'city', 'address']
