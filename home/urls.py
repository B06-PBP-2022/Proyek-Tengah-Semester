from django.urls import path, include
from home.views import index

app_name = 'home'

urlpatterns = [
    path('', index, name='index'),
    path('daftar-donasi/',include('form_donasi.urls'),name='daftar_donasi'),
    path('donasi/',include('berdonasi.urls'), name='donasi')
]