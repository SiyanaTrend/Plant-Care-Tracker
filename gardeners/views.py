from django.urls import reverse_lazy
from django.views.generic import CreateView

from gardeners.forms import GardenerCreateForm
from gardeners.models import Gardener


class GardenerCreateView(CreateView):
    model = Gardener
    form_class = GardenerCreateForm
    template_name = 'gardeners/create-gardener.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form: GardenerCreateForm):
        return super().form_valid(form)