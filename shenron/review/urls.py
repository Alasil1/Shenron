from django.urls import path
from . import views

urlpatterns = [
    path('', views.user_reviews, name='user_reviews'),
    path('create/<int:movie_id>/', views.create_review, name='create_review'),
    path('remove/<int:movie_id>/', views.remove_review, name='remove_review'),
    path('movie/<int:movie_id>/', views.movie_reviews, name='movie_reviews'),
]
