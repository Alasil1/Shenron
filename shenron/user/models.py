from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import authenticate,login

class User(AbstractUser):
    @classmethod
    def CreateUser(cls,username,password,email):
        user=User.objects.create_user(username=username,password=password,email=email)
        user.save()
        return user
    @classmethod
    def Login(cls,request,username,password):
        user=authenticate(request,username=username,password=password)
        if user is not None:
            return user
        else:
            return False

