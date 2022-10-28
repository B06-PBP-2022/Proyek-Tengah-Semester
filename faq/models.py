from django.db import models

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=250,blank=True)
    answer = models.TextField(blank=True)
