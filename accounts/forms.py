from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

User = get_user_model()


class AppUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email']


class AppUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = User
        fields = ['email']
