import datetime
from kalkulator.models import CarbonDetail, CarbonPrintHistory
from register.models import UserProfile
from form_donasi.models import OpenDonasi
from berdonasi.models import ikutdonasi

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.core import serializers

from user_profile.forms import PasswordChangingForm
from user_profile.models import LastEdited

@login_required(login_url='/login/')
def show_profile(request):

    profile = UserProfile.objects.get(user=request.user)
    passform = PasswordChangingForm(request.user, request.POST)

    # Instansiasi last edited
    try:
        last_edited = LastEdited.objects.get(user = request.user)
    except:
        last_edited = LastEdited(user = request.user)

    # Handle password changing
    if request.method == 'POST':
        if passform.is_valid():
            last_edited.save()
            user = passform.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('user_profile:show_profile')
        else:
            messages.error(request, 'Please correct the error.')
            return HttpResponse('')

    # Passing data to template
    if not profile.organization:
        try:
            histori_karbon = CarbonPrintHistory.objects.get(user = profile)
        except:
            histori_karbon = CarbonPrintHistory(user = profile)
            histori_karbon.save()

        detail_karbon = CarbonDetail.objects.filter(histori_karbon = histori_karbon)
        histori_berdonasi = ikutdonasi.objects.filter(user = request.user)
        context = {
            'histori_karbon': histori_karbon,
            'detail_karbon': detail_karbon,
            'histori_berdonasi': histori_berdonasi,
            'passform': passform,
            'last_edited': last_edited,
        }
    else :
        daftar_donasi = OpenDonasi.objects.filter(user = request.user)
        context = {
            'daftar_donasi': daftar_donasi,
            'passform': passform,
            'last_edited': last_edited,
        }

    # Render template
    return render(request, 'user_profile.html', context)

@login_required(login_url='/login/')
def change_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # Update username
        user = request.user
        user.username = username
        user.save()
        messages.success(request, 'Your username was successfully updated!')
    return HttpResponse(user.username)

@csrf_exempt
def username_available(request):
    username = request.GET.get('username')
    user = User.objects.filter(username = username).exists()
    if user:
        return HttpResponse(False)
    else:
        return HttpResponse(True)

@login_required(login_url='/login/')
def username_json(request):
    return JsonResponse({'username': request.user.username})

@login_required(login_url='/login/')
def change_contact(request):
    contact = request.POST.get('contact')
    profile = UserProfile.objects.get(user=request.user)
    profile.contact = contact
    profile.save()
    return HttpResponse(contact)

@login_required(login_url='/login/')
def change_email(request):
    email = request.POST.get('email')
    user = request.user
    user.email = email
    user.save()
    return HttpResponse(email)

@login_required(login_url='/login/')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error.')
    return HttpResponse('')

@login_required(login_url='/login/')
def is_organization(request):
    return HttpResponse(request.user.is_organization)



# FOR FLUTTER

@login_required(login_url='/login/')
def profile_json(request):
    user = request.user
    profile = UserProfile.objects.get(user=request.user)
    return JsonResponse(
        {
            "status": True,
            "username" : user.username,
            "email" : user.email,
            "is_admin" : user.is_superuser,
            "contact" : profile.contact,
            "name" : profile.name,
            "organization" : profile.organization,
        }, 
        status=200
    )

@csrf_exempt
def is_username_available(request):
    username = request.GET.get('username')
    user = User.objects.filter(username = username).exists()
    if user:
        return JsonResponse({"available": False}, status=200)
    else:
        return JsonResponse({"available": True}, status=200)

@csrf_exempt
@login_required(login_url='/login/')
def change_username_flutter(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # Update username
        user = request.user
        user.username = username
        user.save()
        messages.success(request, 'Your username was successfully updated!')
    return JsonResponse({"username": request.user.username}, status=200)

@csrf_exempt
@login_required(login_url='/login/')
def change_contact_flutter(request):
    contact = request.POST.get('contact')
    profile = UserProfile.objects.get(user=request.user)
    profile.contact = contact
    profile.save()
    return JsonResponse({"contact": contact}, status=200)

@csrf_exempt
@login_required(login_url='/login/')
def change_email_flutter(request):
    email = request.POST.get('email')
    user = request.user
    user.email = email
    user.save()
    return JsonResponse({"email": request.user.email}, status=200)

@csrf_exempt
@login_required(login_url='/login/')
def carbon_history_flutter(request):
    profile = UserProfile.objects.get(user=request.user)
    if not profile.organization:
        try:
            histori_karbon = CarbonPrintHistory.objects.get(user = profile)
        except:
            histori_karbon = CarbonPrintHistory(user = profile)
            histori_karbon.save()

        detail_karbon = CarbonDetail.objects.filter(histori_karbon = histori_karbon)
        # histori_berdonasi = ikutdonasi.objects.filter(user = request.user)
        context = {
            'carbon_history': histori_karbon,
            'carbon_detail': detail_karbon,
            # 'histori_berdonasi': histori_berdonasi,
            # 'passform': passform,
            # 'last_edited': last_edited,
        }

        data_total_carbon = {'total_carbon': histori_karbon.carbon_print_total}
        data_carbon_detail = {'carbon_detail': {}}


        set = data_carbon_detail['carbon_detail']
        for detail in detail_karbon:
            # for key, value in detail.__dict__.items():
            #     # if key == '_state':
            #     #     continue
            #     data['carbon_detail'].add({key: value})
            usage = detail.usage
            date_input = detail.date_input.strftime("%d/%m/%Y")
            carbon_print = detail.carbon_print
            set.add({'usage':usage, 'date_input':date_input, 'carbon_print':carbon_print})

        
        # return JsonResponse(serializers.serialize("json", data), content_type="application/json")
        # data = {**data_total_carbon, **data_carbon_detail

        data = set()
        data.add(data_total_carbon)
        data.add(data_carbon_detail)
        
        return JsonResponse(data, status=200)
    else :
        return JsonResponse({'message':'You must logged in with a personal account'},status=404)

@csrf_exempt
@login_required(login_url='/login/')
def donation_history_flutter(request):
    profile = UserProfile.objects.get(user=request.user)
    if not profile.organization:
        # try:
        #     histori_karbon = CarbonPrintHistory.objects.get(user = profile)
        # except:
        #     histori_karbon = CarbonPrintHistory(user = profile)
        #     histori_karbon.save()

        # detail_karbon = CarbonDetail.objects.filter(histori_karbon = histori_karbon)
        histori_berdonasi = ikutdonasi.objects.filter(user = request.user)
        context = {
            # 'histori_karbon': histori_karbon,
            # 'detail_karbon': detail_karbon,
            'donation_history': histori_berdonasi,
            # 'passform': passform,
            # 'last_edited': last_edited,
        }

        return JsonResponse(context, status=200)
    else :
        return JsonResponse({'message':'You must logged in with a personal account'},status=404)


@csrf_exempt
@login_required(login_url='/login/')
def opened_donation_flutter(request):
    profile = UserProfile.objects.get(user=request.user)
    if profile.organization:
        daftar_donasi = OpenDonasi.objects.filter(user = request.user)
        context = {
            'opened_donation': daftar_donasi,
            # 'passform': passform,
            # 'last_edited': last_edited,
        }

        return JsonResponse(context, status=200)
    else :
        return JsonResponse({'message':'You must logged in with an organizational account'},status=404)