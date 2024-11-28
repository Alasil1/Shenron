from django.shortcuts import render, get_object_or_404
from .models import User, Movie,Favourites


# def add_to_favorites(request, user_id, movie_id):
#     user = get_object_or_404(User, id=user_id)
#     movie = get_object_or_404(Movie, id=movie_id)
#     user.favourites.movies.add(movie)
#     favorite_movies = user.favourites.movies.all()  # Fetch updated favorites
#     return render(request, 'favourites.html', {'movies': favorite_movies, 'user': user})

from django.shortcuts import redirect
from .models import User, Movie

def remove_from_favorites(request, user_id, movie_id):
    try:
        favourites = Favourites.objects.get(user_id=user_id) 
        movie = Movie.objects.get(id=movie_id)

        favourites.movies.remove(movie)
    except User.DoesNotExist:
        return redirect('error_page')  
    except Movie.DoesNotExist:
        return redirect('error_page')  

    return redirect('/favourites')  

def get_favorites(request):
    user = get_object_or_404(User, id=request.user.id)
    favorite_movies = user.favourites.movies.all()
    return render(request, 'favourite.html', {'movies': favorite_movies, 'user': user})
