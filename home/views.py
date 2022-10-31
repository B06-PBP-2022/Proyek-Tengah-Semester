from django.shortcuts import render
from form_donasi.models import OpenDonasi


def index(request):
    data = OpenDonasi.objects.all()
    context = {'data' : data}
    return render(request, 'index.html', context)
