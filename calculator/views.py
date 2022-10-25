# rendering stuff
from django.shortcuts import redirect, render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse

# general form stuff
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers

# authentication stuff
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login

from django.contrib import messages

# TODO: add login required here
def carbon_calculator(request):
    if request.method == "POST":
        jenis_pemakaian = request.POST.get('usage')
        if jenis_pemakaian == "listrik":
            messages.info("Listrik dipilih")
        if jenis_pemakaian == "mobil":
            messages.info("Mobil dipilih")
        if jenis_pemakaian == "motor":
            messages.info("Motor dipilih")
