from django.shortcuts import render, redirect
from .models import User
from django.contrib.auth import login as auth_login, logout
from rest_framework.decorators import api_view

def create_user_view(request):
    """
    Handle the creation of a new user.

    This view processes POST requests to create a new user, checks for existing
    usernames and emails, and logs in the user upon successful creation.

    :param request: The HTTP request object.
    :return: Redirect to the 'shenron' page or render the user creation page with errors.
    """
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
        user = User.CreateUser(username, password, email)
        print(user)
        auth_login(request, user)
        return redirect('/shenron')
    return render(request, 'create_user.html')

def login(request):
    """
    Handle user login.

    This view processes POST requests to log in a user, checks the username and
    password, and redirects to the next URL upon successful login.

    :param request: The HTTP request object.
    :return: Redirect to the 'shenron' page or render the login page with errors.
    """
    if request.user.is_authenticated:
        return redirect('/shenron')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.Login(request, username, password)
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
    """
    Handle user logout.

    This view logs out the user and redirects to the login page.

    :param request: The HTTP request object.
    :return: Redirect to the login page.
    """
    logout(request)
    return redirect('login')
