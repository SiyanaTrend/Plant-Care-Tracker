from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from maintenance.forms import MaintenanceCreateForm, MaintenanceEditForm, MaintenanceDeleteForm
from maintenance.models import MaintenanceRecord
from plants.models import Plant


class MaintenanceDetailsView(DetailView):
    model = Plant
    template_name = 'maintenance/maintenance-details.html'
    pk_url_kwarg = 'plant_pk'
    context_object_name = 'plant'


class MaintenanceCreateView(CreateView):
    model = MaintenanceRecord
    form_class = MaintenanceCreateForm
    template_name = 'maintenance/create-maintenance.html'

    def form_valid(self, form: MaintenanceCreateForm):
        plant = get_object_or_404(Plant, pk=self.kwargs['plant_pk'])
        form.instance.plant = plant
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('maintenance-details', kwargs={'plant_pk': self.kwargs['plant_pk']})


class MaintenanceEditView(UpdateView):
    model = MaintenanceRecord
    form_class = MaintenanceEditForm
    template_name = 'maintenance/edit-maintenance.html'
    pk_url_kwarg = 'maintenance_pk'

    def get_success_url(self):
        plant_id = self.object.plant.pk
        return reverse('maintenance-details', kwargs={'plant_pk': plant_id})


class MaintenanceDeleteView(DeleteView):
    model = MaintenanceRecord
    form_class = MaintenanceDeleteForm
    template_name = 'maintenance/delete-maintenance.html'
    pk_url_kwarg = 'maintenance_pk'
    success_url = reverse_lazy('catalogue')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs

    def get_success_url(self):
        plant_id = self.object.plant.pk
        return reverse('maintenance-details', kwargs={'plant_pk': plant_id})
