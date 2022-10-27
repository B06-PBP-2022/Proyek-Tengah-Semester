from django.urls import path
from .views import show_faq, get_json, add_answer, add_question

app_name = 'faq'

urlpatterns = [
    path('', show_faq, name='show_faq'),
    path('json/', get_json, name='get_json'),
    path('add/', add_question, name='add_question'),
    path('answer/<str:pk>/', add_answer, name='add_answer')
]
