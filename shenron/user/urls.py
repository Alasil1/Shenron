from django.urls import path
from .views import create_user_view,login

urlpatterns = [
    path("", create_user_view),
    path("login/",login,name='login'),
    ]