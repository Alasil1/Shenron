from django.urls import path
from .views import create_user_view,login,logout_view
from django.urls import include
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("", create_user_view,name='signup'),

    path("login/",login,name='login'),

    path('logout/',logout_view, name='logout'),
    # oter paths
    ]