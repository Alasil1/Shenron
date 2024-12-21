from django.test import TestCase
from django.urls import reverse

from .models import Movie
from user.models import User
# Create your tests here.

class MovieModelTest(TestCase):
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

    def test_movie_title(self):
        self.assertEqual(self.movie.title, 'Test Movie')

    def test_movie_vote_average(self):
        self.assertEqual(self.movie.vote_average, 5.0)

    def test_movie_vote_count(self):
        self.assertEqual(self.movie.vote_count, 1000)

    def test_movie_status(self):
        self.assertEqual(self.movie.status, 'Released')

    def test_movie_release_date(self):
        self.assertEqual(self.movie.release_date, '2021-01-01')

    def test_movie_revenue(self):
        self.assertEqual(self.movie.revenue, 1000000)

    def test_movie_runtime(self):
        self.assertEqual(self.movie.runtime, 120)

    def test_movie_adult(self):
        self.assertEqual(self.movie.adult, False)

    def test_movie_backdrop_path(self):
        self.assertEqual(self.movie.backdrop_path, 'backdrop.jpg')

    def test_movie_budget(self):
        self.assertEqual(self.movie.budget, 1000000)

    def test_movie_original_language(self):
        self.assertEqual(self.movie.original_language, 'en')

    def test_movie_overview(self):
        self.assertEqual(self.movie.overview, 'This is a test movie.')

    def test_movie_poster_path(self):
        self.assertEqual(self.movie.poster_path, 'poster.jpg')

    def test_movie_tagline(self):
        self.assertEqual(self.movie.tagline, 'Test tagline')

    def test_movie_genres(self):
        self.assertEqual(self.movie.genres, 'Action')

    def test_movie_keywords(self):
        self.assertEqual(self.movie.keywords, 'Test keyword')

    def test_movie_str(self):
        self.assertEqual(self.movie.__str__(), 'Test Movie')

class MovieViewsTests(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(id=1,
                                          title='Test Movie',
                                          vote_average=5.0,
                                          vote_count=1001,
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

    def test_movie_detail_view(self):
        response = self.client.get(reverse('details', args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)

    def test_all_movies_view(self):
        for i in range(19):
            movie = Movie.objects.create(id=i+2,
                                          title=f'Test Movie {i+2}',
                                          vote_average=5.0,
                                          vote_count=1001,
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
            movie.save()
        response = self.client.get(reverse('movies'))
        self.assertEqual(response.status_code, 200)

    def test_home_view(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

