from django.urls import path
from kalkulator.views import show_kalkulator, add_carbon_kendaraan, add_carbon_listrik
from kalkulator.views import add_carbon_kendaraan_flutter, add_carbon_listrik_flutter
from kalkulator.views import show_json_carbon_detail, user_histori

app_name = 'kalkulator'

urlpatterns = [
    path('', show_kalkulator, name='show_kalkulator'),
    path('calculate-kendaraan/', add_carbon_kendaraan, name='calculate-kendaraan'),
    path('calculate-listrik/', add_carbon_listrik, name='calculate-listrik'),
    path('calculate-kendaraan-flutter/', add_carbon_kendaraan_flutter, name='calculate-kendaraan-flutter'),
    path('calculate-listrik-flutter/', add_carbon_listrik_flutter, name='calculate-listrik-flutter'),
    path('kalkulator-json/', show_json_carbon_detail, name='show_json_carbon_detail'),
    path('get_total_carbon/', user_histori, name='user_histori'),
]