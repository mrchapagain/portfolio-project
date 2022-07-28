from django.shortcuts import render, redirect, get_object_or_404
from .datavis import *
from .models import Climatedf, Foodinput, Massage

#from .data import *
#import glob
#from openpyxl import load_workbook

def itm_tosearch(request):
    name_choosen= request.POST['itm_name']
    #Lets take the data that stored in databased through model
    data_objects = Climatedf.objects.all()
    climate_data= [data.df for data in data_objects][0]

    cls= FoodCo2Analytics()

    #Lets use function to read data
    allfooddatas= cls.datareader(climate_data).sort_values(by=['Total_CO2_eq_perkg'], ascending=False).round(decimals = 2)
    #name_choosen= allfooddatas.sample().reset_index(drop=True)
    choosen_item_data= allfooddatas.loc[allfooddatas['Product_en']== name_choosen].reset_index(drop=True)

    # CO2 Pie-chart of the single item choosen (name_choosen)
    co2_foodplots_item= cls.piechart_fooditem_co2(choosen_item_data)
    # Energy Pie-chart of the single item choosen (name_choosen)
    energy_foodplots_item= cls.piechart_fooditem_energy(choosen_item_data)

    # Rows of the 5 higest and 5 least CO2 contributor
    top10_fooddatas= allfooddatas.tail(5).append(allfooddatas.head(5))

    # list offood-item
    food_pair= allfooddatas[['Category_en', 'Product_en']].to_dict('record')
    food_cat_list= ['Meat/poultry', 'Seafood', 'Oils/fats edible', 'Candy/sugar products', 'Prepared/preserved foods', 'Seasonings/preservatives/extracts', 'Milk/eggs/substitute products', 'Beverages', 'Bread/bakery products', 'Fruit/vegetable products', 'Cereal/grain/pulse products', 'Fruits', 'Vegetables']
    
    return render(request, 'fooddata/allfooddatas.html', {'food_pair':food_pair, 'food_cat_list':food_cat_list, 'name_choosen':name_choosen, 'co2_foodplots_item':co2_foodplots_item, 'energy_foodplots_item':energy_foodplots_item, 'choosen_item_data':choosen_item_data, 'top10_fooddatas':top10_fooddatas})
    

def cat_tosearch(request):
    category_choosen= request.POST['cat_name']
    #Lets take the data that stored in databased through model
    data_objects = Climatedf.objects.all()
    climate_data= [data.df for data in data_objects][0]
  
    #Lets initiate the class that has been defined in datavis page
    cls= FoodCo2Analytics()
    #Lets use function to read data
    allfooddatas= cls.datareader(climate_data).sort_values(by=['Total_CO2_eq_perkg'], ascending=False).round(decimals = 2)

    # Rows of the 5 higest and 5 least CO2 contributor
    top10_fooddatas= allfooddatas.tail(5).append(allfooddatas.head(5))
    
    # dataframe grouped as per category
    df_with_category= allfooddatas[['Category_en', 'Agriculture', 'iLUC', 'Processing', 'Packaging',	'Transport',	'Retail', 'Total_CO2_eq_perkg']].groupby(by= ['Category_en'], sort=True).mean().sort_values(by=['Total_CO2_eq_perkg'], ascending=False).round(decimals = 2)
    choosen_category_data= df_with_category.loc[df_with_category.index== category_choosen].reset_index(drop=True)

    # CO2 Pie-chart of the single item choosen (name_choosen)
    co2_category_piechart= cls.piechart_fooditem_co2(choosen_category_data)

    food_cat_list= ['Meat/poultry', 'Seafood', 'Oils/fats edible', 'Candy/sugar products', 'Prepared/preserved foods', 'Seasonings/preservatives/extracts', 'Milk/eggs/substitute products', 'Beverages', 'Bread/bakery products', 'Fruit/vegetable products', 'Cereal/grain/pulse products', 'Fruits', 'Vegetables']
    food_pair= allfooddatas[['Category_en', 'Product_en']].to_dict('record')

    #massage to display as analytics
    massages_obj= Massage.objects.all()
    massage= [body.massage for body in massages_obj if body.title == category_choosen][0]

    return render(request, 'fooddata/allfooddatas.html', {'food_cat_list':food_cat_list, 'food_pair':food_pair, 'category_choosen':category_choosen, 'co2_category_piechart':co2_category_piechart, 'massage':massage, 'top10_fooddatas':top10_fooddatas})


def allfooddatas(request):
    data_objects = Climatedf.objects.all()
    climate_data= [data.df for data in data_objects][0]
    #Lets initiate the class that has been defined in datavis page       

    cls= FoodCo2Analytics()
    #Lets use function to read data
    allfooddatas= cls.datareader(climate_data).sort_values(by=['Total_CO2_eq_perkg'], ascending=False).round(decimals = 2)

    # Rows of the 5 higest and 5 least CO2 contributor
    top10_fooddatas= allfooddatas.tail(5).append(allfooddatas.head(5))

    #Lets use the function to display graph of data with categor grupped
    co2_foodplots_category= cls.co2_data_plot(allfooddatas)

    # Lets use function to display detail food info of indivisual item
        
    food_pair= allfooddatas[['Category_en', 'Product_en']].to_dict('record')
    
    food_cat_list= ['Meat/poultry', 'Seafood', 'Oils/fats edible', 'Candy/sugar products', 'Prepared/preserved foods', 'Seasonings/preservatives/extracts', 'Milk/eggs/substitute products', 'Beverages', 'Bread/bakery products', 'Fruit/vegetable products', 'Cereal/grain/pulse products', 'Fruits', 'Vegetables']

    return render(request, 'fooddata/allfooddatas.html', {'allfooddatas': allfooddatas, 'top10_fooddatas': top10_fooddatas, 'food_pair':food_pair, 'co2_foodplots_category':co2_foodplots_category, 'food_cat_list':food_cat_list}) 
    #'item_foodinfo': item_foodinfo, 'namechoosen_foodplots': namechoosen_foodplots 