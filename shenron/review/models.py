from django.db import models
from MoviePage.models import Movie
from django.contrib.auth import get_user_model

User = get_user_model()
class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    plot = models.IntegerField()
    acting = models.IntegerField()
    cinematography = models.IntegerField()
    music = models.IntegerField()
    character_development = models.IntegerField()
    pacing = models.IntegerField()
    overall = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

