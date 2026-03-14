from django import forms

from gardeners.models import Gardener


class GardenerBaseForm(forms.ModelForm):
    class Meta:
        model = Gardener
        fields = '__all__'

        labels = {
            'nickname': 'Nickname:',
            'first_name': 'First Name:',
            'last_name': 'Last Name:',
            'email': 'Email:',
            'profile_picture': 'Profile Image:',
            'about_me': 'About Me:',
            'is_pro': 'Are you a professional gardener?',
        }

        widgets = {
            'email': forms.EmailInput(attrs={'placeholder': 'example: john.doe@mail.com'}),
            'profile_picture': forms.URLInput(attrs={'placeholder': 'https://...'}),
            'about_me': forms.Textarea(attrs={'placeholder': 'Share something interesting about you...'}),
        }


class GardenerCreateForm(GardenerBaseForm):
    class Meta(GardenerBaseForm.Meta):
        exclude = ['about_me', 'profile_picture', 'is_pro']
        pass


class GardenerEditForm(GardenerBaseForm):
    pass
