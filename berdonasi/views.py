import email
from sre_constants import SUCCESS
from django.shortcuts import render
from .models import ikutdonasi
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import admin


def show_masukkan_nominal(request):

    return render(request,'form_berdonasi.html')

def pembayaran(request):
     if request.method=='POST':
        nominal = request.POST['nominal']
        pesan = request.POST['pesan']
        new_ikutdonasi = ikutdonasi(nominal=nominal,pesan=pesan)
        new_ikutdonasi.save()
        success = 'User' + nominal + pesan
        return HttpResponse(success)
