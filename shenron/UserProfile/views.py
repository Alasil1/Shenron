from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404 ,redirect
from .models import User

# Create your views here.
@login_required(login_url='login')
def userProfile(request):
    username = request.user.username
    email = request.user.email
    datejoined = request.user.date_joined
    return render(request, 'userProfile.html', {'username': username, 'email': email, 'datejoined': datejoined})
