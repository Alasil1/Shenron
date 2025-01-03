
# urls.py
from django.urls import path
from . import views



urlpatterns = [
    path('', views.forum, name='forum'),
    path('topic/<int:topic_id>/', views.topic_detail, name='topic_detail'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
]