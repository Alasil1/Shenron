# favourite_list/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_favorites, name='favourite_list'),
    # path('/add/<int:movie_id>/', views.add_to_favourites, name='add_to_favourites'),
    path('remove/<int:user_id>/<int:movie_id>/', views.remove_from_favorites, name='remove_from_favorites'),

]
