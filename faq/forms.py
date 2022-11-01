from django import forms
from .models import Faq

class FormFaq(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['question']
        widgets = {
            'question': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Tanyakan Seputar JejaKarbon'}),
        }

class AnswerFormAdmin(forms.ModelForm):
    class Meta:
        model = Faq
        fields = ['answer']
        widgets = {
            'answer': forms.TextInput(attrs={'class': 'form-control', 'placeholder' : 'Jawab Pertanyaan'}),
        }
