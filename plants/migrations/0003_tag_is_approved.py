from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0002_add_initial_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
    ]
