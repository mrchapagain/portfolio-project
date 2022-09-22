from django.shortcuts import render, redirect, get_object_or_404
from .logic import *
from .models import Dataset, Category

def Food_category(request):
    category= request.POST['food_cat']

    data_frida_final= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/finaldf_fridanutrient_aditionallink_groups.xlsx"
    cls= FridaDataAnalytics()
    df= cls.frida_datareader(data_frida_final)
    df_category= cls.df_FødevareGruppe(df, category)
    food_group_list= cls.FødevareGruppe_list(df)

    name_list=df_category.FødevareNavn.to_list()
    barplot_foodwate= cls.foodwaste_portion_barplot(df, 65, category)
    
    return render(request, 'dashboard/alldashboards.html', {"category":category, "df_category":df_category, "name_list":name_list, "food_group_list":food_group_list, "barplot_foodwate":barplot_foodwate})


def foodname_todf(request):
    foodname= request.POST['food_name']

    data_frida_final= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/finaldf_fridanutrient_aditionallink_groups.xlsx"
    data_climate_selected= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/df_climate_selected.xlsx"
    
    cls= FridaDataAnalytics()
    df= cls.frida_datareader(data_frida_final)
    df_climate= cls.frida_datareader(data_climate_selected)
    
    food_group_list= cls.FødevareGruppe_list(df)
    df_food_name= cls.df_FødevareNavn(df, foodname)

    cat=df_food_name.FødevareGruppe.item()
    name_list=df[df.FødevareGruppe == cat].FødevareNavn.to_list()

    pie_chart_energy= cls.piechart_fooditem_energy(df_food_name)

    df_foodname_climate= df_climate[df_climate.Product_dk== foodname]
    pie_chart_climate= cls.piechart_fooditem_co2(df_foodname_climate)

    group_plot_climate= cls.co2_data_plot(df_climate)
    barplot_climate_comparision=cls.comparision_barplot_climate(df_climate, foodname)

    return render(request, 'dashboard/alldashboards.html', {"foodname":foodname, "df_food_name":df_food_name, "food_group_list":food_group_list, "name_list":name_list, "pie_chart_energy":pie_chart_energy, "pie_chart_climate":pie_chart_climate, "group_plot_climate":group_plot_climate, "barplot_climate_comparision":barplot_climate_comparision})


def item_todisplay(request):
    data_frida_final= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/finaldf_fridanutrient_aditionallink_groups.xlsx"
    
    cls= FridaDataAnalytics()
    df= cls.frida_datareader(data_frida_final)
    food_name_list= cls.FødevareNavn_list(df)
    food_group_list= cls.FødevareGruppe_list(df)
    df_group_name_dict= cls.FødevareGruppe_FødevareNavn_dict(df)

    return render(request, 'dashboard/alldashboards.html', {"food_name_list":food_name_list, "food_group_list":food_group_list, "df_group_name_dict":df_group_name_dict})
    