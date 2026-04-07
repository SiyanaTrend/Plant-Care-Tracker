from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Create groups and assign permissions'

    def handle(self, *args, **kwargs):
        gardeners_group, _ = Group.objects.get_or_create(name='Gardeners')
        gardener_perms = [
            'add_plant', 'change_plant', 'delete_plant', 'view_plant',
            'add_maintenancerecord', 'change_maintenancerecord', 'delete_maintenancerecord', 'view_maintenancerecord',
            'view_notification', 'change_notification',
            'change_gardener', 'view_gardener', 'add_tag'
        ]
        for perm_code in gardener_perms:
            try:
                perm = Permission.objects.get(codename=perm_code)
                gardeners_group.permissions.add(perm)
            except Permission.DoesNotExist:
                continue

        moderators_group, _ = Group.objects.get_or_create(name='Moderators')
        mod_perms = [
            'add_tag', 'change_tag', 'delete_tag', 'view_tag',
            'view_plant', 'delete_plant',
            'view_maintenancerecord',
            'view_notification'
        ]
        for perm_code in mod_perms:
            try:
                perm = Permission.objects.get(codename=perm_code)
                moderators_group.permissions.add(perm)
            except Permission.DoesNotExist:
                continue

        self.stdout.write(self.style.SUCCESS('Groups and permissions fixed successfully'))
