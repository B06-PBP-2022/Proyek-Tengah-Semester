from unicodedata import name
from django.urls import path
from .views import logout_user

app_name = 'logout'

urlpatterns = [ 
    path('', logout_user, name='logout'),
]