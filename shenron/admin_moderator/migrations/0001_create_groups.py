from django.db import migrations

def create_groups_and_permissions(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Permission = apps.get_model('auth', 'Permission')
    ContentType = apps.get_model('contenttypes', 'ContentType')
    User = apps.get_model('auth', 'User')

    admin_group, _ = Group.objects.get_or_create(name='Admin')
    all_permissions = Permission.objects.all()
    admin_group.permissions.set(all_permissions)

    moderator_group, _ = Group.objects.get_or_create(name='Moderator')
    moderator_permissions = Permission.objects.filter(
        codename__in=[
            'delete_topic',
            'delete_post', 
            'delete_comment',
        ]
    )
    moderator_group.permissions.set(moderator_permissions)

class Migration(migrations.Migration):

    dependencies = []

    operations = [
        migrations.RunPython(create_groups_and_permissions),
    ]
