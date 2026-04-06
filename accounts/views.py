from django.contrib.auth import get_user_model
from django.shortcuts import redirect
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

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('catalogue')
        return super().dispatch(request, *args, **kwargs)


class AppUserLoginView(LoginView):
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


class AppUserLogoutView(LogoutView):
    template_name = 'accounts/logout.html'
