from . import views
from django.urls import path

urlpatterns = [
    path('', views.all_movies, name='movie'),
    path('<int:movie_id>/', views.movie, name='movie'),
]
