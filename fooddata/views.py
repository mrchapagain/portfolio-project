from django.shortcuts import render, redirect, get_object_or_404
from .datavis import *
from .models import Climatedf, Foodinput, Massage


def itm_tosearch(request):
    name_choosen= request.POST['itm_name']
    #Lets take the data that stored in databased through model
    data_objects = Climatedf.objects.all()
    climate_data= [data.df for data in data_objects][0]
    
    return render(request, 'fooddata/allfooddatas.html', {'name_choosen':name_choosen})
    

def cat_tosearch(request):
    category_choosen= request.POST['cat_name']
    #Lets take the data that stored in databased through model
    data_objects = Climatedf.objects.all()
    climate_data= [data.df for data in data_objects][0]
  

    #massage to display as analytics
    massages_obj= Massage.objects.all()
    massage= [body.massage for body in massages_obj if body.title == category_choosen][0]

    return render(request, 'fooddata/allfooddatas.html', {'category_choosen':category_choosen, 'massage':massage})


def allfooddatas(request):
    data_objects = Climatedf.objects.all()
    climate_data= [data.df for data in data_objects][0]
    #Lets initiate the class that has been defined in datavis page       

    return render(request, 'fooddata/allfooddatas.html', {}) 
    #'item_foodinfo': item_foodinfo, 'namechoosen_foodplots': namechoosen_foodplots 