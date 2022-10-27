from django.shortcuts import render
from .forms import FormFaq, FormAnswer
from .models import Faq
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers

# Create your views here.
def show_faq(request):
    form = FormFaq()
    faq = Faq.objects.all()
    context = { "faq" : faq, "form" : form }
    return render(request, 'faq.html', context)

def get_json(request):
    data = Faq.objects.all()
    return HttpResponse(serializers.serialize("json", data))

def add_question(request):
    if request.method == 'POST':
        form = FormFaq(request.POST)

        if form.is_valid():
            question = request.POST.get('question')
            faq = Faq(question=question)
            faq.save()
            return HttpResponse(b"CREATED")

    return HttpResponseNotFound()

def add_answer(request ,pk):
    if request.method == "POST":
        form = FormAnswer(request.POST)
        question = Faq.objects.get(id=pk)
        answer = request.POST.get('answer')
        faq = Faq(question=question.question,answer=answer)
        faq.save()
        return HttpResponse(b"UPDATE")
