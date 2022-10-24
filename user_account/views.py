from jejakarbon.models import User, DataCarbon

from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect,HttpResponse

# @login_required(login_url='/login/')
def show_account(request):
    user = User.objects.get(user=request.user)
    data_carbon = DataCarbon.objects.filter(user=user)
    context = {
        'user': user,
        'data_carbon': data_carbon,
    }
    return render(request, 'user_account.html', context)

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
    else:
        form = PasswordChangeForm(request.user)
    return HttpResponse('')