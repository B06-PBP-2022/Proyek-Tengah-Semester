from django.db import models
from django.conf import settings
from django.utils import timezone
 
# ambil usernya nanti dari modelsnya rania
class UserTemp(models.Model):
    user_logged_in = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
 
# tiap user punya 1 carbon print history yg isinya >1 detail2 carbonnya
class CarbonPrintHistory(models.Model):
    carbon_print_total = models.PositiveIntegerField(default=0)  

class KomponenKalkulator(models.Model):
    # listrik
    tagihan_listrik_rupiah = models.IntegerField(default=0)
    kilowatt_hour = models.FloatField(default=0)
    # kendaraan
    fuel_type = models.CharField(max_length=10)
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

