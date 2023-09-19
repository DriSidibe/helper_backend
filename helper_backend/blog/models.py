from django.db import models


class BlogPost(models.Model):
    label = models.CharField(("label"), max_length=128)
    thumbnail = models.CharField(("thumbnail"), max_length=128, blank=True, null=True)
    description = models.CharField(("description"), max_length=128)


class PostContent(models.Model):
    content = models.TextField()
    nextPost = models.CharField(("nextPost"), max_length=128, blank=True, null=True)
    previewPost = models.CharField(
        ("previewPost"), max_length=128, blank=True, null=True
    )
    blogPost = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
