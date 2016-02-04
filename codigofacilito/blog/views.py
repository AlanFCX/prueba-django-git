from django.shortcuts import render
from blog.models import BlogPost

# Create your views here.

def archive(request):
    posts = BlogPost.objects.all()
    context = {"posts":posts}
    return render(request, "archive.html",context)