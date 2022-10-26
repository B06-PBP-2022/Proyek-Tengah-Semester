from django.db import models

class LastEdited(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    last_username_edited = models.DateField()
    last_password_edited = models.DateField()