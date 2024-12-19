from django.contrib.auth.decorators import login_required
from.models import Reviews
from MoviePage.models import Movie
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
@login_required(login_url='login')
def user_reviews(request):
    """
    Display the user's reviews.

    :param request: The HTTP request object.
    :return: Rendered HTML page with the user's reviews.
    """
    return render(request, 'user_reviews.html', {'user': request.user, 'reviews': request.user.reviews.all()})

@login_required(login_url='login')
def create_review(request, movie_id):
    if Reviews.objects.filter(user=request.user, movie=Movie.objects.get(id=movie_id)).exists():
        return render(request, 'user_reviews.html', {'user': request.user, 'reviews': request.user.reviews.all()})
    if request.method == 'POST':
        plot = request.POST.get('plot')
        acting = request.POST.get('acting')
        cinematography = request.POST.get('cinematography')
        music = request.POST.get('music')
        character_development = request.POST.get('character_development')
        pacing = request.POST.get('pacing')
        overall = request.POST.get('overall')
        review = Reviews.objects.create(user=request.user, movie=Movie.objects.get(id=movie_id), plot=plot, acting=acting, cinematography=cinematography, music=music, character_development=character_development, pacing=pacing, overall=overall)
        return render(request, 'user_reviews.html', {'user': request.user, 'reviews': request.user.reviews.all()})
    else:
        return render(request, 'create_review.html', {'movie': Movie.objects.get(id=movie_id)})

@login_required(login_url='login')
def remove_review(request, movie_id):
    review = Reviews.objects.get(user=request.user, movie=Movie.objects.get(id=movie_id))
    review.delete()
    return redirect('user_reviews')

def movie_reviews(request, movie_id):
    return render(request, 'movie_reviews.html', {'movie': Movie.objects.get(id=movie_id), 'reviews': Reviews.objects.filter(movie=Movie.objects.get(id=movie_id))})
