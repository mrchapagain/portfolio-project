from django.shortcuts import render, get_object_or_404
from .models import Analytics

# Create your views here.
def  allanalytics(request):
    analyticss= Analytics.objects
    return render(request, 'analytics/allanalytics.html', {'analyticss': analyticss})

def analyticsdetail(request, analytics_id):
    detailanalytics= get_object_or_404(Analytics, pk=analytics_id)
    return render(request, 'aboutme/analyticsdetail.html', {'analytics': detailanalytics})