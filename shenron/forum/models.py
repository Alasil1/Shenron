from django.db import models
from django.conf import settings

class Topic(models.Model):
    """
    Model representing a forum topic.

    Attributes:
        name (str): The name of the topic.
        createdby (User): The user who created the topic.
    """
    name = models.CharField(max_length=255)
    createdby = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        """
        Return a string representation of the topic.

        :return: The name of the topic.
        """
        return self.name

class Post(models.Model):
    """
    Model representing a post in a forum topic.

    Attributes:
        title (str): The title of the post.
        content (str): The content of the post.
        author (User): The user who authored the post.
        topic (Topic): The topic to which the post belongs.
        created_at (datetime): The date and time when the post was created.
    """
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, related_name='posts', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a string representation of the post.

        :return: The title of the post.
        """
        return self.title

class Comment(models.Model):
    """
    Model representing a comment on a post.

    Attributes:
        post (Post): The post to which the comment belongs.
        content (str): The content of the comment.
        author (User): The user who authored the comment.
        created_at (datetime): The date and time when the comment was created.
    """
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    content = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        Return a string representation of the comment.

        :return: A string indicating the author and the post.
        """
        return f'Comment by {self.author} on {self.post}'