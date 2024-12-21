from allauth.account.signals import user_signed_up
from django.dispatch import receiver
from allauth.socialaccount.models import SocialAccount

@receiver(user_signed_up)
def user_signed_up_request(request, user, **kwargs):
    social_login = SocialAccount.objects.filter(user=user)
    if social_login or user.is_staff or user.is_superuser:
        user.activated = True
        user.save()
