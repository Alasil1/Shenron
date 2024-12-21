# Generated by Django 5.1.3 on 2024-12-21 17:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("forum", "0003_alter_comment_options_alter_post_options_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="followers",
            field=models.ManyToManyField(
                related_name="followed_topics", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]