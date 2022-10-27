from django import forms

class EditUsernameForm(forms.Form):
    username = forms.CharField(max_length=200)

class EditPasswordForm(forms.Form):
    old_username = forms.CharField(max_length=200)
    password = forms.CharField(max_length=200)
    confirm_password = forms.CharField(max_length=200)