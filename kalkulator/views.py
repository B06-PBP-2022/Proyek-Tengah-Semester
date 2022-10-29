from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.csrf import csrf_exempt

from kalkulator.forms import CarbonDetailForm, DetailListrikForm, DetailKendaraanForm
from kalkulator.models import CarbonPrintHistory, KomponenKalkulator, CarbonDetail

# @login_required(login_url='/login/')
def show_kalkulator(request):
    form_detail = CarbonDetailForm()
    form_listrik = DetailListrikForm()
    form_kendaraan = DetailKendaraanForm()

    context = {
        'form_detail': form_detail,
        'form_listrik': form_listrik,
        'form_kendaraan': form_kendaraan}
    return render(request, 'show_kalkulator.html', context)

# add login required untuk individual user
@csrf_exempt
def add_carbon_listrik(request):

    data = {}
    if request.method == "POST":

        print("ADD CARBON LISTRIK")

        kilowatt_hour = request.POST.get('kilowatt_hour')

        #  make KomponenKalkulator instance
        komponen_kalkulasi = KomponenKalkulator(kilowatt_hour=kilowatt_hour)
        komponen_kalkulasi.save()

        histori = get_object_or_404(CarbonPrintHistory, user=request.user)
        usage = request.POST.get('usage')
        carbon_print = kilowatt_hour/0.794
        histori.carbon_print_total += carbon_print

        # make DetailCarbon instance
        detail = CarbonDetail(
            histori_karbon=histori,
            usage=usage,
            carbon_print=carbon_print,
            komponen_kalkulasi=komponen_kalkulasi)
        detail.save()

        print(histori.carbon_print_total + " INI DIA YAH LISTRIK TOTAL")

        data = {
                "pk" : detail.pk,
                "usage" : detail.usage,
                "detail_karbon" : detail.detail_karbon,
                "komponen_kalkulasi" : detail.komponen_kalkulasi,
                "date_input" : detail.date_input,

            }

    return JsonResponse(data)


    #     form_listrik = DetailListrikForm(request.POST)
    #     form_detail = CarbonDetailForm(request.POST)
    #     if all((form_listrik.is_valid(), form_detail.is_valid())):
    #         print("ADD CARBON LISTRIK")
    #         # set Histori
    #         histori = get_object_or_404(CarbonPrintHistory, user=request.user)
            
    #         # save form
    #         komponen_listrik = form_listrik.save()
    #         detail = form_detail.save(commit=False)
    #         # hitung emisi CO2
    #         detail.komponen_kalkulasi = komponen_listrik
    #         detail.carbon_print = detail.komponen_kalkulasi.kilowatt_hour*0.794
    #         # form_detail.cleaned_data['kilowatt_hour']
    #         data = {
    #             "pk" : form_detail.pk,
    #             "usage" : form_detail.usage,
    #             "detail_karbon" : form_detail.detail_karbon,
    #             "komponen_kalkulasi" : form_detail.komponen_kalkulasi,
    #             "date_input" : form_detail.date_input,

    #         }
            
    #         # update total carbon print user
    #         detail.histori_karbon = histori
    #         detail.histori_karbon.carbon_print_total = detail.histori_karbon.carbon_print_total+detail.carbon_print  
    #         # save input form sbg object baru
    #         form_detail.save()
            
    # return JsonResponse(data)

@csrf_exempt
def add_carbon_kendaraan(request):
    data = {}
    print("ADD CARBON KENDARAAN1111")
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

        histori = get_object_or_404(CarbonPrintHistory, user=request.user)
        usage = request.POST.get('usage')
        carbon_print = kilometer_jarak*litre_per_km/0.794
        histori.carbon_print_total += carbon_print

        # make DetailCarbon instance
        detail = CarbonDetail(
            histori_karbon=histori,
            usage=usage,
            carbon_print=carbon_print,
            komponen_kalkulasi=komponen_kalkulasi)
        detail.save()

        print(histori.carbon_print_total + " INI DIA YAH")

        data = {
                "pk" : detail.pk,
                "usage" : detail.usage,
                "detail_karbon" : detail.detail_karbon,
                "komponen_kalkulasi" : detail.komponen_kalkulasi,
                "date_input" : detail.date_input,

            }

    return JsonResponse(data)


        # form_kendaraan = DetailKendaraanForm(request.POST)
        # form_detail = CarbonDetailForm(request.POST)
        
        # if form_detail.is_valid():
        #     print("ADD CARBON KENDARAAN1111")

        # if all((form_kendaraan.is_valid(), form_detail.is_valid())):
        #     print("ADD CARBON KENDARAAN")
        #     # set Histori
        #     histori = get_object_or_404(CarbonPrintHistory, user=request.user)
            
        #     # save form
        #     komponen_kendaraan = form_kendaraan.save()
        #     detail = form_detail.save(commit=False)
        #     # hitung emisi CO2
        #     detail.komponen_kalkulasi = komponen_kendaraan
        #     detail.carbon_print = detail.komponen_kalkulasi.kilowatt_hour*0.794
        #     # form_detail.cleaned_data['kilowatt_hour']
        #     data = {
        #         "pk" : form_detail.pk,
        #         "usage" : form_detail.usage,
        #         "detail_karbon" : form_detail.detail_karbon,
        #         "komponen_kalkulasi" : form_detail.komponen_kalkulasi,
        #         "date_input" : form_detail.date_input,

        #     }
            
        #     # update total carbon print user
        #     detail.histori_karbon = histori
        #     detail.histori_karbon.carbon_print_total = detail.histori_karbon.carbon_print_total+detail.carbon_print  
        #     # save input form sbg object baru
        #     form_detail.save()

        #     print(data["usage"])
            
    # return JsonResponse(data)