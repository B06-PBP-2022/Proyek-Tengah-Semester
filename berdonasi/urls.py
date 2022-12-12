from django.urls import path
from berdonasi.views import add_nominal, show_masukkan_nominal
from berdonasi.views import pembayaran
from berdonasi.views import get_json
from berdonasi.views import add_nominal

app_name = 'berdonasi'

urlpatterns = [
    path('<int:id>/',show_masukkan_nominal, name='show_masukkan_nominal'),
    path('<int:id>/pembayaran/',pembayaran, name='pembayaran'),
    path('<str:pk>/json/',get_json, name='get_json'),
    path('<int:id>/add/',add_nominal, name='add_nominal'),
]
