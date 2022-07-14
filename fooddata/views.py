from django.shortcuts import render, redirect, get_object_or_404
from .datavis import *
#from .data import *

import glob
from openpyxl import load_workbook
#from itables import init_notebook_mode
#init_notebook_mode(all_interactive=True)

def allfooddatas(request):
    #Lets initiate the class that has been defined in datavis page
    data_link = "https://github.com/mrchapagain/FoodClimateAnalytics/raw/main/ClimateData.xlsx" # glob.glob(path + '*.xlsx')
    cls= FoodCo2Analytics()
    
    #Lets use function to read data
    allfooddatas= cls.datareader(data_link).sort_values(by=['Total_CO2_eq_perkg'], ascending=False).round(decimals = 2)

    # Rows of the 5 higest and 5 least CO2 contributor
    top10_fooddatas= allfooddatas.tail(5).append(allfooddatas.head(5))

    #Lets use the function to display graph of data with categor grupped
    co2_foodplots= cls.co2_data_plot(allfooddatas)

    # Lets use function to display detail food info of indivisual item
    #item_foodinfo= print(selected_foodinfo(allfooddatas))
    df_rows_list= allfooddatas.Product_en.tolist()
    name_choosen =  allfooddatas.sample().reset_index(drop=True)

    return render(request, 'fooddata/allfooddatas.html', {'allfooddatas': allfooddatas, 'top10_fooddatas': top10_fooddatas, 'co2_foodplots': co2_foodplots, 'df_rows_list': df_rows_list, 'name_choosen':name_choosen}) #'item_foodinfo': item_foodinfo