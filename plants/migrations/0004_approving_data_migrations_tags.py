from django.db import migrations


def approve_existing_tags(apps, schema_editor):
    Tag = apps.get_model('plants', 'Tag')

    Tag.objects.all().update(is_approved=True)


class Migration(migrations.Migration):
    dependencies = [
        ('plants', '0003_tag_is_approved'),
    ]

    operations = [
        migrations.RunPython(approve_existing_tags),
    ]
