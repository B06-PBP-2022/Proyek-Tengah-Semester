from django.shortcuts import render, redirect
from .forms import FormFaq, AnswerFormAdmin
from .models import Faq
from django.http import HttpResponse, HttpResponseNotFound
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_faq(request):
    faqs = Faq.objects.all()
    form = FormFaq()
    form_admin = AnswerFormAdmin()
    context = {'form':form, 'username': request.user, 'form_admin':form_admin, 'faqs' : faqs}
    return render(request, 'faq.html', context)

def get_json(request):
    data = Faq.objects.all()
    return HttpResponse(serializers.serialize("json", data))

@login_required(login_url='/login/')
def add_question(request):
    user = request.user
    if request.method == 'POST':
        if user.is_authenticated:
            form = FormFaq(request.POST)

            if form.is_valid():
                question = form.cleaned_data.get('question')
                faq = Faq(question=question, answer="", user=user, username=user)
                faq.save()
            return HttpResponse(b"CREATED")
        else:
            return redirect('login:login_user')

    else:
        form = FormFaq()
    return HttpResponseNotFound()

@login_required(login_url='/login/')
def edit_faq(request, pk):
    form = AnswerFormAdmin()
    if request.method == 'POST':
        form = AnswerFormAdmin(request.POST)
        faq = Faq.objects.get(id=pk)

        new_answer = request.POST.get('answer')
        faq.answer = new_answer
        faq.save()
        return redirect('faq:show_faq')