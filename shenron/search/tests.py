from django.test import TestCase
from MoviePage.models import Movie
from django.urls import reverse
# Create your tests here.
class SearchViewsTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(id=1,
                                          title='Test Movie',
                                          vote_average=5.0,
                                          vote_count=1000,
                                          status='Released',
                                          release_date='2021-01-01',
                                          revenue=1000000,
                                          runtime=120,
                                          adult=False,
                                          backdrop_path='backdrop.jpg',
                                          budget=1000000,
                                          original_language='en',
                                          overview='This is a test movie.',
                                          poster_path='poster.jpg',
                                          tagline='Test tagline',
                                          genres='Action',
                                          keywords='Test keyword')
        self.movie.save()

    def test_search_view(self):
        response = self.client.get(reverse('search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')

        response = self.client.post(reverse('search'), {'q': 'Test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        self.assertContains(response, 'Test Movie')
        self.assertEqual(response.context['results'].count(), 1)

        response = self.client.post(reverse('search'), {'q': 'random'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'search.html')
        self.assertEqual(response.context['results'].count(), 0)
