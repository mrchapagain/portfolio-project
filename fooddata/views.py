from django.shortcuts import render, redirect, get_object_or_404
from .datavis import *
#from job.models import Job
#from blog.models import Blog
from .data import *

import glob
from openpyxl import load_workbook

# Create your views here.

def allfooddatas(request):
    #filename = r"https://github.com/mrchapagain/FoodClimateAnalytics/raw/main/ClimateData.xlsx" #r'./ClimateData.xlsx'
    #data_link = load_workbook(filename)
    #path= "static/"
    data_link = "https://github.com/mrchapagain/FoodClimateAnalytics/raw/main/ClimateData.xlsx" # glob.glob(path + '*.xlsx')
    fooddatas= datareader(data_link)

    plots= data_plot(fooddatas)
    foodinfo= selected_foodinfo(fooddatas)

    return render(request, 'fooddata/allfooddatas.html', {'fooddatas': fooddatas, 'plots': plots, 'foodinfo': foodinfo})