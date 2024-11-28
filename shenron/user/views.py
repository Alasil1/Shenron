# login/views.py
from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, authenticate
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
            auth_login(request, user)
            next_url = request.POST.get('next', '/movies')
            return redirect(next_url)
        else:
            return HttpResponse("failure")
    next_url = request.GET.get('next', '/movies/')
    return render(request, 'login.html', {'next': next_url})