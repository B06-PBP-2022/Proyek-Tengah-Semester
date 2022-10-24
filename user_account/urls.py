from django.urls import path
from user_account.views import show_account

app_name = 'todolist'

urlpatterns = [
    path('', show_account, name='show_account'),
]