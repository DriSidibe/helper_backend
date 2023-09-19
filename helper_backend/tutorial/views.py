from .models import TutorialField, Chapiter
from django.http import HttpResponse, JsonResponse


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
