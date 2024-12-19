from django.shortcuts import render
from MoviePage.models import Movie
from django.db.models import Case, When, Value, IntegerField
from rest_framework.decorators import api_view

def search(request):
    """
    Handle the search functionality for movies.

    This view processes POST requests containing a search query, filters movies
    based on the query, and returns the search results.

    :param request: The HTTP request object.
    :return: Rendered HTML page with search results or an empty search page.
    """
    if request.method == 'POST':
        query = request.POST.get('q')
        if query:
            results = Movie.objects.filter(title__icontains=query, vote_count__gt=100).annotate(
                exact_match=Case(
                    When(title__iexact=query, then=Value(1)),
                    default=Value(0),
                    output_field=IntegerField(),
                )
            ).order_by('-exact_match', '-vote_average')

            return render(request, 'search.html', {'results': results})
    return render(request, 'search.html')
