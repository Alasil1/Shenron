from django.db import models
from django.contrib.auth import get_user_model
from MoviePage.models import Movie

User = get_user_model()

class Favourites(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='favourites')
    movies = models.ManyToManyField(Movie, related_name='favourited_by', blank=True)

    def __str__(self):
        return f"{self.user.username}'s Favourite List"
