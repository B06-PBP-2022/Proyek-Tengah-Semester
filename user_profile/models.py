from django.utils import timezone
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class LastEdited(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    password_edited = models.BooleanField(default=False)
    last_password_edited = models.DateField(default=timezone.now)

    def save(self):
        self.password_edited = True
        self.last_password_edited = timezone.now()