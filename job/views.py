from django.shortcuts import render, get_object_or_404
from .models import Job, Google, Tweet, Climate, Health, Ontology
from blog.models import Blog


# Create your views here.
def  home(request):
    jobs= Job.objects
    blogs= Blog.objects
    googles= Google.objects
    tweets=Tweet.objects
    climates=Climate.objects
    healths=Health.objects
    ontologys=Ontology.objects

    return render(request, 'job/home.html', {'jobs': jobs, 'blogs': blogs, 'googles':googles, 'tweets':tweets, 'climates':climates, 'healths':healths, 'ontologys':ontologys})

def  alljobs(request):
    jobs= Job.objects
    googles= Google.objects
    tweets=Tweet.objects
    climates=Climate.objects
    healths=Health.objects
    ontologys=Ontology.objects
    return render(request, 'job/alljobs.html', {'jobs': jobs, 'googles':googles, 'tweets':tweets, 'climates':climates, 'healths':healths, 'ontologys':ontologys})

def jobdetail(request, job_id):
    detailjob = get_object_or_404(Job, pk=job_id)
    return render(request, 'job/jobdetail.html', {'job': detailjob})