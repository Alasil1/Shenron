
# urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('', views.forum, name='forum'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('post/create_post/', views.create_post, name='create_post'),
    path('topic/create_topic/', views.create_topic, name='create_topic'),
    # path('forum/<int:post_id>/create_comment/', views.create_comment, name='create_comment'),
    path('comment/create_comment', views.create_comment, name='create_comment'),
]