from django.shortcuts import render, redirect, get_object_or_404
from .datavis import *
from .models import Climatedf, Foodinput

#from .data import *
#import glob
#from openpyxl import load_workbook

def itm_tosearch(request):
    name_choosen= request.POST['itm_name']

    #Lets initiate the class that has been defined in datavis page
    data_link = "https://github.com/mrchapagain/FoodClimateAnalytics/raw/main/ClimateData.xlsx" # glob.glob(path + '*.xlsx')
    cls= FoodCo2Analytics()
    #Lets use function to read data
    allfooddatas= cls.datareader(data_link).sort_values(by=['Total_CO2_eq_perkg'], ascending=False).round(decimals = 2)
    name_choosen= allfooddatas.sample().reset_index(drop=True)

    # CO2 Pie-chart of the single item choosen (name_choosen)
    co2_foodplots_item= cls.piechart_fooditem_co2(name_choosen)
    # Energy Pie-chart of the single item choosen (name_choosen)
    energy_foodplots_item= cls.piechart_fooditem_energy(name_choosen)
    return render(request, 'fooddata/allfooddatas.html', {'name_choosen':name_choosen, 'co2_foodplots_item':co2_foodplots_item, 'energy_foodplots_item':energy_foodplots_item})
    

def cat_tosearch(request):
    category_choosen= request.POST['cat_name']

    #Lets initiate the class that has been defined in datavis page
    data_link = "https://github.com/mrchapagain/FoodClimateAnalytics/raw/main/ClimateData.xlsx" # glob.glob(path + '*.xlsx')
    cls= FoodCo2Analytics()
    #Lets use function to read data
    allfooddatas= cls.datareader(data_link).sort_values(by=['Total_CO2_eq_perkg'], ascending=False).round(decimals = 2)
    #Lets use the function to display graph of data with categor grupped
    co2_foodplots_category= cls.co2_data_plot(allfooddatas)

    return render(request, 'fooddata/allfooddatas.html', {'category_choosen':category_choosen, 'co2_foodplots_category':co2_foodplots_category})


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
        
    food_pair= allfooddatas[['Category_en', 'Product_en']].to_dict('record')

    
    food_cat_list= ['Meat/poultry', 'Seafood', 'Oils/fats edible', 'Candy/sugar products', 'Prepared/preserved foods', 'Seasonings/preservatives/extracts', 
    'Milk/eggs/substitute products', 'Beverages', 'Bread/bakery products', 'Fruit/vegetable products', 'Cereal/grain/pulse products', 'Fruits', 'Vegetables']

    #food_cat_list= allfooddatas[['Category_en', 'Agriculture', 'iLUC', 'Processing', 'Packaging', 'Transport', 'Retail', 'Total_CO2_eq/kg']].groupby(by= ['Category_en'], sort=True).mean().sort_values(by=['Total_CO2_eq/kg'], ascending=False).round(decimals = 2).index.tolist()

    return render(request, 'fooddata/allfooddatas.html', {'allfooddatas': allfooddatas, 'top10_fooddatas': top10_fooddatas, 'food_pair':food_pair}) 
    #'item_foodinfo': item_foodinfo, 'namechoosen_foodplots': namechoosen_foodplots 