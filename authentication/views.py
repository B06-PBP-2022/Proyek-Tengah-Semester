import json
from django.contrib.auth import authenticate, login as auth_login, logout
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from register.models import UserProfile

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            profile = UserProfile.objects.get(user=user)
            # Redirect to a success page.
            return JsonResponse({
            "status": True,
            "message": "Successfully Logged In!",
            # Insert any extra data if you want to pass data to Flutter
            "id" : user.id,
            "username" : user.username,
            "email" : user.email,
            "is_admin" : user.is_superuser,
            "contact" : profile.contact,
            "name" : profile.name,
            "organization" : profile.organization,
            }, status=200)
        else:
            return JsonResponse({
            "status": False,
            "message": "Failed to Login, Account Disabled."
            }, status=401)

    else:
        return JsonResponse({
        "status": False,
        "message": "Failed to Login, check your email/password."
        }, status=401)

@csrf_exempt
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        username = data["username"]
        email = data["email"]
        password1 = data["password1"]
        password2 = data["password2"]
        name = data['name']
        contact = data['contact']
        organization = data['organization']

        if password1 != password2:
            return JsonResponse({'status': 'failed', 'message': 'Gagal woi'})

        newUser = User.objects.create_user(username = username, email = email, password = password1)
        newUser.save()
        userProfile = UserProfile(user = newUser, name = name, contact = contact, organization = organization)
        userProfile.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def logout(request):
    try:
        logout(request)
        return JsonResponse({
                    "status": True,
                    "message": "Successfully Logged out!",
                }, status=200)
    except:
        return JsonResponse({
          "status": False,
          "message": "Failed to Logout"
        }, status=401)