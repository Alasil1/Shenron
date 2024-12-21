from django.urls import path
from . import views
from forum.views import post_detail
urlpatterns = [
    path('notifications/', views.notificationview, name='notifications_view'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
]
