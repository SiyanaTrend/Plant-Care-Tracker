from django import forms

from common.mixins import ReadOnlyMixin, HiddenHelpText
from maintenance.models import MaintenanceRecord


class MaintenanceBaseForm(forms.ModelForm):
    class Meta:
        model = MaintenanceRecord
        exclude = ['plant']

        labels = {
            'action': 'Care Action:',
            'date': 'Add on:',
            'notes': 'Notes:',
        }

        widgets = {
            'action': forms.RadioSelect(attrs={'class': 'action-radio'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'notes': forms.Textarea(attrs={
                'placeholder': 'Share more about your care actions...',
                'rows': 3,
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        date = cleaned_data.get('date')

        plant = self.instance.plant

        if plant and date and date < plant.created_at.date():
            self.add_error(
                'date',
                f"Date cannot be before plant creation date ({plant.created_at.date()})."
            )

        return cleaned_data


class MaintenanceCreateForm(MaintenanceBaseForm):
    pass


class MaintenanceEditForm(MaintenanceBaseForm):
    pass


class MaintenanceDeleteForm(ReadOnlyMixin, HiddenHelpText, MaintenanceBaseForm):
    action = forms.CharField(widget=forms.TextInput())
    read_only_fields = ['date', 'action']

    class Meta(MaintenanceBaseForm.Meta):
        exclude = ['plant', 'notes']
