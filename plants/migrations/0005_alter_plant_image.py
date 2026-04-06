import cloudinary.models
import common.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plants', '0004_approving_data_migrations_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plant',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, validators=[common.validators.FileSizeValidator(5)], verbose_name='image'),
        ),
    ]
