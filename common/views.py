from django.db.models import Count, Max
from django.shortcuts import render
from django.views.generic import TemplateView
from common.mixins import SingleProfileMixin
from maintenance.models import MaintenanceRecord
from plants.models import Plant, Tag


class HomePageView(SingleProfileMixin, TemplateView):
    template_name = 'common/home.html'


def statistics_view(request):
    all_plants = Plant.objects.all()
    total_records = MaintenanceRecord.objects.count()

    max_actions = all_plants.annotate(
        actions=Count('maintenance_records')
    ).aggregate(Max('actions'))['actions__max']

    star_plants = []
    if max_actions and max_actions > 0:
        star_plants = all_plants.annotate(
            actions=Count('maintenance_records')
        ).filter(actions=max_actions)

    max_favs = all_plants.annotate(
        fav_count=Count('favourite_by')
    ).aggregate(Max('fav_count'))['fav_count__max']

    most_loved = []
    if max_favs and max_favs > 0:
        most_loved = all_plants.annotate(
            fav_count=Count('favourite_by')
        ).filter(fav_count=max_favs)

    top_tags = Tag.objects.annotate(
        count=Count('plants')
    ).filter(count__gt=0).order_by('-count')[:3]

    context = {
        'total_plants': all_plants.count(),
        'total_records': total_records,
        'top_tags': top_tags,
        'star_plants': star_plants,
        'most_loved': most_loved,
        'max_actions': max_actions,
        'all_plants': all_plants,
    }
    return render(request, 'common/statistics.html', context)
