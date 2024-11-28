
# urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('', views.forum, name='forum'),
    path('forum/topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('forum/<int:post_id>/', views.post_detail, name='post_detail'),
    path('forum/create_post/', views.create_post, name='create_post'),
    path('forum/<int:post_id>/create_comment/', views.create_comment, name='create_comment'),
]