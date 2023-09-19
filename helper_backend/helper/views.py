from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from helper.models import CustomUser


def home(request):
    return HttpResponse(
        "<div style='display: flex; justify-content: center; align-items: center; height: 100vh;'><h1>helper backend</h1></div>"
    )


@csrf_exempt
def signup(request):
    response_good = HttpResponse(0)
    response_bad = HttpResponse(1)
    response_very_bad = HttpResponse(-1)
    try:
        resp = request.POST
        try:
            user1 = CustomUser.objects.get(username=resp["username"])
        except:
            user1 = None
            try:
                user2 = CustomUser.objects.get(email=resp["email"])
            except:
                user2 = None
        if (user1) or (user2):
            return response_bad
        else:
            user = CustomUser.objects.create_user(
                username=resp["username"],
                email=resp["email"],
                password=resp["password"],
                avatar=resp["avatar"],
            )
            user.last_name = resp["lastname"]
            user.first_name = resp["firstname"]
            user.save()
            user = authenticate(username=resp["username"], password=resp["password"])
            if user is not None:
                return response_good
            else:
                return response_very_bad
    except Exception as e:
        return response_very_bad


@csrf_exempt
def signin(request):
    try:
        resp = request.POST
        try:
            user = authenticate(username=resp["username"], password=resp["password"])
        except:
            user = None
        if user:
            user = CustomUser.objects.get(username=resp["username"])
            return JsonResponse({"status": 0, "avatar": user.avatar})
        else:
            return HttpResponse(1)
    except Exception as e:
        print(e)
        return HttpResponse(-1)
