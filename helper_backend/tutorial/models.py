from django.db import models
import uuid


class TutorialField(models.Model):
    label = models.CharField(("label"), max_length=128)
    thumbnail = models.CharField(("thumbnail"), max_length=128, blank=True, null=True)
    description = models.CharField(("description"), max_length=128)


class Chapiter(models.Model):
    label = models.CharField(("label"), max_length=128)
    thumbnail = models.CharField(("thumbnail"), max_length=128, blank=True, null=True)
    content = models.TextField()
    chapiterNumber = models.CharField(
        editable=False, default=uuid.uuid4(), max_length=255
    )
    nextChapiter = models.CharField(
        ("nextChapiter"), max_length=128, blank=True, null=True
    )
    previewChapiter = models.CharField(
        ("previewChapiter"), max_length=128, blank=True, null=True
    )
    tutorialField = models.ForeignKey(TutorialField, on_delete=models.CASCADE)
