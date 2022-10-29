from django.urls import path
from berdonasi.views import show_masukkan_nominal


app_name = 'berdonasi'

urlpatterns = [
    path('',show_masukkan_nominal, name='show_masukkan_nominal')
]
