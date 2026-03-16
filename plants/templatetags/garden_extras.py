from datetime import date
from django import template

register = template.Library()


@register.simple_tag
def garden_health_details(plants):
    if not plants.exists():
        return {'score': 0, 'needs_attention': []}

    total_plants = plants.count()
    healthy_plants = 0
    needs_attention = []
    today = date.today()

    for plant in plants:
        last_watering = plant.maintenance_records.filter(
            action='Watering'
        ).order_by('-date').first()

        days_interval = 30 / plant.watering_frequency

        if last_watering:
            days_since_last = (today - last_watering.date).days
            if days_since_last <= (days_interval + 1):
                healthy_plants += 1
            else:
                needs_attention.append(plant)
        else:
            days_since_creation = (today - plant.created_at.date()).days
            if days_since_creation <= (days_interval + 1):
                healthy_plants += 1
            else:
                needs_attention.append(plant)

    score = round((healthy_plants / total_plants) * 100)

    return {
        'score': score,
        'needs_attention': needs_attention
    }
