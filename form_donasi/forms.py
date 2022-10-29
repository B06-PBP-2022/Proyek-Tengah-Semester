from django.forms import ModelForm
from .models import OpenDonasi

class OpenDonasiForm(ModelForm):
    class Meta:
        model = OpenDonasi
        fields = ['tema_kegiatan','deskripsi','target_donasi']