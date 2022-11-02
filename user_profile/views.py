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

from user_profile.forms import EditUsernameForm, EditAccountForm, PasswordChangingForm
from user_profile.models import LastEdited

@login_required(login_url='/login/')
def show_profile(request):

    # todo: PERLU HANDLE SUPERUSER
    profile = UserProfile.objects.get(user=request.user)

    passform = PasswordChangingForm(request.user, request.POST)

    # Handle password changing
    if request.method == 'POST':
        if passform.is_valid():
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
        }
    else :
        daftar_donasi = OpenDonasi.objects.filter(user = request.user)
        context = {
            'daftar_donasi': daftar_donasi,
            'passform': passform,
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
    return HttpResponse(contact)

@login_required(login_url='/login/')
def change_email(request):
    email = request.POST.get('email')
    user = request.user
    user.email = email
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