from django.shortcuts import render
from .models import AboutMe

# Create your views here.
def  alldocs(request):
    docs= AboutMe.objects
    return render(request, 'aboutme/alldocs.html', {'docs': docs})