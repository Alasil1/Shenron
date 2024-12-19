from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view

from .models import Movie
import requests
# from PIL import Image
# from io import BytesIO
# from colorthief import ColorThief
def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    trailers,images=movie.get_videos()
    # print(images)
    trailer_image_pairs = zip(trailers, images)
    return render(request, 'movie.html', {'movie': movie, 'trailers':trailer_image_pairs })

def all_movies(request):
    movies = Movie.objects.filter(vote_count__gt=1000).order_by('-vote_average')[0:20]
    return render(request, 'all_movies.html', {'movies': movies})

def home(request):
    return render(request, 'home.html')
