from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User

class ikutdonasi(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nominal = models.IntegerField()
    pesan = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nominal

