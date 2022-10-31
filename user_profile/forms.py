from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class EditUsernameForm(forms.Form):
    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))

class EditAccountForm(UserChangeForm):

    username = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = (
            'username',
            # 'email',
        )