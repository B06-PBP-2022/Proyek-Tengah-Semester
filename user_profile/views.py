import datetime
# from kalkulator.models import DataCarbon
from register.models import UserProfile
# from calculator.models import DataCarbon

from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse

from user_profile.forms import EditUsernameForm, EditAccountForm
from user_profile.models import LastEdited

@login_required(login_url='/login/')
def show_profile(request):
    # # data_carbon = DataCarbon.objects.filter(user = request.user)
    username_form = EditUsernameForm()
    # edit_account_form = EditAccountForm()
    # password_form = PasswordChangeForm(request.user, request.POST)
    context = {
        'username_form': username_form,
        # 'edit_account_form': edit_account_form,
    #     'data_carbon': data_carbon,
    #     'username_form': username_form,
    #     'password_form': password_form,
    #     'last_username_edited': LastEdited.objects.get(user = request.user).last_username_edited,
    #     'last_password_edited': LastEdited.objects.get(user = request.user).last_password_edited
    }
    return render(request, 'user_profile.html', context)

def change_username(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # Update username
        user = request.user
        user.username = username
        user.save()
        messages.success(request, 'Your username was successfully updated!')
        # # Menyimpan data kapan username terakhir kali diedit
        # last_edited = LastEdited.objects.get(user = request.user)
        # if last_edited is not None:
        #     # Mengubah field LastEdited
        #     last_edited.last_username_edited = datetime.date.today()
        #     last_edited.save()
        # else:
        #     # Membuat objek LastEdited baru
        #     last_edited = LastEdited(user = request.user)
        #     last_edited.last_username_edited = datetime.date.today()
        #     last_edited.save()
    return HttpResponse(user.username)

@csrf_exempt
def username_available(request):
    username = request.GET.get('username')
    user = User.objects.filter(username = username).exists()
    if user:
        return HttpResponse(False)
    else:
        return HttpResponse(True)

def username_json(request):
    return JsonResponse({'username': request.user.username})

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            # return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    return HttpResponse('')
