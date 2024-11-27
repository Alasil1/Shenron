from django.urls import path
from . import views

urlpatterns = [
path('favourites/', views.favourite_list, name='favourites_list'),

]
