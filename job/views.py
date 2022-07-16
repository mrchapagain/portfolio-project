from django.shortcuts import render, get_object_or_404
from .models import Job
from blog.models import Blog
#from plotly.offline import plot
# in the template {% outoscape off%} & {% endautoscape %}

# Create your views here.
def  home(request):
    jobs= Job.objects
    blogs= Blog.objects
    return render(request, 'job/home.html', {'jobs': jobs, 'blogs': blogs})

def  alljobs(request):
    jobs= Job.objects
    return render(request, 'job/alljobs.html', {'jobs': jobs})

def jobdetail(request, job_id):
    detailjob = get_object_or_404(Job, pk=job_id)
    return render(request, 'job/jobdetail.html', {'job': detailjob})