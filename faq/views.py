from django.shortcuts import render, redirect
from .forms import FormFaq, AnswerFormAdmin
from .models import Faq
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.decorators import login_required

# Create your views here.
def show_faq(request):
    faqs = Faq.objects.all()
    form = FormFaq()
    form_admin = AnswerFormAdmin()

    # session
    if 'recently_answered' not in request.session:
        recently_answered_faq = None
    else:
        recently_answered_faq = Faq.objects.filter(pk__in=request.session['recently_answered'])
            
    context = {'form':form, 
               'username': request.user,
               'form_admin':form_admin, 
               'faqs' : faqs,
               'recently_answered_faq' : recently_answered_faq}

    return render(request, 'faq.html', context)

def get_json(request):
    data = Faq.objects.all()
    return HttpResponse(serializers.serialize("json", data))

@login_required(login_url='/login/')
def add_question(request):
    user = request.user
    if user.is_authenticated:
        if request.method == 'POST':
                form = FormFaq(request.POST)
                if form.is_valid():
                    question = form.cleaned_data.get('question')
                    faq = Faq(question=question, answer="", user=user, username=user)
                    faq.save()
                return HttpResponse(b"CREATED")
        else:
            form = FormFaq()
    else:
        return redirect('login:login_user')

@login_required(login_url='/login/')
def edit_faq(request, pk):
    form = AnswerFormAdmin()
    if request.method == 'POST':
        form = AnswerFormAdmin(request.POST)
        faq = Faq.objects.get(id=pk)

        new_answer = request.POST.get('answer')
        faq.answer = new_answer
        faq.save()

        if 'recently_answered' in request.session:
            if pk in request.session['recently_answered']:
                request.session['recently_answered'].remove(pk)

            request.session['recently_answered'].insert(0, pk)
            if len(request.session['recently_answered']) > 1:
                request.session['recently_answered'].pop()
        else:
            request.session['recently_answered'] = [pk]

        request.session.modified = True
        return redirect('faq:show_faq')

@login_required(login_url='/login/')
def delete_faq(request, pk):
    faq = Faq.objects.get(id=pk)
    faq.delete()
    return redirect('faq:show_faq')