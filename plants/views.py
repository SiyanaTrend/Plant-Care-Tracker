from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from common.mixins import SingleProfileMixin

from plants.forms import PlantCreateForm, PlantEditForm, PlantDeleteForm
from plants.models import Plant


class PlantsListView(LoginRequiredMixin, ListView):
    model = Plant
    template_name = 'plants/catalogue.html'
    context_object_name = 'plants'

    def get_queryset(self):
        return Plant.objects.filter(user=self.request.user)


class PlantCreateView(LoginRequiredMixin, CreateView):
    model = Plant
    form_class = PlantCreateForm
    template_name = 'plants/create-plant.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form: PlantCreateForm):
        form.instance.user = self.request.user
        return super().form_valid(form)


class PlantDetailsView(LoginRequiredMixin, DetailView):
    model = Plant
    template_name = 'plants/plant-details.html'
    pk_url_kwarg = 'plant_pk'


class PlantEditView(LoginRequiredMixin, UpdateView):
    model = Plant
    form_class = PlantEditForm
    template_name = 'plants/edit-plant.html'
    pk_url_kwarg = 'plant_pk'

    def get_success_url(self):
        return reverse('plant-details', kwargs={'plant_pk': self.object.pk})


class PlantDeleteView(LoginRequiredMixin, DeleteView):
    model = Plant
    form_class = PlantDeleteForm
    template_name = 'plants/delete-plant.html'
    pk_url_kwarg = 'plant_pk'
    success_url = reverse_lazy('catalogue')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
