# login/views.py
from django.shortcuts import render
from .models import User
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required

# @login_required(login_url='/login')
def create_user_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        # phone = request.POST['phone']
        User.CreateUser(username, password, email)
        return HttpResponse("success")
    return render(request, 'create_user.html')
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.Login(request,username, password)
        if user:
            return HttpResponse("success")
        else:
            return HttpResponse("failure")
    return render(request, 'login.html')