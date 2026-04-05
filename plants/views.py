from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from plants.forms import PlantCreateForm, PlantEditForm, PlantDeleteForm, SuggestTagForm
from plants.models import Plant, Tag


class SuggestTagView(LoginRequiredMixin, CreateView):
    model = Tag
    form_class = SuggestTagForm
    template_name = 'plants/suggest-tag.html'
    success_url = reverse_lazy('catalogue')

    def form_valid(self, form):
        return super().form_valid(form)


class PlantFavouriteView(LoginRequiredMixin, View):
    def get(self, request, plant_slug):
        plant = get_object_or_404(Plant, slug=plant_slug)

        if request.user in plant.favourite_by.all():
            plant.favourite_by.remove(request.user)
        else:
            plant.favourite_by.add(request.user)

        return redirect('plant-details', plant_slug=plant.slug)

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
    slug_url_kwarg = 'plant_slug'


class PlantEditView(LoginRequiredMixin, UpdateView):
    model = Plant
    form_class = PlantEditForm
    template_name = 'plants/edit-plant.html'
    slug_url_kwarg = 'plant_slug'

    def get_success_url(self):
        return reverse('plant-details', kwargs={'plant_slug': self.object.slug})


class PlantDeleteView(LoginRequiredMixin, DeleteView):
    model = Plant
    form_class = PlantDeleteForm
    template_name = 'plants/delete-plant.html'
    slug_url_kwarg = 'plant_slug'
    success_url = reverse_lazy('catalogue')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.object
        return kwargs
