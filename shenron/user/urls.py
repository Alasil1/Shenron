from django.urls import path
from .views import create_user_view,login,logout_view,activate,activate_account,request_forget_password,forget_password

urlpatterns = [
    path("", create_user_view,name='signup'),
    path('activate/', activate_account, name='activate_account'),
    path("login/",login,name='login'),
    path('request_forget_password/', request_forget_password, name='request_forget_password'),

    path('activate/<uidb64>/<token>', activate, name='activate'),
    path('forget_password/<uidb64>/<token>',forget_password , name='forget_password'),
    path('logout/',logout_view, name='logout'),

    ]