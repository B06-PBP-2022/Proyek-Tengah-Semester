from django import forms
from kalkulator.models import KomponenKalkulator, CarbonDetail
from django.utils.translation import gettext_lazy as _

SATUAN_JARAK = [
    ('km','km'),
    ('mil', 'mil')
]

USAGE_CHOICES = [
    ('listrik', 'Listrik'),
    ('mobil', 'Mobil'),
    ('motor', 'Motor')
]

# FUEL_TYPE_CHOICES = [
#     ('bensin', 'Bensin'),
#     ('diesel', 'Diesel')
# ]

class DetailListrikForm(forms.ModelForm):
    class Meta:
        model = KomponenKalkulator
        fields = ['kilowatt_hour']
        widgets = {
            'kilowatt_hour' : forms.NumberInput(
                attrs={
                    'class': "form-control form-kalkulator",
                    'id': 'kilowatt_hour',
                    'name': 'kilowatt_hour'
                }
            ),
        }

class CarbonDetailForm(forms.ModelForm):
    class Meta:
        model = CarbonDetail
        fields = ['usage','carbon_print']
        widgets = {
            'usage' : forms.Select(
                choices=USAGE_CHOICES,
                attrs={
                    'class': "form-select form-select-lg",
                    'aria-label': ".form-select-lg",
                    'id': 'usage',
                    'name': 'usage'
                }
            ),
        }

class DetailKendaraanForm(forms.ModelForm):
    class Meta:
        model = KomponenKalkulator
        fields = ['fuel_type', 'kilometer_jarak', 'litre_per_km']
        widgets = {
            'fuel_type' : forms.RadioSelect(
                attrs={
                    'class': "form-check fuel-type-class",
                    'name': 'fuel_type',
                    'id': 'fuel_type'
                }
            ),
            'kilometer_jarak' : forms.NumberInput(
                attrs={
                    'class': "form-control form-calculator",
                    'name': 'kilometer_jarak',
                    'id': 'kilometer_jarak'
                }
            ),
            'litre_per_km' : forms.NumberInput(
                attrs={
                    'class': "form-control form-calculator",
                    'name': 'litre_per_km',
                    'id': 'litre_per_km'
                }
            ),
        }

    pilihan_satuan = forms.ChoiceField(widget=forms.Select, choices=SATUAN_JARAK)
