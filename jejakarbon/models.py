from email.policy import default
from django.db import models
from django.conf import settings
import datetime

class User(models.Model):
    # nitip field user sm totalCarbon yah -neysa
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    total_carbon = models.PositiveIntegerField(default=0)

class DataCarbon(models.Model):
    jenis_pemakaian = models.CharField(max_length=10)
    jumlah_kwh = models.FloatField(default=0)
    jumlah_km = models.FloatField(default=0)
    jumlah_bensin_liter = models.IntegerField(default=0)
    jenis_bbm = models.CharField(max_length=6)
    date_input = models.DateField(default=datetime.date.today())