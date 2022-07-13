from django.shortcuts import render, redirect, get_object_or_404
from .datavis import *
from .data import *

import glob
from openpyxl import load_workbook

# Create your views here.

def allfooddatas(request):
    #Lets use function to read data
    data_link = "https://github.com/mrchapagain/FoodClimateAnalytics/raw/main/ClimateData.xlsx" # glob.glob(path + '*.xlsx')
    allfooddatas= datareader(data_link).sort_values(by=['Total_CO2_eq/kg'], ascending=False).round(decimals = 2)

    # Rows of the 5 higest and 5 least CO2 contributor
    top10_fooddatas= allfooddatas.tail(5).append(allfooddatas.head(5))

    #Lets use the function to display graph of data with categor grupped
    co2_foodplots= co2_data_plot(allfooddatas)

    # Lets use function to display detail food info of indivisual item
    item_foodinfo= print(selected_foodinfo(allfooddatas))

    return render(request, 'fooddata/allfooddatas.html', {'top10_fooddatas': top10_fooddatas, 'co2_foodplots': co2_foodplots, 'item_foodinfo': item_foodinfo})