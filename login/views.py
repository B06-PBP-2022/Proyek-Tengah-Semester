from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.
def login_user(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home:index')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home:index')
        else:
            messages.info(request, 'The username or password is incorrect!')
    context = {}
    return render(request, 'login.html', context)