from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from kalkulator.forms import DetailListrikForm


def show_kalkulator_listrik(request):
    if request.method == "POST":
        form = DetailListrikForm(request.POST)
        if form.is_valid():
            tempsave = form.save(commit=False)
            tempsave.user = request.user
            form.save()
            return redirect('/')
    return redirect('/')
