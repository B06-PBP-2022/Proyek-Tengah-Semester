from django.urls import path
from form_donasi.views import show_page


app_name = 'form_donasi'

urlpatterns = [
    path('',show_page, name='show_page')
]
