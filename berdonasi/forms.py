from django.forms import ModelForm
from .models import ikutdonasi

class formPembayaran(ModelForm):
    class Meta:
        model = ikutdonasi
        fields = ['nominal','pesan']