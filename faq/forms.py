from dataclasses import field
from django import forms
from .models import Faq

class FormFaq(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['question']

class FormAnswer(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['answer']