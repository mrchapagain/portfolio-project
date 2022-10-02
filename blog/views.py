from django.shortcuts import render, get_object_or_404

from .models import Blog

# Create your views here.

def allblogs(request):
    blogs= Blog.objects.all()
    #detailblog = get_object_or_404(Blog, pk=blog_id)
    sample_blog= [blog for blog in blogs if blog.title == "blog check"]
    return render(request, 'blog/allblogs.html', {'blogs': blogs, "sample_blog":sample_blog})

def detail(request, blog_id):
    blogs= Blog.objects
    detailblog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blogs': blogs, 'blog': detailblog})

