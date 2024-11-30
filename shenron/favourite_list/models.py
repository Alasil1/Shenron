from django.db import models
from django.contrib.auth import get_user_model
from MoviePage.models import Movie

User = get_user_model()

class Favourites(models.Model):
    """
    Model representing a user's list of favorite movies.

    Attributes:
        user (User): The user who owns the favorite list.
        movies (ManyToManyField): The movies that are in the user's favorite list.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='favourites')
    movies = models.ManyToManyField(Movie, related_name='favourited_by', blank=True)

    def __str__(self):
        """
        Return a string representation of the favorite list.

        :return: A string representing the user's favorite list.
        """
        return f"{self.user.username}'s Favourite List"
