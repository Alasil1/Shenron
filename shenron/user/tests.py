from django.test import TestCase
from .models import User
from django.urls import reverse
# Create your tests here.
class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='1234', email='test@gmail.com')
        self.user.save()

    def test_user_username(self):
        self.assertEqual(self.user.username, 'test_user')

    def test_user_email(self):
        self.assertEqual(self.user.email, 'test@gmail.com')

    def test_user_is_active(self):
        self.assertTrue(self.user.is_active)

    def test_user_is_staff(self):
        self.assertFalse(self.user.is_staff)

    def test_user_is_superuser(self):
        self.assertFalse(self.user.is_superuser)

    def test_user_str(self):
        self.assertEqual(str(self.user), 'test_user')

class UserViewTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='1234', email='test@gmail.com')
        self.user.save()

    def test_create_user_view(self):
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 200)
        self.client.logout()

        response = self.client.post(reverse('signup'), {'username': 'test_user2', 'password': '1234', 'email': 'test2@gmail.com'})
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username='test_user2').exists())

        self.client.logout()
        response = self.client.post(reverse('signup'), {'username': self.user.username, 'password': '1234', 'email': 'random@gmail.com'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Username is already taken. Please choose another one.')

        self.client.logout()
        response = self.client.post(reverse('signup'), {'username': 'random', 'password': '1234', 'email': self.user.email})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Email is already taken. Please use a different email.')

        self.client.login(username='test_user', password='1234')
        response = self.client.get(reverse('signup'))
        self.assertEqual(response.status_code, 302)

    # def test_login_view(self):
    #     self.client.logout()
    #     response = self.client.get(reverse('login'))
    #     self.assertEqual(response.status_code, 200)

    #     self.client.logout()
    #     response = self.client.post(reverse('login'), {'username': self.user.username, 'password': self.user.password})
    #     self.assertEqual(response.status_code, 200)

    #     self.client.logout()
    #     response = self.client.post(reverse('login'), {'username': 'test_user', 'password': '12345'})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Username or password is wrong, please try again.')

    #     self.client.logout()
    #     response = self.client.post(reverse('login'), {'username': 'test_user____', 'password': '1234'})
    #     self.assertEqual(response.status_code, 200)
    #     self.assertContains(response, 'Username or password is wrong, please try again.')

    #     self.client.login(username='test_user', password='1234')
    #     response = self.client.get(reverse('login'))
    #     self.assertEqual(response.status_code, 302)

    def test_logout_view(self):
        self.client.login(username='test_user', password='1234')
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.client.session.get('_auth_user_id'))

        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)

        self.client.logout()
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(self.client.session.get('_auth_user_id'))
