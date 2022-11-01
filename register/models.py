from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='userprofile', on_delete=models.CASCADE)
    name = models.CharField(max_length=200, blank=True)
    contact = models.CharField(max_length=100)
    organization = models.BooleanField()

    def __str__(self):
        return self.user.username
