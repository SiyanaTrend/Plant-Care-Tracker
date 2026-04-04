from django import forms

from gardeners.models import Gardener


class GardenerBaseForm(forms.ModelForm):
    class Meta:
        model = Gardener
        exclude = ['user']

        labels = {
            'nickname': 'Nickname:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'profile_picture': 'Profile Image:',
            'about_me': 'About Me:',
            'is_pro': 'Are you a professional gardener?',
        }

        widgets = {
            'about_me': forms.Textarea(attrs={
                'placeholder': 'Share something interesting about you...',
                'rows': 3,
            }),
        }


class GardenerEditForm(GardenerBaseForm):
    pass
