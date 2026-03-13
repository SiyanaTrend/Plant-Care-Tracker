from django.views.generic import ListView
from common.mixins import SingleProfileMixin
from plants.models import Plant


class PlantsListView(SingleProfileMixin, ListView):
    model = Plant
    template_name = 'plants/catalogue.html'
    context_object_name = 'plants'
