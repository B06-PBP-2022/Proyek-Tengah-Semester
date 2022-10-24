from jejakarbon.models import User, DataCarbon

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse

from user_account.forms import EditPasswordForm, EditUsernameForm

# @login_required(login_url='/login/')
def show_account(request):
    user = User.objects.get(user=request.user)
    data_carbon = DataCarbon.objects.filter(user=user)
    username_form = EditUsernameForm()
    password_form = EditPasswordForm()
    context = {
        'user': user,
        'data_carbon': data_carbon,
        'username_form': username_form,
        'password_form': password_form
    }
    return render(request, 'user_account.html', context)

def change_username(request):
    if request.method == 'POST':
        user = User.objects.get(username = request.user.username)
        user.username = request.POST.get('username')
        user.save()
        messages.success(request, 'Your username was successfully updated!')
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
            return redirect('change_password')
        else:
            messages.error(request, 'Please correct the error below.')
    return HttpResponse('')