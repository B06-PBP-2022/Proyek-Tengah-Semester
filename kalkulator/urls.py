from django.urls import path
from kalkulator.views import show_kalkulator_listrik

app_name = 'kalkulator'

urlpatterns = [
    path('', show_kalkulator_listrik, name='show_kalkulator_listrik')
]