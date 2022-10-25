from django.urls import path
from views import carbon_calculator

app_name = ['jejakarbon']

urlpatterns = [
    path('calculate-carbon/', carbon_calculator, name='carbon_calculator'),
]

