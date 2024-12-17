from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate, login

class User(AbstractUser):
    """
    Custom user model extending the default Django AbstractUser.

    Methods:
        CreateUser(username, password, email): Creates a new user with the given username, password, and email.
        Login(request, username, password): Authenticates a user with the given username and password.
    """

    @classmethod
    def CreateUser(cls, username, password, email):
        """
        Create a new user with the given username, password, and email.

        :param username: The username for the new user.
        :param password: The password for the new user.
        :param email: The email for the new user.
        :return: The created user instance.
        """
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        return user

    @classmethod
    def Login(cls, request, username, password):
        """
        Authenticate a user with the given username and password.

        :param request: The HTTP request object.
        :param username: The username of the user.
        :param password: The password of the user.
        :return: The authenticated user instance if credentials are valid, otherwise False.
        """
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return user
        else:
            return False