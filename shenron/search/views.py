from django.shortcuts import render
from MoviePage.models import Movie
from django.views.decorators.csrf import csrf_protect

from django.db.models import Case, When, Value, IntegerField


def search(request):
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



