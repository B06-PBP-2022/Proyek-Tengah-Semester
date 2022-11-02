import email
from sre_constants import SUCCESS
from urllib import request
from django.shortcuts import render

from faq.views import get_json
from .models import ikutdonasi
from .forms import formPembayaran
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import admin
from django.core import serializers


def show_masukkan_nominal(request):
    ikutberdonasi = ikutdonasi.objects.all()
    form = formPembayaran()

    # if request.method=='POST':
    #     nominal = request.POST.get['nominal']
    #     pesan = request.POST['pesan']
    #     new_ikutdonasi = ikutdonasi(nominal=nominal,pesan=pesan)
    #     new_ikutdonasi.save()
    #     success = 'User' + nominal + pesan
    
    context = {
        'ikutberdonasi': ikutberdonasi,
        'form': form,
    }
      
    return render(request,'form_berdonasi.html',context)

def pembayaran(request):
     if request.method=='POST':

        nominal = request.POST['nominal']
        pesan = request.POST['pesan']
        new_ikutdonasi = ikutdonasi(user=request.user,nominal=nominal,pesan=pesan)
        new_ikutdonasi.save()
        success = 'User' + nominal + pesan
        return HttpResponse(success)


def get_json(request):
    data = ikutdonasi.objects.all()
    return HttpResponse(serializers.serialize("json", data))

def add_nominal(request):
    form = formPembayaran()
    if request.method == 'POST':
        form = formPembayaran(request.POST)
        if form.is_valid():
            nominal = request.POST['nominal']
            pesan = request.POST['pesan']
            new_ikutdonasi = ikutdonasi(nominal=nominal,pesan=pesan)
            new_ikutdonasi.save()

            return HttpResponse(b"CREATED")
