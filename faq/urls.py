from django.urls import path
from .views import show_faq, get_json, add_question, edit_faq, delete_faq

app_name = 'faq'

urlpatterns = [
    path('', show_faq, name='show_faq'),
    path('json/', get_json, name='get_json'),
    path('add/', add_question, name='add_question'),
    path('answer/<str:pk>', edit_faq, name='edit_faq'),
    path('delete/<str:pk>/', delete_faq, name='delete_faq'),
]
