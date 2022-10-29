import datetime
from calculator.models import DataCarbon
from register.models import UserProfile

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse

from user_profile.forms import EditPasswordForm, EditUsernameForm
from user_profile.models import LastEdited

@login_required(login_url='/login/')
def show_profile(request):
    user_profile = UserProfile.objects.get(user = request.user)
    # data_carbon = DataCarbon.objects.filter(user = request.user)
    # username_form = EditUsernameForm()
    # password_form = PasswordChangeForm(request.user, request.POST)
    context = {
        'user_profile': user_profile,
    #     'data_carbon': data_carbon,
    #     'username_form': username_form,
    #     'password_form': password_form,
    #     'last_username_edited': LastEdited.objects.get(user = request.user).last_username_edited,
    #     'last_password_edited': LastEdited.objects.get(user = request.user).last_password_edited
    }
    return render(request, 'user_profile.html')

def change_username(request):
    if request.method == 'POST':
        form = EditUsernameForm(request.POST)
        if form.is_valid():
            # Mengubah username
            user = User.objects.get(username = request.user.username)
            user.username = request.POST.get('username')
            user.save()
            # Menyimpan data kapan username terakhir kali diedit
            last_edited = LastEdited.objects.get(user = request.user)
            if last_edited is not None:
                # Mengubah field LastEdited
                last_edited.last_username_edited = datetime.date.today()
                last_edited.save()
            else:
                # Membuat objek LastEdited baru
                last_edited = LastEdited(user = request.user)
                last_edited.last_username_edited = datetime.date.today()
                last_edited.save()
            # Menampilkan pesan sukses
            messages.success(request, 'Your username was successfully updated!')
        else :
            messages.error(request, 'Please correct the error below.')
    else:
        messages.error(request, 'Please correct the error below.')
    return HttpResponse('')

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