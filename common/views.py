from django.views.generic import TemplateView
from common.mixins import SingleProfileMixin


class HomePageView(SingleProfileMixin, TemplateView):
    template_name = 'common/home.html'
