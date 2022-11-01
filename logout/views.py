from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AnonymousUser

# Create your views here.
@login_required(login_url='/login/')
def logout_user(request):
    logout(request)
    request.session.flush()
    request.user = AnonymousUser
    return redirect('home:index')