from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount

@receiver(user_signed_up)
def user_signed_up_request(request, user, **kwargs):
    social_login = SocialAccount.objects.filter(user=user)
    if social_login:
        user.activated = True
        user.save()
