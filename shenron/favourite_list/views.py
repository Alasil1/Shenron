from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.decorators import api_view

from .models import User, Movie, Favourites

@login_required(login_url='login')
def add_to_favorites(request, movie_id):
    """
    Add a movie to the user's favorites.

    :param request: The HTTP request object.
    :param movie_id: The ID of the movie to add to favorites.
    :return: Rendered HTML page with the movie details and its trailers.
    """
    user = request.user
    movie = get_object_or_404(Movie, id=movie_id)
    favourites, created = Favourites.objects.get_or_create(user=user)
    favourites.movies.add(movie)
    trailers, images = movie.get_videos()
    trailer_image_pairs = zip(trailers, images)
    return render(request, 'movie.html', {'movie': movie, 'trailers': trailer_image_pairs})

@login_required(login_url='login')
def remove_from_favorites(request, movie_id):
    """
    Remove a movie from the user's favorites.

    :param request: The HTTP request object.
    :param user_id: The ID of the user.
    :param movie_id: The ID of the movie to remove from favorites.
    :return: Redirect to the favorites page.
    """
    user_id=request.user.id
    favourites = Favourites.objects.get(user_id=user_id)
    movie = Movie.objects.get(id=movie_id)
    favourites.movies.remove(movie)
    return redirect('/favourites')

@login_required(login_url='login')
def get_favorites(request):
    """
    Retrieve the user's favorite movies.

    :param request: The HTTP request object.
    :return: Rendered HTML page with the list of favorite movies.
    """
    user = request.user
    favorite_movies = user.favourites.movies.all() if hasattr(user, 'favourites') else []
    return render(request, 'favourite.html', {'movies': favorite_movies, 'user': user})
