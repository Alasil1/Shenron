from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Movie

def movie(request, movie_id):
    movie = Movie.objects.get(pk=movie_id)
    # movies=movies['id'][:10
    return render(request, 'movie.html', {'movie': movie})

def all_movies(request):
    movies = Movie.objects.filter(vote_count__gt=1000).order_by('-vote_average')[0:20]
    return render(request, 'all_movies.html', {'movies': movies})

def home(request):
    return render(request, 'home.html')
