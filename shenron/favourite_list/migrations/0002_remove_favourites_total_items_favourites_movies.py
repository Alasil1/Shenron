# Generated by Django 5.1.3 on 2024-11-26 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MoviePage', '0001_initial'),
        ('favourite_list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favourites',
            name='total_items',
        ),
        migrations.AddField(
            model_name='favourites',
            name='movies',
            field=models.ManyToManyField(blank=True, related_name='favourited_by', to='MoviePage.movie'),
        ),
    ]
