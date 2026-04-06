from datetime import date
from notifications.models import Notification


def update_notifications(user):
    plants = user.plants.all()
    today = date.today()

    checks = [
        ('Watering', 'watering_frequency', 30),
        ('Fertilizing', 'fertilizing_frequency', 365),
        ('Pruning', 'pruning_frequency', 365),
    ]

    for plant in plants:
        for action, field, days_in_period in checks:
            freq = getattr(plant, field)
            if freq and freq > 0:
                interval = days_in_period / freq

                last_record = plant.maintenance_records.filter(action=action).order_by('-date').first()

                base_date = last_record.date if last_record else plant.created_at.date()

                if (today - base_date).days > interval:

                    Notification.objects.get_or_create(
                        user=user,
                        plant=plant,
                        action_type=action,
                    )
