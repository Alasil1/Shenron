# login/views.py
from django.shortcuts import render,redirect
from .models import User
from django.http import HttpResponse
from django.contrib.auth import login as auth_login, logout


def create_user_view(request):
    if request.user.is_authenticated:
        return redirect('/shenron')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        if User.objects.filter(username=username).exists():
            return render(request, 'create_user.html',
                          {'error': 'Username is already taken. Please choose another one.'})
        if User.objects.filter(email=email).exists():
            return render(request, 'create_user.html',
                          {'error': 'Email is already taken. Please use a different email.'})
        user=User.CreateUser(username, password, email)
        print(user)
        auth_login(request,user)
        return redirect('/shenron')
    return render(request, 'create_user.html')
def login(request):
    if request.user.is_authenticated:
        return redirect('/shenron') 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.Login(request,username, password)
        if user:
            auth_login(request, user)
            next_url = request.POST.get('next')
            return redirect(next_url)
        else:
            return render(request, 'login.html',
                          {'error': 'Username or password is wrong, please try again.'})
    next_url = request.GET.get('next', '/shenron/')
    return render(request, 'login.html', {'next': next_url})
def logout_view(request):
    logout(request)
    return redirect('login')
