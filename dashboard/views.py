from django.shortcuts import render, redirect, get_object_or_404
#from .datavis import *
from .models import Dataset, Category


def item_todisplay(request):
    df= Dataset.objects.all()
    return render(request, 'dashboard/alldashboards.html', {'df': df})
    