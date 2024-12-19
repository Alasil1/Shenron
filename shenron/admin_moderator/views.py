from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import permission_required
from django.contrib import messages 
from MoviePage.models import Movie
import random


@permission_required('MoviePage.add_movie', raise_exception=True)
def add_movie(request):
    if request.method == 'POST':
        movie_title = request.POST.get('movie_title')


        movie_data = Movie().get_movie_data_by_title(movie_title)
        # print(movie_data)
        if movie_data is None:
            messages.error(request, "Movie not found or invalid title.")
            return redirect('add_movie')

        if Movie.objects.filter(id=movie_data['id']).exists():
            messages.error(request, "This movie already exists in the database.")
            # print("it exists man ")
            return redirect('add_movie')

        movie = Movie(
            id=movie_data['id'],
            title=movie_data['title'],
            vote_average=movie_data.get('vote_average', 0),
            vote_count=movie_data.get('vote_count', 0),
            status=movie_data.get('status', ""),
            release_date=movie_data.get('release_date', ""),
            revenue=movie_data.get('revenue', 0),
            runtime=movie_data.get('runtime', 0),
            adult=movie_data.get('adult', " "),
            backdrop_path=movie_data.get('backdrop_path', ""),
            budget=movie_data.get('budget', 0),
            original_language=movie_data.get('original_language', ""),
            overview=movie_data.get('overview', ""),
            poster_path=movie_data.get('poster_path', ""),
            tagline=movie_data.get('tagline', " "),
            genres=movie_data.get('genres', " "),
            keywords=movie_data.get('keywords', " "),
        )
        movie.save()
        # messages.success(request, f"{movie.title} has been added successfully!")
        trailers,images=movie.get_videos()
        # print(images)
        trailer_image_pairs = zip(trailers, images)
        return render(request, 'movie.html', {'movie': movie, 'trailers':trailer_image_pairs })

    return render(request, 'add_movie.html')


@permission_required('MoviePage.delete_movie', raise_exception=True)
def remove_movie(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'POST':
        movie.delete()
        return redirect('MoviePage')
    return render(request, 'remove_movie.html', {'movie': movie})