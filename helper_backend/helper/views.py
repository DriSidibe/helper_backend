from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

from helper.models import CustomUser, TutorialField, Chapiter


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


def tutorials(request):
    try:
        tutorials = TutorialField.objects.all()
        tutorialsDict = {}
        i = 0
        for tutorial in tutorials:
            tutorialsDict[i] = {
                "label": tutorial.label,
                "thumbnail": tutorial.thumbnail,
                "description": tutorial.description,
            }
            i += 1
        return JsonResponse(tutorialsDict)
    except:
        return HttpResponse(-1)


def tutorials_chapiters(request, tutorialTitle):
    try:
        tutorial = TutorialField.objects.get(label=tutorialTitle)
        tutorials_chapiters = Chapiter.objects.filter(tutorialField=tutorial)
        print(tutorials_chapiters)
        tutorialsChapitersDict = {}
        i = 0
        try:
            for chapiter in tutorials_chapiters:
                tutorialsChapitersDict[i] = {
                    "label": chapiter.label,
                    "thumbnail": chapiter.thumbnail,
                    "content": chapiter.content,
                    "chapiterNumber": chapiter.chapiterNumber,
                    "nextChapiter": chapiter.nextChapiter,
                    "previewChapiter": chapiter.previewChapiter,
                }
                i += 1
        except:
            tutorialsChapitersDict[i] = {
                "label": tutorials_chapiters.label,
                "thumbnail": tutorials_chapiters.thumbnail,
                "content": tutorials_chapiters.content,
                "chapiterNumber": tutorials_chapiters.chapiterNumber,
                "nextChapiter": tutorials_chapiters.nextChapiter,
                "previewChapiter": tutorials_chapiters.previewChapiter,
            }
        return JsonResponse(tutorialsChapitersDict)
    except:
        return HttpResponse(-1)


def tutorials_chapiters_by_number(request, number):
    try:
        chapiter = Chapiter.objects.get(chapiterNumber=number)
        chapiterDict = {}
        chapiterDict["label"] = chapiter.label
        chapiterDict["thumbnail"] = chapiter.thumbnail
        chapiterDict["content"] = chapiter.content
        chapiterDict["chapiterNumber"] = chapiter.chapiterNumber
        chapiterDict["nextChapiter"] = chapiter.nextChapiter
        chapiterDict["previewChapiter"] = chapiter.previewChapiter
        return JsonResponse(chapiterDict)
    except:
        return HttpResponse(-1)


def tutorials_by_field_and_chapiters(request, field, chapiter):
    try:
        chapiter = " ".join(chapiter.split("_"))
        tutorial = TutorialField.objects.get(label=field)
        chapiter = Chapiter.objects.get(tutorialField=tutorial, label=chapiter)
        chapiterDict = {}
        chapiterDict["label"] = chapiter.label
        chapiterDict["thumbnail"] = chapiter.thumbnail
        chapiterDict["content"] = chapiter.content
        chapiterDict["chapiterNumber"] = chapiter.chapiterNumber
        chapiterDict["nextChapiter"] = chapiter.nextChapiter
        chapiterDict["previewChapiter"] = chapiter.previewChapiter
        return JsonResponse(chapiterDict)
    except:
        return HttpResponse(-1)
