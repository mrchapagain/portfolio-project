from django.shortcuts import render, get_object_or_404
from .models import AboutMe, MyCv

# Create your views here.
def  alldocs(request):
    aboutmes= AboutMe.objects
    return render(request, 'aboutme/alldocs.html', {'aboutmes': aboutmes})

def docdetail(request, aboutme_id):
    detaildoc= get_object_or_404(AboutMe, pk=aboutme_id)
    return render(request, 'aboutme/docdetail.html', {'aboutme': detaildoc})

def cv_certificate_display(request):
    mydocs= MyCv.objects
    
    return render(request, 'aboutme/alldocs.html', {'mydocs': mydocs})
