from django.urls import path
from form_donasi.views import show_page, login_user, register, show_json


app_name = 'form_donasi'

urlpatterns = [
    path('',show_page, name='show_page'),
    path('json/', show_json, name='show_json')
]
