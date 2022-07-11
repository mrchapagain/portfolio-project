from django.shortcuts import render, redirect, get_object_or_404
#from .apiauth import *
#from .classifier import *
#from job.models import Job
from blog.models import Blog

# Create your views here.

def allfooddatas(request):
    fooddatas= Blog.objects
    return render(request, 'fooddata/allfooddatas.html', {'fooddatas': fooddatas})