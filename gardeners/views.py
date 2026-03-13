from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView

from common.mixins import SingleProfileMixin
from gardeners.forms import GardenerCreateForm, GardenerEditForm
from gardeners.models import Gardener


class GardenerCreateView(CreateView):
    model = Gardener
    form_class = GardenerCreateForm
    template_name = 'gardeners/create-gardener.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form: GardenerCreateForm):
        return super().form_valid(form)


class GardenerDetailsView(SingleProfileMixin, DetailView):
    model = Gardener
    template_name = 'gardeners/gardener-details.html'


class GardenerEditView(SingleProfileMixin, UpdateView):
    model = Gardener
    form_class = GardenerEditForm
    template_name = 'gardeners/edit-gardener.html'
    success_url = reverse_lazy('home')
