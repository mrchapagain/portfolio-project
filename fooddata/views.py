from django.shortcuts import render
from .datavis import *
from .models import Country_Name, Trendskeyword,  TimeFrame


def keyword_tosearch(request):
    kw_choosen= request.POST['key_words']
    #Lets take the data that stored in databased through model
    keyword_dict= Trendskeyword.objects.all()

    
    return render(request, 'fooddata/allfooddatas.html', {'kw_choosen':kw_choosen, "keyword_dict":keyword_dict})
    

def timeframe_tosearch(request):
    tf_choosen= request.POST['time_frame']
    #Lets take the data that stored in databased through model
    pn_dict = Country_Name.objects.all()
    tf_dict = TimeFrame.objects.all()
 
    return render(request, 'fooddata/allfooddatas.html', {'tf_choosen':tf_choosen, 'pn_dict':pn_dict, "tf_dict":tf_dict})


def allfooddatas(request):

    keyword_dict= Trendskeyword.objects.all()
    pn_dict = Country_Name.objects.all()
    tf_dict = TimeFrame.objects.all()
    
    st_dict = {"":""}
    cat_dict = { "":""}


    return render(request, 'fooddata/allfooddatas.html', {"keyword_dict":keyword_dict, "pn_dict":pn_dict, "tf_dict":tf_dict, "st_dict":st_dict, "cat_dict":cat_dict}) 