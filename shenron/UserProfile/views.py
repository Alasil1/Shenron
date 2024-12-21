import hashlib

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404 ,redirect
from django.contrib.auth.hashers import check_password
from django.contrib.auth import update_session_auth_hash
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


@login_required(login_url='login')
def reset_password(request):
    if request.method == 'POST':
        current_password = request.POST['old_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        if new_password != confirm_password:
            return render(request, 'ResetPassword.html', {'error': 'New password and Confirm are not the same, please try again.'})
        if check_password(current_password, request.user.password):
            if new_password == current_password:
                return render(request, 'ResetPassword.html',
                              {'error': 'New password and Old Password are the same, please try again.'})
            else:
                user = request.user
                user.set_password(new_password)
                user.save()
                update_session_auth_hash(request, user)
            return redirect('profile')
        else:
            return render(request, 'ResetPassword.html',{'error': 'Old Password is incorrect, please try again.'})



    return render(request, 'ResetPassword.html')
