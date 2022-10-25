from django.urls import path
from user_profile.views import show_profile

app_name = 'todolist'

urlpatterns = [
    path('', show_profile, name='show_profile'),
]