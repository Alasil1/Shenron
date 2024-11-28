# Generated by Django 5.1.3 on 2024-11-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Movie",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("title", models.CharField(max_length=255)),
                ("vote_average", models.FloatField()),
                ("vote_count", models.IntegerField()),
                ("status", models.CharField(max_length=50)),
                ("release_date", models.DateField()),
                ("revenue", models.BigIntegerField()),
                ("runtime", models.IntegerField()),
                ("adult", models.BooleanField()),
                ("backdrop_path", models.CharField(max_length=255)),
                ("budget", models.BigIntegerField()),
                ("original_language", models.CharField(max_length=10)),
                ("overview", models.TextField()),
                ("poster_path", models.CharField(max_length=255)),
                ("tagline", models.CharField(max_length=255)),
                ("genres", models.CharField(max_length=255)),
                ("keywords", models.CharField(max_length=255)),
            ],
        ),
    ]
