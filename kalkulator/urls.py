from django.urls import path
from kalkulator.views import show_kalkulator, add_carbon_kendaraan, add_carbon_listrik

app_name = 'kalkulator'

urlpatterns = [
    path('', show_kalkulator, name='show_kalkulator'),
    path('calculate-kendaraan/', add_carbon_kendaraan, name='calculate-kendaraan'),
    path('calculate-listrik/', add_carbon_listrik, name='calculate-listrik')
]