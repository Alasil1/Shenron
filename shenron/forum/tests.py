# from Tools.scripts.make_ctype import method
from django.test import TestCase
from .models import Post, Comment, Topic
from django.urls import reverse
from user.models import User
from MoviePage.models import Movie
# Create your tests here.

class TopicModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='1234', email='test@gmail.com')
        self.user.save()
        self.client.login(username='test_user', password='1234')
        self.topic = Topic.objects.create(name='Test Topic', createdby_id=self.user.id)
        self.topic.save()
        self.client.login(username='test_user', password='1234')
        self.topic.__str__()

    def test_topic_name(self):
        self.assertEqual(self.topic.name, 'Test Topic')

    def test_topic_createdby(self):
        self.assertEqual(self.topic.createdby_id, self.user.id)

class PostModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='1234', email='test@gmail.com')
        self.user.save()
        self.client.login(username='test_user', password='1234')
        self.topic = Topic.objects.create(name='Test Topic', createdby_id=self.user.id)
        self.topic.save()
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author_id=self.user.id, topic_id=self.topic.id)
        self.post.save()

    def test_post_title(self):
        self.assertEqual(self.post.title, 'Test Post')

    def test_post_content(self):
        self.assertEqual(self.post.content, 'This is a test post.')

    def test_post_author(self):
        self.assertEqual(self.post.author_id, self.user.id)

    def test_post_topic(self):
        self.assertEqual(self.post.topic_id, self.topic.id)

class CommentModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='1234', email='test@gmail.com')
        self.user.save()
        self.client.login(username='test_user', password='1234')
        self.topic = Topic.objects.create(name='Test Topic', createdby_id=self.user.id)
        self.topic.save()
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author_id=self.user.id, topic_id=self.topic.id)
        self.post.save()
        self.comment = Comment.objects.create(post_id=self.post.id, content='This is a test comment.', author_id=self.user.id)
        self.comment.save()


    def test_comment_author(self):
        self.assertEqual(self.comment.author_id, self.user.id)

class ForumViewsTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='test_user', password='1234', email='test@gmail.com')
        self.user.save()
        self.topic = Topic.objects.create(name='Test Topic', createdby_id=self.user.id)
        self.topic.save()
        self.post = Post.objects.create(title='Test Post', content='This is a test post.', author_id=self.user.id, topic_id=self.topic.id)
        self.post.save()

    def test_topic_detail(self):
        self.client.login(username='test_user', password='1234')
        self.user.activated = True
        response = self.client.get(reverse('topic_detail', args=[self.topic.id]))
        self.assertNotEqual(response.status_code, 200)

    def test_topic_detail_no_login(self):
        response = self.client.get(reverse('topic_detail', args=[self.topic.id]))
        self.assertEqual(response.status_code, 302)


    def test_post_detail(self):
        self.client.login(username='test_user', password='1234')
        self.user.activated = True
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertNotEqual(response.status_code, 200)

    def test_post_detail_no_login(self):
        response = self.client.get(reverse('post_detail', args=[self.post.id]))
        self.assertEqual(response.status_code, 302)


