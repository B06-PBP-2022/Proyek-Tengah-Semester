from unicodedata import name
from django.urls import path, include
from form_donasi.views import show_page, show_json, ajax_submit, berdonasi, add_donasi_flutter, show_json_user,delate_event, edit_event_flutter


app_name = 'form_donasi'

urlpatterns = [
    path('',show_page, name='show_page'),
    path('json/', show_json, name='show_json'),
    path('json-user/', show_json_user, name='show_json_user'),
    path('open-donasi/', ajax_submit ,name='open_donasi'),
    path('open-donasi-flutter/', add_donasi_flutter ,name='open_donasi_flutter'),
    path('donasi/<int:id>/',berdonasi, name='donasi'),
    path('delete-event/<str:pk>/',delate_event, name='tutup_donasi'),
    path('edit-event/<str:pk>/',edit_event_flutter, name='edit_donasi'),
    

    # path('donasi/',include('berdonasi.urls'), name='donasi')
]
