from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import BlogPost, PostContent


def blog_posts(request):
    try:
        blogPosts = BlogPost.objects.all()
        blogPostsDict = {}
        i = 0
        for post in blogPosts:
            blogPostsDict[i] = {
                "label": post.label,
                "thumbnail": post.thumbnail,
                "description": post.description,
            }
            i += 1
        return JsonResponse(blogPostsDict)
    except:
        return HttpResponse(-1)


def post_content(request, title):
    try:
        blogPostTitle = " ".join(title.split("_"))
        blogPost = BlogPost.objects.get(label=blogPostTitle)
        postContent = PostContent.objects.get(blogPost=blogPost)
        postContentDict = {}
        postContentDict["content"] = postContent.content
        postContentDict["nextPost"] = postContent.nextPost
        postContentDict["previewPost"] = postContent.previewPost
        postContentDict["postTitle"] = postContent.blogPost.label
        return JsonResponse(postContentDict)
    except:
        return HttpResponse(-1)
