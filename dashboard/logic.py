from analytics.classifier import get_graph

#for user intractivity
#import ipywidgets as widgets
#from ipywidgets import interact, interactive, fixed, interact_manual

# Importing the required libaries for EDA
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
import warnings
warnings.filterwarnings("ignore")

import ipywidgets as widgets
from ipywidgets import interact, interactive, fixed, interact_manual

import networkx as nx


class FridaDataAnalytics():

  def frida_datareader(self, frida_data_object):
    self.frida_data_object= frida_data_object

    df_frida= pd.read_excel(frida_data_object, sheet_name=0, index_col=0, header=0, skiprows=0)
    return df_frida

  def FødevareNavn_list(self,df_frida):
    self.df_frida= df_frida

    FødevareNavn_list= df_frida.FødevareNavn.to_list()
    return FødevareNavn_list

  def FødevareGruppe_list(self,df_frida):
    self.df_frida= df_frida

    FødevareGruppe_list= df_frida.FødevareGruppe.unique()
    return FødevareGruppe_list

  def FødevareGruppe_FødevareNavn_dict(self,df_frida):
    self.df_frida= df_frida

    FødevareGruppe_FødevareNavn_dict= df_frida[["FødevareGruppe",	"FødevareNavn"]].head(100).to_dict(orient='list')
    return FødevareGruppe_FødevareNavn_dict

  def df_FødevareGruppe(self, df_frida, food_category):
    self.df_frida= df_frida
    self.food_category= food_category

    df_with_category= df_frida[df_frida.FødevareGruppe == food_category]
    return df_with_category

  def df_FødevareNavn(self, df_frida, food_name):
    self.df_frida= df_frida
    self.food_name=food_name
    df_food_name= df_frida[df_frida.FødevareNavn == food_name]

    return df_food_name


  def piechart_fooditem_energy(self, df_food_name):
        self.df_food_name=df_food_name

        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = ["Fedt_g", "Kulhydrat_g", "Protein_g"]
        sizes =  df_food_name.loc[:, ["Protein_deklaration_g", 'Kulhydrat_deklaration_g', 'Fedt_total_g']].values.tolist()[0]# 3rd to 8th column value from indivisual-item 
        #sizes= [i*0 for i in sizes if i < 0 ]
        explode = (0, 0, 0.05)  # only "explode" the 3rd slice (i.e. 'Protein')

        my_circle=plt.Circle((0,0),0.4, color="white")
        
        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        
        p=plt.gcf()
        p.gca().add_artist(my_circle)
        ax.annotate(f'Total Energy: \n {df_food_name.Energy_kj.item()}kj / {df_food_name.Energy_kcal.item()} kcal', xy=(0,0), va="center", ha="center", color='red', fontsize=10)

        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(f'Energy content of food-item"{df_food_name.FødevareNavn.item()}"', fontsize=10)

        plt.tight_layout()
        graph=get_graph()
        return graph


  def piechart_fooditem_co2(self, df_fooditem_climate):
        self.df_fooditem_climate=df_fooditem_climate
      
        # Pie chart, where the slices will be ordered and plotted counter-clockwise:
        labels = ['Agriculture', 'iLUC', 'Processing', 'Packaging', 'Transport', 'Retail']
        sizes =  df_fooditem_climate[labels].values.tolist()[0] # 3rd to 8th column value from indivisual-item 
        sizes = [0 if i < 0 else i for i in sizes] # Negetive value replace with 0
        explode = (0, 0, 0, 0, 0.1, 0)  # only "explode" the 5th slice (i.e. 'Transport')

        my_circle=plt.Circle((0,0),0.4, color="white")
        
        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        
        p=plt.gcf()
        p.gca().add_artist(my_circle)
        ax.annotate(f'Total CO2 eq_perkg: \n {df_fooditem_climate.Total_CO2_eq_perkg.item()}', xy=(0,0), va="center", ha="center", color='red', fontsize=10)

        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        plt.title(f'Carbon footprint contribution from "{df_fooditem_climate.Product_dk.item()}"', fontsize=10)
        plt.tight_layout()
        graph=get_graph()
        #ax.legend()
        return graph



  def co2_data_plot(self, selected_dropped_data):
        self.selected_dropped_data= selected_dropped_data
        # Group some of the elements from columns with categorical data
        df_with_category= selected_dropped_data[['Category_en', 'Agriculture', 'iLUC', 'Processing', 'Packaging',	'Transport',	'Retail', 'Total_CO2_eq_perkg']].groupby(by= ['Category_en'], sort=True).mean().sort_values(by=['Total_CO2_eq_perkg'], ascending=False).round(decimals = 2)
        
        # Stacked bar plot
        rows= selected_dropped_data.shape[0]
        plt.switch_backend('AGG')
        fig, ax= plt.subplots(figsize=(10, 5))
        ax.barh(df_with_category.index, df_with_category['Agriculture'], label= "Agriculture")
        ax.barh(df_with_category.index, df_with_category['iLUC'], label='iLUC')
        ax.barh(df_with_category.index, df_with_category['Packaging'], label='Processing')
        ax.barh(df_with_category.index, df_with_category['Packaging'], label='Packaging')
        ax.barh(df_with_category.index, df_with_category['Transport'], label='Transport')
        ax.barh(df_with_category.index, df_with_category['Retail'], label='Retail')

        #sns.barplot(df2.values, df2.index, alpha=1)
        plt.xticks(rotation=20)
        plt.title(f'"Share of the Total CO2 contribution based on food category"')
        plt.ylabel("Product Category")
        plt.xlabel("Total average CO2 equivalent/Kg")
        ax.legend()
        plt.tight_layout()
        graph=get_graph()
        return graph  


  def comparision_barplot_climate(self, df_climate, foodname):
      self.df_climate=df_climate
      #self.foodname= foodname
      plt.switch_backend('AGG')

      plt.figure(figsize=(10,5))
      #plt.title(title, fontsize=8)
      #sns.bar(df_fooditem_climate.Analysis.unique(), df_fooditem_climate['Analysis'].value_counts(), color ='grey', width = 0.4)
      df_foodname_climate= df_climate[df_climate.Product_dk== foodname]
      sns.barplot(data= df_climate, x= "Category_dk", y= "Total_CO2_eq_perkg", palette= "hls") #df_foodname_climate.Product_dk.item()
      # # palette={"Vegetables_Average": "blue", "Meat/Poultry_Average": "red", {foodname}: "green"}
      plt.xticks(rotation=20)
      plt.xlabel('Name of Food item')
      plt.ylabel('Total CO2 emission contribution')
      plt.tight_layout()
      graph=get_graph()
      return graph


  def foodwaste_portion_barplot(self, df_frida, svind_percentage, title_cat):
      self.df_frida= df_frida
      self.svind_percentage= svind_percentage
      self.title_cat= title_cat

      #slider= widgets.IntSlider(value=0, min=0, max=99,description="Choose food-waste %", orientation= "horizontal", readout= True)
      #interact(func, svind_percentage=slider)
      
      ## first acess right data from the given dataset
      # Drop the rows with non numeric and change rest of the rows to float type
      df_numeric_fridasvind= df_frida["Svind_%"].drop(df_frida[df_frida["Svind_%"] == "iv"].index).astype(float)
      # Just select the desired row with waste % value
      svind_condition=df_numeric_fridasvind[df_numeric_fridasvind > svind_percentage]
      # Get whole datasetwith the condition above
      df_frida_foodwaste= df_frida[["FødevareNavn","Svind_%"]].iloc[svind_condition.index]
      
      # add column for eaten part
      df_frida_foodwaste["Spiseligt_%"] = df_frida_foodwaste["Svind_%"].apply(lambda x: 100-x)

      df_frida_foodwaste_sorted=df_frida_foodwaste.sort_values("Svind_%", ascending=False, ignore_index=True).head(10)
      
      ## code for plotting
      
      plt.switch_backend('AGG')
      plt.subplots(figsize=(15, 10))
      
      #plt.bar(df_frida_foodwaste_sorted["FødevareNavn"], df_frida_foodwaste_sorted["Svind_%"], color="red") #Horizontal bar plot
      #plt.bar(df_frida_foodwaste_sorted["FødevareNavn"], df_frida_foodwaste_sorted["Spiseligt_%"], color="green")
      #sns.barplot(data= df_frida_foodwaste_sorted, x= 'FødevareNavn', y='Svind_%', hue= "FødevareGruppe", palette= 'hls') #{"Vegetables_Average": "blue", "Meat/Poultry_Average": "red", {foodname}: "green"} 
      df_frida_foodwaste_sorted[["FødevareNavn","Spiseligt_%", "Svind_%"]].set_index('FødevareNavn').plot(kind='bar', stacked=True, color=['green', 'red'])

      plt.title(f'List of top 10 food-items with over {svind_percentage} percent waste from {title_cat}', fontsize=10)
      plt.legend()
      plt.xticks(rotation=75)
      plt.xlabel(f'FødevareNavn lister')
      plt.ylabel('Spiseligtand and Svind %')
      #plt.text(x=0, y=0, s= "gg", color= None)
      plt.tight_layout()
      graph=get_graph()
      return graph

  # Function for text display
  def text_display_frida(self, frida_data):
      self.frida_data= frida_data
      plt.switch_backend('AGG')
      fig, ax= plt.subplots(figsize=(10,5))
      
      FødevareNavn= frida_data["FødevareNavn"].values[0]
      
      Total_energy_kj= frida_data["Energy_kj"].values[0]
      Total_energy_kacl= frida_data["Energy_kcal"].values[0]

      Protein_deklaration_g= frida_data["Protein_deklaration_g"].values[0]
      Kulhydrat_deklaration_g= frida_data["Kulhydrat_deklaration_g"].values[0]
      Fedt_total_g= frida_data["Fedt_total_g"].values[0]
      Kostfibre_g= frida_data["Kostfibre_g"].values[0]
      Organiske_syrer= frida_data["Organiske syrer_total"].values[0]
      Alkohol= frida_data["Alkohol_g"].values[0]
      Sukkeralkoholer= frida_data["Sukkeralkoholer_total"].values[0]

      TaxonomicName= frida_data["TaxonomicName"].values[0]
      Water_Drymatter= frida_data["Vand_g"].values[0]
      Svind_percent= frida_data["Svind_%"].values[0]

      #A= frida_data["A_vitamin_RE"].values[0]
      #B1= frida_data["B1_vitamin"].values[0]
      #B2= frida_data["B2-vitamin_riboflavin"].values[0]
      #B6= frida_data["B6_vitamin"].values[0]
      #B12= frida_data["B12_vitamin"].values[0]
      #C= frida_data["C_vitamin"].values[0]
      #D= frida_data["D_vitamin_µg"].values[0]
      #D3= frida_data["D3_vitamin_µg"].values[0]
      #E= frida_data["E_vitamin"].values[0]
      #\n Vitamins: A-{A}_µg, E-{E}_µg, B1-{B1}_µg, B2-{B2}_µg, B6-{B6}_µg, B12-{B12}_µg, C-{C}_µg, D-{D}_µg, D3-{D3}_µg

      text_kwargs = dict(ha='left', va='top', fontsize=12, color='C1')
      txt= f' ************************ \
            \n Food Name:  {FødevareNavn},\
            \n Total Energy:  {Total_energy_kj}kj /{Total_energy_kacl}kacl, \
            \n - Organiske_syrer:  {Organiske_syrer}g, \
            \n - Protein:  {Protein_deklaration_g}g,\
            \n - Carbohydrate: {Kulhydrat_deklaration_g}g,\
            \n - Fat:  {Fedt_total_g}g, \
            \n - Fiber: {Kostfibre_g}g, \
            \n - Alkohol: {Alkohol}g, \
            \n - Sukkeralkoholer: {Sukkeralkoholer}g, \
            \n\
            \n Scientific Name:  {TaxonomicName}, \
            \n Water & Dry_matter ratio: {(Water_Drymatter , 100-Water_Drymatter)}, \
            \n Can not be eaten %:  {Svind_percent}%, \
            \n ************************ '
      plt.text(0.05, 1.0, txt, **text_kwargs)
           
      plt.title(f'Detail information of the food item: {FødevareNavn}', fontsize=10)
      plt.axis('off')
      plt.tight_layout()
      graph=get_graph()
      return graph


  def flavour_compound(self, FødevareNavn):
      self.FødevareNavn= FødevareNavn

      plt.switch_backend('AGG')

      #plt.figure(figsize=(10,5))
      fig, ax = plt.subplots(figsize=(10,5))

      G = nx.Graph()
      G.add_edge(FødevareNavn, 'Flavour_B')
      G.add_edge(FødevareNavn, 'Flavour_C')
      G.add_edge(FødevareNavn, 'Flavour_D')
      G.add_edge(FødevareNavn, 'Flavour_E')
      G.add_edge('Flavour_C', "Food-item_1")
      G.add_edge('Flavour_C', "Food-item_2")
      G.add_edge('Flavour_C', "Food-item_3")

      # explicitly set positions
      pos = {'Flavour_B': (-1, -1), 'Flavour_C': (1, -1), FødevareNavn: (0, 0), 'Flavour_D': (-1, 1), 'Flavour_E': (1, 1), "Food-item_1": (1, 0), "Food-item_2": (1.45, -0.25), "Food-item_3": (1.5, -1)}

      options = {
        "font_size": 10,
        "node_size": 5000,
        "node_color": "grey",
        "edgecolors": "grey",
        "linewidths": 3,
        "width": 3,
        "alpha":1,
      }

      nx.draw_networkx(G, pos, **options)

      # Set margins for the axes so that nodes aren't clipped
      ax = plt.gca()
      ax.margins(0.10)

      txt= "(This is a sample figure and relavent figure will be updated soon.........)"
      plt.text(-1, -1.5, txt, color= "r", fontsize = 9, alpha=0.8)
      plt.title(f'Flavour compound from the food item: {FødevareNavn}', fontsize=10)
      plt.axis('off')
      plt.tight_layout()
      graph=get_graph()
      return graph