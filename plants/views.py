from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from common.mixins import SingleProfileMixin
from common.utils import get_profile
from plants.forms import PlantCreateForm, PlantEditForm, PlantDeleteForm
from plants.models import Plant


class PlantsListView(SingleProfileMixin, ListView):
    model = Plant
    template_name = 'plants/catalogue.html'
    context_object_name = 'plants'


class PlantCreateView(CreateView):
    model = Plant
    form_class = PlantCreateForm
    template_name = 'plants/create-plant.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form: PlantCreateForm):
        form.instance.gardener = get_profile()
        return super().form_valid(form)


class PlantDetailsView(DetailView):
    model = Plant
    template_name = 'plants/plant-details.html'
    pk_url_kwarg = 'plant_pk'


class PlantEditView(UpdateView):
    model = Plant
    form_class = PlantEditForm
    template_name = 'plants/edit-plant.html'
    pk_url_kwarg = 'plant_pk'

    def get_success_url(self):
        return reverse('plant-details', kwargs={'plant_pk': self.object.pk})


class PlantDeleteView(DeleteView):
    model = Plant
    form_class = PlantDeleteForm
    template_name = 'plants/delete-plant.html'
    pk_url_kwarg = 'plant_pk'
    success_url = reverse_lazy('catalogue')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
