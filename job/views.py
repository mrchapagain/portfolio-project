from django.shortcuts import render
from .models import Job

# Create your views here.
def  home(request):
    jobs= Job.objects
    return render(request, 'job/home.html', {'jobs': jobs})

def  alljobs(request):
    jobs= Job.objects
    return render(request, 'job/alljobs.html', {'jobs': jobs})

