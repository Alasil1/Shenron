from django.db import models
from django.contrib.auth import get_user_model
from MoviePage.models import Movie

User = get_user_model()

class Favourites(models.Model):
    list_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favourites')
    movies = models.ManyToManyField(Movie, blank=True, related_name='favourited_by')

    def __str__(self):
        return f"Favourites List for {self.user.username}"
