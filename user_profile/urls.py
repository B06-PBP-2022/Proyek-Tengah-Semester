from django.urls import path
from user_profile.views import show_profile, change_username, username_available, change_contact, change_email, is_organization, profile_json, is_username_available

app_name = 'user_profile'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('change-username/', change_username, name='change_username'),
    path('username-available/', username_available, name='username_available'),
    path('change-contact/', change_contact, name='change_contact'),
    path('change-email/', change_email, name='change_email'),
    path('is-organization/', is_organization, name='is_organization'),
    path('profile-json/', profile_json, name='profile_json'),
    path('is-username-available/', is_username_available, name='is_username_available')
]