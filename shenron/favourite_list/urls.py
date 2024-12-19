# favourite_list/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_favorites, name='favourite_list'),
    path('add/<int:movie_id>/', views.add_to_favorites, name='add_to_favorites'),
    path('remove/<int:movie_id>/', views.remove_from_favorites, name='remove_from_favorites'),
]
