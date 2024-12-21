from django.db import models
from django.conf import settings

class UsedToken(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    token = models.CharField(max_length=1024)
    used_at = models.DateTimeField(auto_now_add=True)