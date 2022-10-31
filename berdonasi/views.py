from django.shortcuts import render
from .models import ikutdonasi
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages


def show_masukkan_nominal(request):

    return render(request,'form_berdonasi.html')

def pembayaran(request):
    
    return render(request,'pembayaran.html')
