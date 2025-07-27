from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from bookshelf.models import Article
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Create groups and assign permissions'

    def handle(self, *args, **kwargs):
        # Define your group names
        groups_permissions = {
            'Admins': ['can_view', 'can_create', 'can_edit', 'can_delete'],
            'Editors': ['can_view', 'can_create', 'can_edit'],
            'Viewers': ['can_view'],
        }

        article_ct = ContentType.objects.get_for_model(Article)

        for group_name, perm_codes in groups_permissions.items():
            group, created = Group.objects.get_or_create(name=group_name)
            for perm_code in perm_codes:
                try:
                    permission = Permission.objects.get(codename=perm_code, content_type=article_ct)
                    group.permissions.add(permission)
                except Permission.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f'Permission {perm_code} does not exist'))
            self.stdout.write(self.style.SUCCESS(f'Updated group: {group_name}'))

        self.stdout.write(self.style.SUCCESS('Groups and permissions setup complete.'))
