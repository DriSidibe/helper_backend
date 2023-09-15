from django.contrib import admin
from .models import CustomUser, TutorialField, Chapiter

admin.site.register(CustomUser)
admin.site.register(TutorialField)
admin.site.register(Chapiter)
