from django import forms
from kalkulator.models import KomponenKalkulator, CarbonDetail

class DetailListrikForm(forms.Form):
    class Meta:
        model = KomponenKalkulator
        fields = ['tagihan_listrik_rupiah', 'kilowatt_hour']

class DetailKendaraanForm(forms.Form):
    class Meta:
        model = KomponenKalkulator
        fields = ['fuel_type', 'kilometer_jarak', 'litre_per_km']