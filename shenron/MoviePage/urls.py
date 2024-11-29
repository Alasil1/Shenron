from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('movies/', views.all_movies, name='movies'),
    path('movies/<int:movie_id>/', views.movie, name='details'),
]
