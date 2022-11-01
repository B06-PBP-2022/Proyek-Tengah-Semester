from django.urls import path
from user_profile.views import show_profile, change_username, username_available

app_name = 'user_profile'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('change-username/', change_username, name='change_username'),
    path('username-available/', username_available, name='username_available'),
]