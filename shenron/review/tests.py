from django.test import TestCase
from .models import Reviews
from MoviePage.models import Movie
from user.models import User
from django.urls import reverse
# Create your tests here.
class ReviewsmodelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='1234', email='test@email.com')
        self.user.save()
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
        self.review = Reviews.objects.create(user=self.user,
                                             movie=self.movie,
                                             plot=1,
                                             acting=2,
                                             cinematography=3,
                                             music=4,
                                             character_development=5,
                                             pacing=5,
                                             overall='This is a great movie.')
        self.review.save()

    def test_review_user(self):
        self.assertEqual(self.review.user, self.user)

    def test_review_movie(self):
        self.assertEqual(self.review.movie, self.movie)

    def test_review_plot(self):
        self.assertEqual(self.review.plot, 1)

    def test_review_acting(self):
        self.assertEqual(self.review.acting, 2)

    def test_review_cinematography(self):
        self.assertEqual(self.review.cinematography, 3)

    def test_review_music(self):
        self.assertEqual(self.review.music, 4)

    def test_review_character_development(self):
        self.assertEqual(self.review.character_development, 5)

    def test_review_pacing(self):
        self.assertEqual(self.review.pacing, 5)

    def test_review_overall(self):
        self.assertEqual(self.review.overall, 'This is a great movie.')

class ReviewViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='1234', email='test@gmail.com')
        self.user.save()
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

    def test_user_reviews(self):
        self.client.login(username='test_user', password='1234')
        response = self.client.get(reverse('user_reviews'))
        self.assertNotEqual(response.status_code, 200)

    def test_user_reviews_no_login(self):
        response = self.client.get(reverse('user_reviews'))
        self.assertEqual(response.status_code, 302)

    def test_create_review(self):
        self.client.login(username='test_user', password='1234')
        response = self.client.get(reverse('create_review', args=[self.movie.id]))
        self.assertNotEqual(response.status_code, 200)
        response = self.client.post(reverse('create_review', args=[self.movie.id]), {'plot': 1, 'acting': 2, 'cinematography': 3, 'music': 4, 'character_development': 5, 'pacing': 5, 'overall': 'This is a great movie.'})
        self.assertNotEqual(response.status_code, 200)

    def test_create_review_no_login(self):
        response = self.client.get(reverse('create_review', args=[self.movie.id]))
        self.assertEqual(response.status_code, 302)

    def test_remove_review(self):
        self.client.login(username='test_user', password='1234')
        movie = Movie.objects.create(id=2,
                                     title='Test Movie 2',
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
        movie.save()
        review = Reviews.objects.create(user=self.user,
                                        movie=movie,
                                        plot=1,
                                        acting=2,
                                        cinematography=3,
                                        music=4,
                                        character_development=5,
                                        pacing=5,
                                        overall='This is a great movie.')
        review.save()
        response = self.client.get(reverse('remove_review', args=[movie.id]))
        self.assertNotEqual(response.status_code, 200)
        self.assertRedirects(response, redirect('user_reviews'))

    def test_remove_review_no_login(self):
        response = self.client.get(reverse('remove_review', args=[self.movie.id]))
        self.assertEqual(response.status_code, 302)

    def test_movie_reviews(self):
        response = self.client.get(reverse('movie_reviews', args=[self.movie.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'movie_reviews.html')
