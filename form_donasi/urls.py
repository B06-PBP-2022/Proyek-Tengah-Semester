from unicodedata import name
from django.urls import path, include
from form_donasi.views import show_page, show_json, ajax_submit


app_name = 'form_donasi'

urlpatterns = [
    path('',show_page, name='show_page'),
    path('json/', show_json, name='show_json'),
    path('open-donasi/', ajax_submit ,name='open_donasi'),
    path('donasi/',include('berdonasi.urls'), name='donasi')
]
