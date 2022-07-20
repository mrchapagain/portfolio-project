from django.shortcuts import render, redirect, get_object_or_404
from .datavis import *

#from .data import *
#import glob
#from openpyxl import load_workbook

def itm_tosearch(request):
    return render(request, 'fooddata/allfooddatas.html')
    

def cat_tosearch(request):
    return render(request, 'fooddata/allfooddatas.html')

def allfooddatas(request):
    #Lets initiate the class that has been defined in datavis page
    data_link = "https://github.com/mrchapagain/FoodClimateAnalytics/raw/main/ClimateData.xlsx" # glob.glob(path + '*.xlsx')
    cls= FoodCo2Analytics()
    
    #Lets use function to read data
    allfooddatas= cls.datareader(data_link).sort_values(by=['Total_CO2_eq_perkg'], ascending=False).round(decimals = 2)

    # Rows of the 5 higest and 5 least CO2 contributor
    top10_fooddatas= allfooddatas.tail(5).append(allfooddatas.head(5))

    #Lets use the function to display graph of data with categor grupped
    co2_foodplots_category= cls.co2_data_plot(allfooddatas)

    # Lets use function to display detail food info of indivisual item
    #item_foodinfo= print(selected_foodinfo(allfooddatas))
    df_rows_list= allfooddatas.Product_en.tolist()
    name_choosen =  allfooddatas.sample().reset_index(drop=True)

    # CO2 Pie-chart of the single item choosen (name_choosen)
    co2_foodplots_item= cls.piechart_fooditem_co2(name_choosen)
    
    # Energy Pie-chart of the single item choosen (name_choosen)
    energy_foodplots_item= cls.piechart_fooditem_energy(name_choosen)


    return render(request, 'fooddata/allfooddatas.html', {'allfooddatas': allfooddatas, 'top10_fooddatas': top10_fooddatas, 'df_rows_list': df_rows_list, 
                                'name_choosen':name_choosen, 'co2_foodplots_category': co2_foodplots_category, 'co2_foodplots_item':co2_foodplots_item, 'energy_foodplots_item':energy_foodplots_item}) 
    #'item_foodinfo': item_foodinfo, 'namechoosen_foodplots': namechoosen_foodplots 