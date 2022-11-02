import email
from sre_constants import SUCCESS
from urllib import request
from django.shortcuts import render

from faq.views import get_json
from .models import ikutdonasi
from form_donasi.models import OpenDonasi
from .forms import formPembayaran
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import HttpResponse
from django.contrib import admin
from django.core import serializers
from django.contrib.auth.decorators import login_required


def show_masukkan_nominal(request, id):
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
        'id_penerima_donasi' : id,
        'form': form,
    }
      
    return render(request,'form_berdonasi.html',context)

@login_required(login_url='/login/')
def pembayaran(request,id):
    if request.method=='POST':
 
        nominal = request.POST['nominal']
        pesan = request.POST['pesan']
        new_ikutdonasi = ikutdonasi(user=user,nominal=nominal,pesan=pesan)
        new_ikutdonasi.save()
        success = 'User' + nominal + pesan
    return render(request,'pembayaran.html')


def get_json(request, id):
    data = ikutdonasi.objects.all()
    return HttpResponse(serializers.serialize("json", data))

def add_nominal(request, id):
    obj = OpenDonasi.objects.get(pk=id)

    form = formPembayaran()
    if request.method == 'POST':
        form = formPembayaran(request.POST)
        if form.is_valid():
            nominal = request.POST['nominal']
            pesan = request.POST['pesan']


            new_ikutdonasi = ikutdonasi(user=request.user,nominal=nominal,pesan=pesan)
            obj.total_donasi_terkumpul += int(nominal)

            new_ikutdonasi.save()
            obj.save()

            return HttpResponse(b"CREATED")
