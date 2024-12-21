from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six
from tokens.models import UsedToken
class AccountActivationTokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp)  + six.text_type(user.is_active)
        )
    def mark_token_used(self, user, token):
        UsedToken.objects.create(user=user, token=token)


account_activation_token = AccountActivationTokenGenerator()