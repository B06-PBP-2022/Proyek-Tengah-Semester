from django.db import models
from django.conf import settings
import datetime

# ambil usernya nanti dari modelsnya rania
class User(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) 

class DataCarbon(models.Model):
    total_carbon = models.PositiveIntegerField(default=0)

class CarbonListrik(models.Model):
    jenis_pemakaian = models.CharField(max_length=10)
    date_input = models.DateField(default=datetime.date.today())

class CarbonKendaraanDarat(models.Model):
    jenis_bbm = models.CharField(max_length=6)
    jumlah_kwh = models.FloatField(default=0)
    jumlah_km = models.FloatField(default=0)
    jumlah_bensin_liter = models.IntegerField(default=1.2)
    date_input = models.DateField(default=datetime.date.today())