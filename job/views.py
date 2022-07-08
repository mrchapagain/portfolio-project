from django.shortcuts import render
from .models import Job

# Create your views here.
def  home(request):
    jobs= Job.objects
    return render(request, 'job/home.html', {'job': jobs})

def  alljobs(request):
    jobs= Job.objects
    return render(request, 'job/alljobs.html', {'job': jobs})

def jobdetail(request, job_id):
    detailjob = get_object_or_404(Job, pk=job_id)
    return render(request, 'job/jobdetail.html', {'job': detailjob})

