from django.contrib import admin
from .models import CustomUser
from helper_backend.tutorial.models import TutorialField, Chapiter
from helper_backend.blog.models import BlogPost, PostContent

admin.site.register(CustomUser)
admin.site.register(TutorialField)
admin.site.register(Chapiter)
admin.site.register(BlogPost)
admin.site.register(PostContent)
