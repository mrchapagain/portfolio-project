from django.shortcuts import render, get_object_or_404
from .models import Portfolios, Google, Tweet, Climate, Health, Ontology
from blog.models import Blog


# Create your views here.
def  home(request):
    portfolioss= Portfolios.objects
    blogs= Blog.objects
    googles= Google.objects
    tweets=Tweet.objects
    climates=Climate.objects
    healths=Health.objects
    ontologys=Ontology.objects

    return render(request, 'portfolios/home.html', {'portfolioss': portfolioss, 'blogs': blogs, 'googles':googles, 'tweets':tweets, 'climates':climates, 'healths':healths, 'ontologys':ontologys})

def  allportfolioss(request):
    portfolioss= Portfolios.objects
    #googles= Google.objects
    #tweets=Tweet.objects
    #climates=Climate.objects
    #healths=Health.objects
    #ontologys=Ontology.objects
    return render(request, 'portfolios/allportfolioss.html', {'portfolioss': portfolioss})

def portfoliosdetail(request, portfolios_id):
    detailportfolios = get_object_or_404(Portfolios, pk=portfolios_id)
    return render(request, 'portfolios/portfoliosdetail.html', {'portfolios': detailportfolios})