from random import choices
from django.db import models
from django.conf import settings
from django.utils import timezone
from register.models import UserProfile
 
# tiap user punya 1 carbon print history yg isinya >1 detail2 carbonnya
class CarbonPrintHistory(models.Model):
    user = models.OneToOneField(
        UserProfile,
        on_delete=models.CASCADE,
        null=True,
        blank=True)
    carbon_print_total = models.FloatField(default=0)  

class KomponenKalkulator(models.Model):
    # listrik
    kilowatt_hour = models.FloatField(default=0)
    # kendaraan
    FUEL_TYPE_CHOICES = [
        ('bensin', 'Bensin'),
        ('diesel', 'Diesel')
    ]
    fuel_type = models.CharField(
        max_length=10, 
        choices=FUEL_TYPE_CHOICES, 
        blank=False,
        default='Unspecified')
    kilometer_jarak = models.FloatField(default=1)
    litre_per_km = models.FloatField(default=1.2)

class CarbonDetail(models.Model):
    histori_karbon = models.ForeignKey(
        CarbonPrintHistory, 
        on_delete=models.CASCADE
        )
    date_input = models.DateField(default=timezone.now)
    usage = models.CharField(max_length=10)
    carbon_print = models.FloatField()
    komponen_kalkulasi = models.OneToOneField(
        KomponenKalkulator, 
        on_delete=models.CASCADE,
        null=True,
        blank=True
        )

