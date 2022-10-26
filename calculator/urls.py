from django.urls import path
from views import carbon_calculator

app_name = ['calculator']

urlpatterns = [
    path('calculate-carbon/', carbon_calculator, name='carbon_calculator'),
]

