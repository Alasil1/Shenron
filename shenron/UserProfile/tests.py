from django.test import TestCase
from user.models import User
from django.urls import reverse
# Create your tests here.
class UserProfileViewsTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='1234', email='test@gmail.com')
        self.client.login(username='test_user', password='1234')


    def test_user_profile_view_unauthenticated(self):
        self.client.logout()
        response = self.client.get(reverse('profile'))
        self.assertEqual(response.status_code, 302)
