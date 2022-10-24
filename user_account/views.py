from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# @login_required(login_url='/todolist/login/')
def show_account(request):
    return render(request, "user_account.html")