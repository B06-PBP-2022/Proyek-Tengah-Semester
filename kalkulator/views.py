from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.core import serializers
from django.http import HttpResponse

from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from urllib3 import HTTPResponse

from kalkulator.forms import CarbonDetailForm, DetailListrikForm, DetailKendaraanForm
from kalkulator.models import CarbonPrintHistory, KomponenKalkulator, CarbonDetail
from register.models import UserProfile

import json

@login_required(login_url='/login/')
def show_kalkulator(request):
    form_detail = CarbonDetailForm()
    form_listrik = DetailListrikForm()
    form_kendaraan = DetailKendaraanForm()

    context = {
        'form_detail': form_detail,
        'form_listrik': form_listrik,
        'form_kendaraan': form_kendaraan}
    return render(request, 'show_kalkulator.html', context)

def show_json_carbon_detail(request):
    data = CarbonDetail.objects.filter(user = request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

# add login required untuk individual user
@login_required(login_url='/login/')
@csrf_exempt
def add_carbon_listrik(request):
    data = {}
    if request.method == "POST":

        print("ADD CARBON LISTRIK")

        kilowatt_hour = request.POST.get('kilowatt_hour')

        #  make KomponenKalkulator instance
        komponen_kalkulasi = KomponenKalkulator(kilowatt_hour=kilowatt_hour)
        komponen_kalkulasi.save()

        userprofile = UserProfile.objects.get(user=request.user)

        try:
            histori = CarbonPrintHistory.objects.get(user=userprofile)
        except CarbonPrintHistory.DoesNotExist:
            histori = CarbonPrintHistory(user=userprofile)
            histori.save()

        usage = request.POST.get('usage')
        carbon_print = float(kilowatt_hour)/0.794
        histori.carbon_print_total += carbon_print
        histori.save()

        # make DetailCarbon instance
        detail = CarbonDetail(
            histori_karbon=histori,
            usage=usage,
            carbon_print=carbon_print,
            komponen_kalkulasi=komponen_kalkulasi)
        detail.save()

        print(histori.carbon_print_total)

        # data = '{"pk" : detail.pk, "usage" : detail.usage, "detail_karbon" : detail.detail_karbon, "komponen_kalkulasi" : detail.komponen_kalkulasi, "date_input" : detail.date_input,}'
        data = {"pk": detail.pk}
    return JsonResponse(data)

@login_required(login_url='/login/')
@csrf_exempt
def add_carbon_kendaraan(request):
    data = {}
    if request.method == "POST":

        print("ADD CARBON KENDARAAN2")

        fuel_type = request.POST.get('fuel_type')
        kilometer_jarak = request.POST.get('kilometer_jarak')
        litre_per_km =request.POST.get('litre_per_km')

        #  make KomponenKalkulator instance
        komponen_kalkulasi = KomponenKalkulator(
            fuel_type=fuel_type,
            kilometer_jarak=kilometer_jarak,
            litre_per_km=litre_per_km)
        komponen_kalkulasi.save()

        userprofile = UserProfile.objects.get(user=request.user)

        try:
            histori = CarbonPrintHistory.objects.get(user=userprofile)
            print("masuk try")
        except CarbonPrintHistory.DoesNotExist:
            histori = CarbonPrintHistory(user=userprofile)
            histori.save()
            print("masuk except")
        
        usage = request.POST.get('usage')
        carbon_print = float(kilometer_jarak)/float(litre_per_km)/0.794
        print(histori.carbon_print_total)
        histori.carbon_print_total += carbon_print
        histori.save()

        # make DetailCarbon instance
        detail = CarbonDetail(
            histori_karbon=histori,
            usage=usage,
            carbon_print=carbon_print,
            komponen_kalkulasi=komponen_kalkulasi)
        detail.save()

        print(histori.carbon_print_total)
        print(histori.pk)

        # data = {"pk" : detail.pk,"usage" : detail.usage,"carbon_print" : detail.carbon_print,"komponen_kalkulasi" : detail.komponen_kalkulasi,"date_input" : detail.date_input}
        data = {"pk": detail.pk}
    return JsonResponse(data)

