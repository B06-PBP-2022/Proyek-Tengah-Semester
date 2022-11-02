from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class ikutdonasi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE),
    nominal = models.CharField(max_length=200),
    pesan = models.CharField(max_length=200),
    
    def __str__(self):
        return self.nominal

