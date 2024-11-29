from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Movie
import requests
# from PIL import Image
# from io import BytesIO
# from colorthief import ColorThief
def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    # poster_path = movie.poster_path
    # url = f"https://image.tmdb.org/t/p/original{poster_path}"
    # response = requests.get(url)
    # print(poster_path)
    # print(response)
    # img = BytesIO(response.content)
    # color_thief = ColorThief(img)
    # dominant_color = color_thief.get_color(quality=1)
    # print(dominant_color)
    # dominant_color_hex = '#{:02x}{:02x}{:02x}'.format(*dominant_color)
    # return render(request, 'movie.html', {'movie': movie, 'dominant_color': dominant_color_hex})

    return render(request, 'movie.html', {'movie': movie})

def all_movies(request):
    movies = Movie.objects.filter(vote_count__gt=1000).order_by('-vote_average')[0:20]
    return render(request, 'all_movies.html', {'movies': movies})

def home(request):
    return render(request, 'home.html')
