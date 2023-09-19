"""
URL configuration for helper_backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from helper.views import signin, signup, home
from tutorial.views import (
    tutorials,
    tutorials_by_field_and_chapiters,
    tutorials_chapiters,
    tutorials_chapiters_by_number,
)
from blog.views import blog_posts, post_content


urlpatterns = [
    path("admin/", admin.site.urls),
    path("signup/", signup),
    path("signin/", signin),
    path("tutorials/", tutorials),
    path("tutorials/<str:tutorialTitle>/chapiters/", tutorials_chapiters),
    path("tutorials/chapiters/<str:number>", tutorials_chapiters_by_number),
    path("tutorials/<str:field>/<str:chapiter>", tutorials_by_field_and_chapiters),
    # ----------------------------------
    path("blogposts/", blog_posts),
    path("postcontent/<str:title>", post_content),
    path("", home),
]
