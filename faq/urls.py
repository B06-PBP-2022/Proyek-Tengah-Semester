from django.urls import path
from .views import show_faq, add_question, edit_faq, delete_faq, show_json, add_question_flutter, edit_question_flutter

app_name = 'faq'

urlpatterns = [
    path('', show_faq, name='show_faq'),
    path('add/', add_question, name='add_question'),
    path('answer/<str:pk>', edit_faq, name='edit_faq'),
    path('delete/<str:pk>/', delete_faq, name='delete_faq'),
    path('json/', show_json, name='show_json'),
    path('add-question/', add_question_flutter, name='add_question_flutter'),
    path('edit-question/<str:pk>/', edit_question_flutter, name='edit_question_flutter'),
]
