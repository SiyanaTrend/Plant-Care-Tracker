from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from common.mixins import SingleProfileMixin
from gardeners.forms import GardenerEditForm
from gardeners.models import Gardener


class GardenerDetailsView(LoginRequiredMixin, SingleProfileMixin, DetailView):
    model = Gardener
    template_name = 'gardeners/gardener-details.html'


class GardenerEditView(LoginRequiredMixin, SingleProfileMixin, UpdateView):
    model = Gardener
    form_class = GardenerEditForm
    template_name = 'gardeners/edit-gardener.html'
    success_url = reverse_lazy('gardener-details')


class GardenerDeleteView(LoginRequiredMixin, SingleProfileMixin, DeleteView):
    model = Gardener
    template_name = 'gardeners/delete-gardener.html'
    success_url = reverse_lazy('home')
