from django.shortcuts import render
from .datavis import *
from .models import Googledf, Country_Name, Massage, Trendskeyword,  Category, TimeFrame, SearchType


def keyword_tosearch(request):
    kw_choosen= request.POST['key_words']
    #Lets take the data that stored in databased through model
    data_objects = Googledf.objects.all()
    google_data= [data.df for data in data_objects][0]
    
    return render(request, 'fooddata/allfooddatas.html', {'kw_choosen':kw_choosen})
    

def timeframe_tosearch(request):
    tf_choosen= request.POST['time_frame']
    #Lets take the data that stored in databased through model
    data_objects = Googledf.objects.all()
    google_data= [data.df for data in data_objects][0]
  

    #massage to display as analytics
    massages_obj= Massage.objects.all()
    massage= [body.massage for body in massages_obj if body.title == tf_choosen][0]

    return render(request, 'fooddata/allfooddatas.html', {'tf_choosen':tf_choosen, 'massage':massage})


def allfooddatas(request):
    data_objects = Googledf.objects.all()
    google_data= [data.df for data in data_objects][0]

    keyword_dict= Trendskeyword.objects.all()
    pn_dict = Country_Name.objects.all()
    cat_dict = Category.objects.all()
    tf_dict = TimeFrame.objects.all()
    st_dict = SearchType.objects.all()
    #Lets initiate the class that has been defined in datavis page       

    return render(request, 'fooddata/allfooddatas.html', {"keyword_dict":keyword_dict, "pn_dict":pn_dict, "cat_dict":cat_dict, "tf_dict":tf_dict, "st_dict":st_dict}) 
    #'item_foodinfo': item_foodinfo, 'namechoosen_foodplots': namechoosen_foodplots 