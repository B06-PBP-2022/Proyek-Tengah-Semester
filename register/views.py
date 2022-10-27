from django.shortcuts import redirect, render, redirect
from django.contrib.auth import authenticate
from .forms import ExtendedUserCreationForm, UserProfileForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = ExtendedUserCreationForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            profile.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('login:login_user')

    else:
        form = ExtendedUserCreationForm()
        profile_form = UserProfileForm()

    context = {'form' : form, 'profile_form' : profile_form}
    return render(request, 'register.html', context)