from django.urls import path
from berdonasi.views import show_masukkan_nominal
from berdonasi.views import pembayaran


app_name = 'berdonasi'

urlpatterns = [
    path('',show_masukkan_nominal, name='show_masukkan_nominal'),
    path('pembayaran',pembayaran, name='pembayaran')
]
