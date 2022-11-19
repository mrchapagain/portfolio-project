from django.shortcuts import render, redirect, get_object_or_404
from .logic import *
from .models import Dataset, Category

#for user intractivity
import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual

def Food_category(request):
    category= request.POST['food_cat']
    #data_frida_final= Dataset.objects

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

    choices_kv= {"Protein_deklaration_g":"Protein rich food-items", "Kostfibre_g":"Fiber (Dietry) rich food-items", "Fedt_total_g":"Fatty-acids rich food-items", "Kulhydrat_deklaration_g":"Carbohydrate rich food-items", 'A_vitamin_RE':'A-vitamin rich food-items', "B1-vitamin":'B1-vitamin rich food-items', "B2-vitamin_riboflavin":'B2-vitamin rich food-items', "B6-vitamin":'B6-vitamin rich food-items', "B12-vitamin":'B12-vitamin rich food-items', "C-vitamin":'C-vitamin rich food-items', "D_vitamin_µg":'D-vitamin rich food-items', "E-vitamin":'E-vitamin rich food-items', "Calcium, Ca":'Calcium rich food-items', "Jern, Fe":'Iron rich food-items', 'Kalium, K':'Potassium rich food-items', 'Natrium, Na': 'Sodium rich food-items'}
    
    return render(request, 'dashboard/alldashboards.html', {'choices_kv':choices_kv, 'choices_dict':choices_dict, "category":category, "df_category":df_frida_category, "name_list":name_list, "food_group_list":food_group_list, "barplot_foodwate":barplot_foodwate, "loop_range":loop_range})


def foodname_todf(request):
    foodname= request.POST['food_name']
    #data_frida_final= Dataset.objects

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
    
    flavour_img= cls.flavour_compound(foodname, 'flavor_bitter', 'flavor_sweet', 'flavor_sour', 'flavor_salty', 'flavor_umamy', 'food_name\n with \nflavor_umamy', 'food_name\n with \nflavor_sweet', 'food_name\n with \nflavor_bitter', 'food_name\n with \nflavor_salty')

    #func= cls.list_x_rich(df_frida, "Protein_deklaration_g")
    choices_dict={"Protein rich food-items": ['Gelatine', 'Æg, høne, æggehvide, tørret', 'Flæskesvær, snacks', 'Æg, høne, tørret', 'Skummetmælksost, max. 5+', 'Sojamel','Parmesan, revet', 'Græskarkerner, tørret', 'Sojabønner, tørrede, rå', 'Gær, tørret'],
                "Fiber (Dietry) rich food-items": ['Te, blade', 'Kanel, stang', 'Hyben pulver, tørret', 'Koriander, frø', 'Chiafrø', 'Hvedeklid', 'Fennikel, frø', 'Kommen, rå', 'Karry, pulver', 'Peber, sort'],
                "Fatty-acids rich food-items": ['Tidselolie', 'Hvedekimolie', 'Bomuldsfrøolie', 'Palmeolie', 'Kakaosmør', 'Palmekerneolie', 'Solsikkeolie', 'Valnøddeolie', 'Torsk, levertran', 'Sesamolie'],
                "Carbohydrate rich food-items": ['Sukker, stødt melis (saccharose)', 'Sukker, brunt rørsukker', 'Lactose, pulver', 'Fruktose','Sukker, brun farin', 'Pastiller, sukkerfri, uspec.','Majsmel','Tyggegummi, med sukker, uspec.', 'Sagogryn (kartoffelstivelse)','Majsstivelse']}

    choices_kv= {"Protein_deklaration_g":"Protein rich food-items", "Kostfibre_g":"Fiber (Dietry) rich food-items", "Fedt_total_g":"Fatty-acids rich food-items", "Kulhydrat_deklaration_g":"Carbohydrate rich food-items", 'A_vitamin_RE':'A-vitamin rich food-items', "B1-vitamin":'B1-vitamin rich food-items', "B2-vitamin_riboflavin":'B2-vitamin rich food-items', "B6-vitamin":'B6-vitamin rich food-items', "B12-vitamin":'B12-vitamin rich food-items', "C-vitamin":'C-vitamin rich food-items', "D_vitamin_µg":'D-vitamin rich food-items', "E-vitamin":'E-vitamin rich food-items', "Calcium, Ca":'Calcium rich food-items', "Jern, Fe":'Iron rich food-items', 'Kalium, K':'Potassium rich food-items', 'Natrium, Na': 'Sodium rich food-items'}

    return render(request, 'dashboard/alldashboards.html', {'choices_kv':choices_kv, 'choices_dict':choices_dict, "foodname":foodname, "df_food_name":df_food_name, "food_group_list":food_group_list, "name_list":name_list, "pie_chart_energy":pie_chart_energy, "pie_chart_climate":pie_chart_climate, "science_fact_textdisplay": science_fact_textdisplay, "flavour_img":flavour_img})


def item_todisplay(request):
    #data_frida_final= Dataset.objects.all()

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

    choices_kv= {"Protein_deklaration_g":"Protein rich food-items", "Kostfibre_g":"Fiber (Dietry) rich food-items", "Fedt_total_g":"Fatty-acids rich food-items", "Kulhydrat_deklaration_g":"Carbohydrate rich food-items", 'A_vitamin_RE':'A-vitamin rich food-items', "B1-vitamin":'B1-vitamin rich food-items', "B2-vitamin_riboflavin":'B2-vitamin rich food-items', "B6-vitamin":'B6-vitamin rich food-items', "B12-vitamin":'B12-vitamin rich food-items', "C-vitamin":'C-vitamin rich food-items', "D_vitamin_µg":'D-vitamin rich food-items', "E-vitamin":'E-vitamin rich food-items', "Calcium, Ca":'Calcium rich food-items', "Jern, Fe":'Iron rich food-items', 'Kalium, K':'Potassium rich food-items', 'Natrium, Na': 'Sodium rich food-items'}

    return render(request, 'dashboard/alldashboards.html', {'choices_kv':choices_kv, 'choices_dict':choices_dict, "food_name_list":food_name_list, "food_group_list":food_group_list, "df_group_name_dict":df_group_name_dict,"loop_range":loop_range, "barplot_foodwate":barplot_foodwate, "group_plot_climate":group_plot_climate})
    


def category_list(request):
    #data_frida_final= Dataset.objects

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
   
    choices_kv= {"Protein_deklaration_g":"Protein rich food-items", "Kostfibre_g":"Fiber (Dietry) rich food-items", "Fedt_total_g":"Fatty-acids rich food-items", "Kulhydrat_deklaration_g":"Carbohydrate rich food-items", 'A_vitamin_RE':'A-vitamin rich food-items', "B1-vitamin":'B1-vitamin rich food-items', "B2-vitamin_riboflavin":'B2-vitamin rich food-items', "B6-vitamin":'B6-vitamin rich food-items', "B12-vitamin":'B12-vitamin rich food-items', "C-vitamin":'C-vitamin rich food-items', "D_vitamin_µg":'D-vitamin rich food-items', "E-vitamin":'E-vitamin rich food-items', "Calcium, Ca":'Calcium rich food-items', "Jern, Fe":'Iron rich food-items', 'Kalium, K':'Potassium rich food-items', 'Natrium, Na': 'Sodium rich food-items'}
   
    return render(request, 'dashboard/alldashboards.html', {'choices_kv':choices_kv, 'choices_dict':choices_dict, "food_name_list":food_name_list, "food_group_list":food_group_list, "df_group_name_dict":df_group_name_dict,"loop_range":loop_range, "barplot_foodwate":barplot_foodwate, "group_plot_climate":group_plot_climate})
    



def xrich_todisplay(request):
    xrich_option= request.POST['x_riches_cat']
    #data_frida_final= Dataset.objects

    data_frida_final= "https://github.com/mrchapagain/ConsumerDataAnalytics/raw/main/finaldf_fridanutrient_aditionallink_groups.xlsx"

    cls= FridaDataAnalytics()
    df_frida= cls.frida_datareader(data_frida_final)

    food_group_list= cls.FødevareGruppe_list(df_frida)
    food_name_list= cls.FødevareNavn_list(df_frida)

    choices_kv= {"Protein_deklaration_g":"Protein rich food-items", "Kostfibre_g":"Fiber (Dietry) rich food-items", "Fedt_total_g":"Fatty-acids rich food-items", "Kulhydrat_deklaration_g":"Carbohydrate rich food-items", 'A_vitamin_RE':'A-vitamin rich food-items', "B1-vitamin":'B1-vitamin rich food-items', "B2-vitamin_riboflavin":'B2-vitamin rich food-items', "B6-vitamin":'B6-vitamin rich food-items', "B12-vitamin":'B12-vitamin rich food-items', "C-vitamin":'C-vitamin rich food-items', "D_vitamin_µg":'D-vitamin rich food-items', "E-vitamin":'E-vitamin rich food-items', "Calcium, Ca":'Calcium rich food-items', "Jern, Fe":'Iron rich food-items', 'Kalium, K':'Potassium rich food-items', 'Natrium, Na': 'Sodium rich food-items'}

    #xrich_choice_df= cls.list_x_rich(df_frida, xrich_option, "fødevareGruppe")
    xrich_choice_df= cls.list_x_rich(df_frida, xrich_option, "fødevareGruppe")

    df_title_xrich= f'Data table with Top 20 "{choices_kv[xrich_option]}"'

    xrich_info_dic={"Protein_deklaration_g": "Proteinindhold kan beregnes ud fra analyserede værdier for totalt nitrogen (kvælstof).",
                    "Kostfibre_g": "Fibre is an important part of a healthy balanced diet and is only found in foods that come from plants. Meat, fish and dairy products don't contain any fibre.Foods that contain fibre make you feel fuller for longer and can help digestion.",
                    "Fedt_total_g": "Det totale fedtindhold er summen af triglycerider, fosforlipider, steroler og en mindre andel af andre fedtopløselige stoffer der ekstraheres i fedt fraktionen. Der analyseres for enkelte fedtsyrer som opdeles i kategorierne mættede, enkeltumættede og flerumættede. Der beregnes summer for fedtsyrekategorierne samt for omega 3 og omega 6 fedtsyrer. ",
                    "Kulhydrat_deklaration_g": "Kulhydrat er forbindelser der består af sukkermolekyler hvilket inkluderer sukkerstoffer, stivelse og kostfibre.",
                    'A_vitamin_RE':"1 RE = 1 µg retinol. Vitamin A (also known as retinol) has several important functions, including: helping your immune system to fight infections, helping your vision in dim light, keeping your skin healthy",
                    "B1-vitamin":"Thiamin is also known as vitamin B1. It helps the other B vitamins to break down and release.",
                    "B2-vitamin_riboflavin": "Riboflavin is also known as vitamin B2. It helps to keep your skin, eyes and nervous system healthy and release energy from the food you eat.",
                    "B6-vitamin":"Pyridoxine is also known as vitamin B6. It helps the body to: use and store energy from protein and carbohydrates in food form the substance that carries oxygen around the body (haemoglobin) in your blood",
                    "B12-vitamin":"Vitamin B12 helps our body: make red blood cells and keep the nervous system healthy, release energy from the food we eat, process folic acid. Folic acid (also known as folate) works with vitamin B12 to form healthy red blood cells.",
                    "C-vitamin":"Vitamin C (also known as ascorbic acid) helps to: protect and keep cells healthy, maintain healthy connective tissue, heal wounds",
                    "D_vitamin_µg":"Vitamin D helps to regulate the amount of calcium and phosphate in the body, important for bone, teeth and muscle health. Vitamin D is made by our skin from sunlight and is also found in small amounts in some foods.",
                    "E-vitamin":"Vitamin E is a powerful antioxidant that helps to: repair damaged cells and protect them from free-radicals, keep your skin and eyes healthy, strengthen your immune system",
                    "Calcium, Ca":"Calcium helps to build strong bones and teeth and regulate your heartbeat. It also ensures your blood clots normally, important for healing.",
                    "Jern, Fe":"Iron helps our body make red blood cells to carry oxygen around your body. If we don't have enough iron in your diet, you're at risk of developing iron deficiency anaemia.",
                    'Kalium, K':"Potassium helps the body control the balance of fluids and keeps our heart healthy and functioning correctly.",
                    'Natrium, Na': "The sodium is an essential nutrient used by our body to maintain blood pressure and regulate your nerves and muscles. Sodium attracts and holds on to water in your blood. If we consume too much salt, the volume of water in our blood increase leading to high blood pressure. If left untreated, we could be at risk of developing heart disease or a stroke."
                    }

    xrich_info_todisplay= xrich_info_dic[xrich_option]

    return render(request, 'dashboard/alldashboards.html', {'xrich_option':xrich_option, 'food_group_list':food_group_list, 'food_name_list':food_name_list, 'choices_kv':choices_kv, 'xrich_choice_df':xrich_choice_df, 'df_title_xrich':df_title_xrich, 'xrich_info_todisplay':xrich_info_todisplay})
    
