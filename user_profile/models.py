from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class LastEdited(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    last_username_edited = models.DateField()
    last_password_edited = models.DateField()