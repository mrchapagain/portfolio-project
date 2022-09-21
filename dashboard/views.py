from django.shortcuts import render, redirect, get_object_or_404
from .logic import *
from .models import Dataset, Category

def Food_category(request):
    category= request.POST['food_cat']

    data_frida_final= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/finaldf_fridanutrient_aditionallink_groups.xlsx"
    cls= FridaDataAnalytics()
    df= cls.frida_datareader(data_frida_final)
    df_category= cls.df_FødevareGruppe(df, category)
    name_list=df_category.FødevareNavn.to_list()

    return render(request, 'dashboard/alldashboards.html', {"category":category, "df":df, "df_category":df_category, "name_list":name_list})


def foodname_todf(request):
    foodname= request.POST['food_name']

    data_frida_final= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/finaldf_fridanutrient_aditionallink_groups.xlsx"
    cls= FridaDataAnalytics()
    df= cls.frida_datareader(data_frida_final)
    df_food_name= cls.df_FødevareNavn(df, foodname)

    return render(request, 'dashboard/alldashboards.html', {"foodname":foodname, "df_food_name":df_food_name})


def item_todisplay(request):
    data_frida_final= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/finaldf_fridanutrient_aditionallink_groups.xlsx"
    
    #category_chosen= request.POST['food_cat']
    
    cls= FridaDataAnalytics()
    df= cls.frida_datareader(data_frida_final)
    df_name_list= cls.FødevareNavn_list(df)
    df_group_list= cls.FødevareGruppe_list(df)
    df_group_name_dict= cls.FødevareGruppe_FødevareNavn_dict(df)

    return render(request, 'dashboard/alldashboards.html', {'df': df, "df_name_list":df_name_list, "df_group_list":df_group_list, "df_group_name_dict":df_group_name_dict})
    