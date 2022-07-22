from django.shortcuts import render, get_object_or_404
from .models import Job, Google
from blog.models import Blog

# Create your views here.
def  home(request):
    jobs= Job.objects
    blogs= Blog.objects
    return render(request, 'job/home.html', {'jobs': jobs, 'blogs': blogs})

def  alljobs(request):
    jobs= Job.objects
    googles= Google.objects
    return render(request, 'job/alljobs.html', {'jobs': jobs, 'googles':googles})

def jobdetail(request, job_id):
    detailjob = get_object_or_404(Job, pk=job_id)
    return render(request, 'job/jobdetail.html', {'job': detailjob})