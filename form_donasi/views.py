import imp
from django.shortcuts import render
from .models import OpenDonasi

from django.shortcuts import render
from . import forms

from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


from django.contrib.auth import authenticate, login

from django.contrib.auth import logout

from django.contrib.auth.decorators import login_required

import datetime
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core import serializers
from django.urls import reverse

from .forms import OpenDonasiForm
# ======================================================================================


# Create your views here.
@login_required(login_url='/login')
def show_page(request):
    return render(request,'form_buat_donasi.html')

def show_json(request):
    data = OpenDonasi.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def ajax_submit(request):
    if (request.method == 'POST'):
        user = request.user
        organization = user.userprofile.organization
        
        data = {}
        form = forms.OpenDonasiForm(request.POST or None)
        if (form.is_valid()):
            tema_kegiatan = form.cleaned_data['tema_kegiatan']
            deskripsi = form.cleaned_data['deskripsi']
            target_donasi = form.cleaned_data['target_donasi']
            new_data = OpenDonasi.objects.create(user=user, pencetus_donasi = user.username , tema_kegiatan=tema_kegiatan, target_donasi=target_donasi, total_donasi_terkumpul=0, deskripsi=deskripsi)
            data["tema_kegiatan"] = tema_kegiatan
            data["tanggal_pembuatan"] = new_data.tanggal_pembuatan
            data["deskripsi"] = new_data.deskripsi
            data["pencetus_donasi"] = new_data.pencetus_donasi
            data["target_donasi"] = new_data.target_donasi
            data["total_donasi_terkumpul"] = new_data.total_donasi_terkumpul
            data["pk"] = new_data.pk
            
            new_data.save()
            return JsonResponse(data)
        # else:
        #     messages.info(request, 'Untuk dapat membuat forum donasi, akun harus merupakan akun organisasi!!!')
        

