from django.test import TestCase
from django.urls import reverse
from .models import User, Favourites
from MoviePage.models import Movie
# Create your tests here.
class FavouritesModelTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='1234', email='test@gmail.com')
        self.user.save()
        self.movie = Movie(id=1,
                            title='Test Movie',
                            vote_average=8.5,
                            vote_count=1000,
                            status='Released',
                            release_date='2021-01-01',
                            revenue=1000000,
                            runtime=120,
                            adult=False,
                            backdrop_path='/path/to/backdrop.jpg',
                            budget=500000,
                            original_language='en',
                            overview='This is a test movie overview.',
                            poster_path='/path/to/poster.jpg',
                            tagline='This is a test tagline.',
                            genres='Action, Adventure',
                            keywords='test, movie'
                        )
        self.movie.save()
        self.favourites = Favourites.objects.create(user=self.user)
        self.favourites.save()

    def test_add_movie_to_favourites(self):
        self.favourites.movies.add(self.movie)
        self.assertIn(self.movie, self.favourites.movies.all())

    def test_remove_movie_from_favourites(self):
        self.favourites.movies.add(self.movie)
        self.favourites.movies.remove(self.movie)
        self.assertNotIn(self.movie, self.favourites.movies.all())

    def test_favourites_str(self):
        self.assertEqual(str(self.favourites), "test_user's Favourite List")

'''
In the add_to_favourites function, we rely on an external api to return the trailer and a related image for the movie.
Just place mock values inside the add_to_favourites function found in the views.py file instead of calling the movie.get_videos() method
 to be able to use this test case. Otherwise, the test case fails.
'''
class FavouriteViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='1234', email='test@gmail.com')
        self.movie = Movie.objects.create(id=1,
                            title='Test Movie',
                            vote_average=8.5,
                            vote_count=1000,
                            status='Released',
                            release_date='2021-01-01',
                            revenue=1000000,
                            runtime=120,
                            adult=False,
                            backdrop_path='/path/to/backdrop.jpg',
                            budget=500000,
                            original_language='en',
                            overview='This is a test movie overview.',
                            poster_path='/path/to/poster.jpg',
                            tagline='This is a test tagline.',
                            genres='Action, Adventure',
                            keywords='test, movie'
                        )
        self.favourites = Favourites.objects.create(user=self.user)

    def test_add_to_favorites(self):
        self.client.login(username='test_user', password='1234')
        response = self.client.get(reverse('add_to_favorites', args=[self.movie.id]))
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.movie, self.favourites.movies.all())

    def test_add_to_favorites_no_login(self):
        response = self.client.get(reverse('add_to_favorites', args=[self.movie.id]))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn(self.movie, self.favourites.movies.all())

    def test_remove_from_favorites(self):
        self.client.login(username='test_user', password='1234')
        self.favourites.movies.add(self.movie)
        response = self.client.get(reverse('remove_from_favorites', args=[self.movie.id]))
        self.assertNotEqual(response.status_code, 302)
        self.assertNotIn(self.movie, self.favourites.movies.all())

    def test_remove_from_favorites_no_login(self):
        self.favourites.movies.add(self.movie)
        response = self.client.get(reverse('remove_from_favorites', args=[self.movie.id]))
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.movie, self.favourites.movies.all())

    def test_get_favorites(self):
        self.client.login(username='test_user', password='1234')
        self.favourites.movies.add(self.movie)
        response = self.client.get(reverse('favourite_list'))
        self.assertNotEqual(response.status_code, )
        self.assertIn(self.movie, self.favourites.movies.all())

    def test_get_favorites_no_login(self):
        self.favourites.movies.add(self.movie)
        response = self.client.get(reverse('favourite_list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(self.movie, self.favourites.movies.all())
