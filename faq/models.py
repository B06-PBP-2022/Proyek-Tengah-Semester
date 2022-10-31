from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Faq(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    question = models.CharField(max_length=250,blank=False)
    answer = models.TextField(blank=True)
    username = models.CharField(blank=True, max_length=250)
