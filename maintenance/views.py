from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from maintenance.forms import MaintenanceCreateForm, MaintenanceEditForm, MaintenanceDeleteForm
from maintenance.models import MaintenanceRecord
from plants.models import Plant


class MaintenanceDetailsView(LoginRequiredMixin, DetailView):
    model = Plant
    template_name = 'maintenance/maintenance-details.html'
    slug_url_kwarg = 'plant_slug'
    context_object_name = 'plant'


class MaintenanceCreateView(LoginRequiredMixin, CreateView):
    model = MaintenanceRecord
    form_class = MaintenanceCreateForm
    template_name = 'maintenance/create-maintenance.html'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        plant = get_object_or_404(Plant, slug=self.kwargs['plant_slug'])
        kwargs['instance'] = MaintenanceRecord(plant=plant)
        return kwargs

    def get_success_url(self):
        return reverse('maintenance-details', kwargs={'plant_slug': self.kwargs['plant_slug']})


class MaintenanceEditView(LoginRequiredMixin, UpdateView):
    model = MaintenanceRecord
    form_class = MaintenanceEditForm
    template_name = 'maintenance/edit-maintenance.html'
    pk_url_kwarg = 'maintenance_pk'

    def get_success_url(self):
        return reverse('maintenance-details', kwargs={'plant_slug': self.object.plant.slug})


class MaintenanceDeleteView(LoginRequiredMixin, DeleteView):
    model = MaintenanceRecord
    form_class = MaintenanceDeleteForm
    template_name = 'maintenance/delete-maintenance.html'
    pk_url_kwarg = 'maintenance_pk'

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def get_success_url(self):
        return reverse('maintenance-details', kwargs={'plant_slug': self.object.plant.slug})
