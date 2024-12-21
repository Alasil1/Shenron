import hashlib

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404 ,redirect
from .models import User


def emailHashing(email):
    email_split = email.split('@')

    email_split[0] = email_split[0].replace(email_split[0][1:-1], '#')
    email = '@'.join(email_split)
    return email

# Create your views here.
@login_required(login_url='login')
def userProfile(request):
    if not request.user.activated:
        return redirect('activate_account')
    username = request.user.username
    email = request.user.email
    email = emailHashing(email)
    datejoined = request.user.date_joined
    return render(request, 'userProfile.html', {'username': username, 'email': email, 'datejoined': datejoined})


