
from django.contrib.auth.decorators import login_required
from .models import Favourites
from MoviePage.models import Movie

# @login_required  
def favourite_list(request):
    favourite_list = Favourites.objects.filter(user=request.user).first()  # Get the user's favourite list
    movies = favourite_list.movies.all() if favourite_list else []  # Fetch all movies if the list exists

    return render(request, 'favourite.html', {
        'favourite_list': favourite_list,
        'movies': movies
    })


# @login_required
# def add_to_favourites(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id) 
#     Favourite.objects.get_or_create(user=request.user, movie=movie)
#     return JsonResponse({'success': True, 'message': f'Added {movie.title} to favourites'})

# @login_required
# def remove_from_favourites(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id)
#     Favourite.objects.filter(user=request.user, movie=movie).delete()
#     return JsonResponse({'success': True, 'message': f'Removed {movie.title} from favourites'})


