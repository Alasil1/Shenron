from django.urls import path
from . import views

urlpatterns = [
    path('add_movie/', views.add_movie, name='add_movie'),
    # path('remove_movie/<int:movie_id>/', views.remove_movie, name='remove_movie'),
]
