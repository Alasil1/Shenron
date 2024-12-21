from . import views
from django.urls import path

urlpatterns = [
    path('', views.userProfile, name='profile'),
    path('reset/', views.reset_password, name='reset_password'),
]