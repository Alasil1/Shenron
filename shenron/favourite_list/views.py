from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404 ,redirect
from .models import User, Movie,Favourites

@login_required(login_url='login')
def add_to_favorites(request, movie_id):
    user = request.user
    movie = get_object_or_404(Movie, id=movie_id)
    favourites, created = Favourites.objects.get_or_create(user=user)
    favourites.movies.add(movie)
    return render(request, 'movie.html', {'movie': movie})


@login_required(login_url='login')
def remove_from_favorites(request, user_id, movie_id):
    favourites = Favourites.objects.get(user_id=user_id) 
    movie = Movie.objects.get(id=movie_id)
    favourites.movies.remove(movie)

    return redirect('/favourites')  


@login_required(login_url='login')
def get_favorites(request):
    user = request.user
    favorite_movies = user.favourites.movies.all() if hasattr(user, 'favourites') else []

    return render(request, 'favourite.html', {'movies': favorite_movies, 'user': user})