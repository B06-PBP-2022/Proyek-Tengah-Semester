from django.shortcuts import render
from .models import ikutdonasi
from django.contrib.auth.forms import UserCreationForm


def show_masukkan_nominal(request):
    
    return render(request,'form_berdonasi.html')


