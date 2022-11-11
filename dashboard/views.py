from django.shortcuts import render, redirect, get_object_or_404
from .logic import *
from .models import Dataset, Category

def Food_category(request):
    category= request.POST['food_cat']

    data_frida_final= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/finaldf_fridanutrient_aditionallink_groups.xlsx"
    data_climate_selected= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/df_climate_selected.xlsx"

    cls= FridaDataAnalytics()
    df_frida= cls.frida_datareader(data_frida_final)
    df_climate= cls.frida_datareader(data_climate_selected)

    df_frida_category= cls.df_FødevareGruppe(df_frida, category).reset_index(drop=True)

    food_group_list= cls.FødevareGruppe_list(df_frida)
    name_list=df_frida_category.FødevareNavn.to_list()

    barplot_foodwate= cls.foodwaste_portion_barplot(df_frida_category, 0.1, f"{category} category")
    
    loop_range= [num for num in range(40,100,5)]

    #func= cls.list_x_rich(df_frida, "Protein_deklaration_g")
    choices_dict={"Protein rich food-items": ['Gelatine', 'Æg, høne, æggehvide, tørret', 'Flæskesvær, snacks', 'Æg, høne, tørret', 'Skummetmælksost, max. 5+', 'Sojamel','Parmesan, revet', 'Græskarkerner, tørret', 'Sojabønner, tørrede, rå', 'Gær, tørret'],
                "Fiber (Dietry) rich food-items": ['Te, blade', 'Kanel, stang', 'Hyben pulver, tørret', 'Koriander, frø', 'Chiafrø', 'Hvedeklid', 'Fennikel, frø', 'Kommen, rå', 'Karry, pulver', 'Peber, sort'],
                "Fatty-acids rich food-items": ['Tidselolie', 'Hvedekimolie', 'Bomuldsfrøolie', 'Palmeolie', 'Kakaosmør', 'Palmekerneolie', 'Solsikkeolie', 'Valnøddeolie', 'Torsk, levertran', 'Sesamolie'],
                "Carbohydrate rich food-items": ['Sukker, stødt melis (saccharose)', 'Sukker, brunt rørsukker', 'Lactose, pulver', 'Fruktose','Sukker, brun farin', 'Pastiller, sukkerfri, uspec.','Majsmel','Tyggegummi, med sukker, uspec.', 'Sagogryn (kartoffelstivelse)','Majsstivelse']}

    choices_kv= {"Protein_deklaration_g":"Protein rich food-items", "Kostfibre_g":"Fiber (Dietry) rich food-items", "Fedt_total_g":"Fatty-acids rich food-items", "Kulhydrat_deklaration_g":"Carbohydrate rich food-items"}
    
    return render(request, 'dashboard/alldashboards.html', {'choices_kv':choices_kv, 'choices_dict':choices_dict, "category":category, "df_category":df_frida_category, "name_list":name_list, "food_group_list":food_group_list, "barplot_foodwate":barplot_foodwate, "loop_range":loop_range})


def foodname_todf(request):
    foodname= request.POST['food_name']

    data_frida_final= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/finaldf_fridanutrient_aditionallink_groups.xlsx"
    data_climate_selected= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/df_climate_selected.xlsx"
    
    cls= FridaDataAnalytics()
    df_frida= cls.frida_datareader(data_frida_final)
    df_climate= cls.frida_datareader(data_climate_selected)
    
    food_group_list= cls.FødevareGruppe_list(df_frida)
    df_food_name= cls.df_FødevareNavn(df_frida, foodname)

    cat=df_food_name.FødevareGruppe.item()
    name_list=df_frida[df_frida.FødevareGruppe == cat].FødevareNavn.to_list()

    pie_chart_energy= cls.piechart_fooditem_energy(df_food_name)

    df_foodname_climate= df_climate[df_climate.Product_dk== foodname]
    pie_chart_climate= cls.piechart_fooditem_co2(df_foodname_climate)

    science_fact_textdisplay=cls.text_display_frida(df_food_name)
    flavour_img= cls.flavour_compound(foodname)

    #func= cls.list_x_rich(df_frida, "Protein_deklaration_g")
    choices_dict={"Protein rich food-items": ['Gelatine', 'Æg, høne, æggehvide, tørret', 'Flæskesvær, snacks', 'Æg, høne, tørret', 'Skummetmælksost, max. 5+', 'Sojamel','Parmesan, revet', 'Græskarkerner, tørret', 'Sojabønner, tørrede, rå', 'Gær, tørret'],
                "Fiber (Dietry) rich food-items": ['Te, blade', 'Kanel, stang', 'Hyben pulver, tørret', 'Koriander, frø', 'Chiafrø', 'Hvedeklid', 'Fennikel, frø', 'Kommen, rå', 'Karry, pulver', 'Peber, sort'],
                "Fatty-acids rich food-items": ['Tidselolie', 'Hvedekimolie', 'Bomuldsfrøolie', 'Palmeolie', 'Kakaosmør', 'Palmekerneolie', 'Solsikkeolie', 'Valnøddeolie', 'Torsk, levertran', 'Sesamolie'],
                "Carbohydrate rich food-items": ['Sukker, stødt melis (saccharose)', 'Sukker, brunt rørsukker', 'Lactose, pulver', 'Fruktose','Sukker, brun farin', 'Pastiller, sukkerfri, uspec.','Majsmel','Tyggegummi, med sukker, uspec.', 'Sagogryn (kartoffelstivelse)','Majsstivelse']}

    choices_kv= {"Protein_deklaration_g":"Protein rich food-items", "Kostfibre_g":"Fiber (Dietry) rich food-items", "Fedt_total_g":"Fatty-acids rich food-items", "Kulhydrat_deklaration_g":"Carbohydrate rich food-items"}

    return render(request, 'dashboard/alldashboards.html', {'choices_kv':choices_kv, 'choices_dict':choices_dict, "foodname":foodname, "df_food_name":df_food_name, "food_group_list":food_group_list, "name_list":name_list, "pie_chart_energy":pie_chart_energy, "pie_chart_climate":pie_chart_climate, "science_fact_textdisplay": science_fact_textdisplay, "flavour_img":flavour_img})


def item_todisplay(request):

    data_frida_final= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/finaldf_fridanutrient_aditionallink_groups.xlsx"
    data_climate_selected= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/df_climate_selected.xlsx"

      
    cls= FridaDataAnalytics()
    df_frida= cls.frida_datareader(data_frida_final)
    df_climate= cls.frida_datareader(data_climate_selected)

    food_name_list= cls.FødevareNavn_list(df_frida)
    food_group_list= cls.FødevareGruppe_list(df_frida)
    df_group_name_dict= cls.FødevareGruppe_FødevareNavn_dict(df_frida)
    loop_range= [num for num in range(40,100,5)]

    barplot_foodwate= cls.foodwaste_portion_barplot(df_frida, 55, "whole dataset")
    group_plot_climate= cls.co2_data_plot(df_climate)

    #func= cls.list_x_rich(df_frida, "Protein_deklaration_g")
    choices_dict={"Protein rich food-items": ['Gelatine', 'Æg, høne, æggehvide, tørret', 'Flæskesvær, snacks', 'Æg, høne, tørret', 'Skummetmælksost, max. 5+', 'Sojamel','Parmesan, revet', 'Græskarkerner, tørret', 'Sojabønner, tørrede, rå', 'Gær, tørret'],
                "Fiber (Dietry) rich food-items": ['Te, blade', 'Kanel, stang', 'Hyben pulver, tørret', 'Koriander, frø', 'Chiafrø', 'Hvedeklid', 'Fennikel, frø', 'Kommen, rå', 'Karry, pulver', 'Peber, sort'],
                "Fatty-acids rich food-items": ['Tidselolie', 'Hvedekimolie', 'Bomuldsfrøolie', 'Palmeolie', 'Kakaosmør', 'Palmekerneolie', 'Solsikkeolie', 'Valnøddeolie', 'Torsk, levertran', 'Sesamolie'],
                "Carbohydrate rich food-items": ['Sukker, stødt melis (saccharose)', 'Sukker, brunt rørsukker', 'Lactose, pulver', 'Fruktose','Sukker, brun farin', 'Pastiller, sukkerfri, uspec.','Majsmel','Tyggegummi, med sukker, uspec.', 'Sagogryn (kartoffelstivelse)','Majsstivelse']}

    choices_kv= {"Protein_deklaration_g":"Protein rich food-items", "Kostfibre_g":"Fiber (Dietry) rich food-items", "Fedt_total_g":"Fatty-acids rich food-items", "Kulhydrat_deklaration_g":"Carbohydrate rich food-items"}

    return render(request, 'dashboard/alldashboards.html', {'choices_kv':choices_kv, 'choices_dict':choices_dict, "food_name_list":food_name_list, "food_group_list":food_group_list, "df_group_name_dict":df_group_name_dict,"loop_range":loop_range, "barplot_foodwate":barplot_foodwate, "group_plot_climate":group_plot_climate})
    


def category_list(request):

    data_frida_final= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/finaldf_fridanutrient_aditionallink_groups.xlsx"
    data_climate_selected= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/df_climate_selected.xlsx"

    cls= FridaDataAnalytics()
    df_frida= cls.frida_datareader(data_frida_final)
    df_climate= cls.frida_datareader(data_climate_selected)

    food_name_list= cls.FødevareNavn_list(df_frida)
    food_group_list= cls.FødevareGruppe_list(df_frida)
    df_group_name_dict= cls.FødevareGruppe_FødevareNavn_dict(df_frida)
    loop_range= [num for num in range(40,100,5)]

    barplot_foodwate= cls.foodwaste_portion_barplot(df_frida, 55, "whole dataset")
    group_plot_climate= cls.co2_data_plot(df_climate)

    #func= cls.list_x_rich(df_frida, "Protein_deklaration_g")
    choices_dict={"Protein rich food-items": ['Gelatine', 'Æg, høne, æggehvide, tørret', 'Flæskesvær, snacks', 'Æg, høne, tørret', 'Skummetmælksost, max. 5+', 'Sojamel','Parmesan, revet', 'Græskarkerner, tørret', 'Sojabønner, tørrede, rå', 'Gær, tørret'],
                "Fiber (Dietry) rich food-items": ['Te, blade', 'Kanel, stang', 'Hyben pulver, tørret', 'Koriander, frø', 'Chiafrø', 'Hvedeklid', 'Fennikel, frø', 'Kommen, rå', 'Karry, pulver', 'Peber, sort'],
                "Fatty-acids rich food-items": ['Tidselolie', 'Hvedekimolie', 'Bomuldsfrøolie', 'Palmeolie', 'Kakaosmør', 'Palmekerneolie', 'Solsikkeolie', 'Valnøddeolie', 'Torsk, levertran', 'Sesamolie'],
                "Carbohydrate rich food-items": ['Sukker, stødt melis (saccharose)', 'Sukker, brunt rørsukker', 'Lactose, pulver', 'Fruktose','Sukker, brun farin', 'Pastiller, sukkerfri, uspec.','Majsmel','Tyggegummi, med sukker, uspec.', 'Sagogryn (kartoffelstivelse)','Majsstivelse']}
   
    choices_kv= {"Protein_deklaration_g":"Protein rich food-items", "Kostfibre_g":"Fiber (Dietry) rich food-items", "Fedt_total_g":"Fatty-acids rich food-items", "Kulhydrat_deklaration_g":"Carbohydrate rich food-items"}

    return render(request, 'dashboard/alldashboards.html', {'choices_kv':choices_kv, 'choices_dict':choices_dict, "food_name_list":food_name_list, "food_group_list":food_group_list, "df_group_name_dict":df_group_name_dict,"loop_range":loop_range, "barplot_foodwate":barplot_foodwate, "group_plot_climate":group_plot_climate})
    



def xrich_todisplay(request):
    xrich_option= request.POST['x_riches_cat']

    data_frida_final= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/finaldf_fridanutrient_aditionallink_groups.xlsx"

    cls= FridaDataAnalytics()
    df_frida= cls.frida_datareader(data_frida_final)

    food_group_list= cls.FødevareGruppe_list(df_frida)
    food_name_list= cls.FødevareNavn_list(df_frida)

    #func= cls.list_x_rich(df_frida, "Protein_deklaration_g")
    choices_dict={"Protein rich food-items": ['Gelatine', 'Æg, høne, æggehvide, tørret', 'Flæskesvær, snacks', 'Æg, høne, tørret', 'Skummetmælksost, max. 5+', 'Sojamel','Parmesan, revet', 'Græskarkerner, tørret', 'Sojabønner, tørrede, rå', 'Gær, tørret'],
                "Fiber (Dietry) rich food-items": ['Te, blade', 'Kanel, stang', 'Hyben pulver, tørret', 'Koriander, frø', 'Chiafrø', 'Hvedeklid', 'Fennikel, frø', 'Kommen, rå', 'Karry, pulver', 'Peber, sort'],
                "Fatty-acids rich food-items": ['Tidselolie', 'Hvedekimolie', 'Bomuldsfrøolie', 'Palmeolie', 'Kakaosmør', 'Palmekerneolie', 'Solsikkeolie', 'Valnøddeolie', 'Torsk, levertran', 'Sesamolie'],
                "Carbohydrate rich food-items": ['Sukker, stødt melis (saccharose)', 'Sukker, brunt rørsukker', 'Lactose, pulver', 'Fruktose','Sukker, brun farin', 'Pastiller, sukkerfri, uspec.','Majsmel','Tyggegummi, med sukker, uspec.', 'Sagogryn (kartoffelstivelse)','Majsstivelse']}
    
    choices_kv= {"Protein_deklaration_g":"Protein rich food-items", "Kostfibre_g":"Fiber (Dietry) rich food-items", "Fedt_total_g":"Fatty-acids rich food-items", "Kulhydrat_deklaration_g":"Carbohydrate rich food-items"}

    xrich_choice_df= cls.list_x_rich(df_frida, xrich_option)

    df_title_xrich= f'Data table with Top 20 "{choices_kv[xrich_option]}"'

    return render(request, 'dashboard/alldashboards.html', {'xrich_option':xrich_option, 'food_group_list':food_group_list, 'food_name_list':food_name_list, 'choices_kv':choices_kv, 'xrich_choice_df':xrich_choice_df, 'choices_dict':choices_dict, 'df_title_xrich':df_title_xrich})
    
