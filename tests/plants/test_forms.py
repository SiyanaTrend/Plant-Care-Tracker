from django.test import TestCase
from plants.forms import PlantCreateForm, SuggestTagForm, PlantBaseForm
from plants.models import Tag


class PlantFormsTests(TestCase):
    def setUp(self):
        Tag.objects.get_or_create(tag_name='Indoor', defaults={'is_approved': True})
        Tag.objects.get_or_create(tag_name='Hidden', defaults={'is_approved': False})

    def test_suggest_tag_form_valid_data(self):
        form = SuggestTagForm(data={'tag_name': 'New Tropical'})
        self.assertTrue(form.is_valid())

    def test_suggest_tag_form_empty_data(self):
        form = SuggestTagForm(data={})
        self.assertFalse(form.is_valid())
        self.assertIn('tag_name', form.errors)

    def test_plant_base_form_tags_queryset_filter(self):
        form = PlantBaseForm()
        queryset = form.fields['tags'].queryset
        self.assertTrue(queryset.filter(tag_name='Indoor').exists())
        self.assertFalse(queryset.filter(tag_name='Hidden', is_approved=False).exists())

    def test_plant_create_form_excluded_fields(self):
        form = PlantCreateForm()
        excluded = ['species', 'image', 'watering_frequency', 'user']
        for field in excluded:
            self.assertNotIn(field, form.fields)

    def test_plant_create_form_valid_data(self):
        form = PlantCreateForm(data={
            'plant_name': 'Valid Plant',
            'city': 'Sofia',
            'address': 'Main St 1',
        })
        self.assertTrue(form.is_valid())