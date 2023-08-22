from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User


def home(request):
    return HttpResponse(
        "<div style='display: flex; justify-content: center; align-items: center; height: 100vh;'><h1>helper backend</h1></div>"
    )


@csrf_exempt
def signup(request):
    resp = request.POST
    print(resp)
    user = User.objects.create_user(
        username=resp["username"],
        email=resp["email"],
        password=resp["password"],
    )
    user.last_name = resp["lastname"]
    user.first_name = resp["firstname"]
    user.save()
    return JsonResponse({"message": "Signup page"})
