from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from accounts.forms import AppUserCreationForm

User = get_user_model()


class RegisterAppUserView(CreateView):
    model = User
    form_class = AppUserCreationForm
    template_name = 'accounts/register.html'
    success_url = reverse_lazy('login')


class AppUserLoginView(LoginView):
    template_name = 'accounts/login.html'


class AppUserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
