from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    avatar = models.CharField(("avatar"), max_length=128)


class TutorialField(models.Model):
    label = models.CharField(("label"), max_length=128)
    thumbnail = models.CharField(("thumbnail"), max_length=128)
    description = models.CharField(("description"), max_length=128)


class Chapiter(models.Model):
    label = models.CharField(("label"), max_length=128)
    thumbnail = models.CharField(("thumbnail"), max_length=128)
    content = models.TextField()
    chapiterNumber = models.IntegerField()
    nextChapiter = models.IntegerField(blank=True, null=True)
    previewChapiter = models.IntegerField(blank=True, null=True)
    tutorialField = models.ForeignKey(TutorialField, on_delete=models.CASCADE)
