from django.core.checks import messages
from django.shortcuts import redirect
from tokens.models import UsedToken
from .models import User
from django.contrib.auth import login as auth_login, logout, get_user_model
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib import messages
from tokens.tokens import account_activation_token


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
        user = User.CreateUser(username, password, email)
        user.backend = 'django.contrib.auth.backends.ModelBackend'
        auth_login(request, user)
        activateEmail(request, user, email)
        return redirect('/shenron')
    return render(request, 'create_user.html')

def login(request):
    if request.user.is_authenticated:
        return redirect('/shenron') 
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = User.Login(request, username, password)
        if user:
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            auth_login(request, user)
            next_url = request.POST.get('next')
            if not next_url:
                next_url = '/shenron/'
            return redirect(next_url)
        else:
            return render(request, 'login.html',
                          {'error': 'Username or password is wrong, please try again.'})
    next_url = request.GET.get('next', '/shenron/')
    return render(request, 'login.html', {'next': next_url})

def logout_view(request):
    logout(request)
    return redirect('login')

def activateEmail(request, user, to_email):
    mail_subject = 'Activate your user account.'
    message = render_to_string('template_activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user}, please go to you email {to_email} inbox and click on \
            received activation link to confirm and complete the registration.')
    else:
        messages.error(request, f'Problem sending confirmation email to {to_email}, check if you typed it correctly.')


def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        if UsedToken.objects.filter(user=user, token=token).exists():
            messages.error(request, 'This activation link has already been used.')
            return redirect('login')
        account_activation_token.mark_token_used(user, token)
        user.activated = True
        user.save()

        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('/shenron')
    else:
        messages.error(request, 'Activation link is invalid!')
    return redirect('/shenron')

from django.shortcuts import render

def activate_account(request):
    return render(request, 'activate.html')

def request_forget_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        user=User.objects.filter(email=email).first()
        if User.objects.filter(email=email).exists():
            mail_subject = 'Reset your password'
            message = render_to_string('forget_password_mail.html', {
                'user': user.username,
                'domain': get_current_site(request).domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
                'protocol': 'https' if request.is_secure() else 'http'
            })
            email = EmailMessage(mail_subject, message, to=[email])
            if email.send():
                messages.success(request, f'Dear {user}, Open the link to reset your password')
            else:
                messages.error(request,
                               f'Problem sending confirmation email to {email}, check if you typed it correctly.')
        else:
            return render(request, 'request_forget_password.html',
                          {'error': 'Email doesnot exist'})
    return render(request, 'request_forget_password.html')

def forget_password(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        if UsedToken.objects.filter(user=user, token=token).exists():
            messages.error(request, 'This password reset link has already been used.')
            return redirect('login')
        if request.method == 'POST':
            account_activation_token.mark_token_used(user, token)
            new_password1 = request.POST.get('new_password1')
            user.set_password(new_password1)
            user.save()
            messages.success(request,
                             'Your password has been reset successfully. You can now log in with the new password.')
            return redirect('login')
        return render(request, 'forget_password.html')
    else:
        messages.error(request, 'Password reset link is invalid!')
        return redirect('login')