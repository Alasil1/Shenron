from django.urls import path
from .views import create_user_view,login

urlpatterns = [
    path("", create_user_view,name='signup'),
    path("login/",login,name='login'),
    ]