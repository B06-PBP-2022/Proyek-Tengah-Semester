from django.urls import path
from user_profile.views import show_profile, change_username, username_available, change_contact, change_email, is_organization, profile_json, is_username_available, change_username_flutter, change_contact_flutter, change_email_flutter, carbon_history_flutter, donation_history_flutter, opened_donation_flutter

app_name = 'user_profile'

urlpatterns = [
    path('', show_profile, name='show_profile'),
    path('change-username/', change_username, name='change_username'),
    path('username-available/', username_available, name='username_available'),
    path('change-contact/', change_contact, name='change_contact'),
    path('change-email/', change_email, name='change_email'),
    path('is-organization/', is_organization, name='is_organization'),
    path('profile-json/', profile_json, name='profile_json'),
    path('is-username-available/', is_username_available, name='is_username_available'),
    path('change-username-flutter/', change_username_flutter, name='change_username_flutter'),
    path('change-contact-flutter/', change_contact_flutter, name='change_contact_flutter'),
    path('change-email-flutter/', change_email_flutter, name='change_email_flutter'),
    path('carbon-history-flutter/', carbon_history_flutter, name='carbon_history_flutter'),
    path('donation-history-flutter/', donation_history_flutter, name='donation_history_flutter'),
    path('opened-donation-flutter/', opened_donation_flutter, name='opened_donation_flutter'),
]