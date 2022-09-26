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
        plt.title(f'Total Energy content of food-item"{df_food_name.FødevareNavn.item()}"', fontsize=12)

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
        plt.title(f'Carbon footprint contribution from "{df_fooditem_climate.Product_dk.item()}"', fontsize=12)
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

      plt.title(f'List of top 10 food-items with over {svind_percentage} percent waste from {title_cat}', fontsize=8)
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
      plt.figure(figsize=(10,5))
      
      FødevareNavn= frida_data["FødevareNavn"].values[0]
      Svind_percent= frida_data["Svind_%"].values[0]
      Total_energy_kj= frida_data["Energy_kj"].values[0]
      Total_energy_kacl= frida_data["Energy_kcal"].values[0]
      Protein_deklaration_g= frida_data["Protein_deklaration_g"].values[0]
      Kulhydrat_deklaration_g= frida_data["Kulhydrat_deklaration_g"].values[0]
      Fedt_total_g= frida_data["Fedt_total_g"].values[0]
      Kostfibre_g= frida_data["Kostfibre_g"].values[0]
      Fedt_total_g= frida_data["Fedt_total_g"].values[0]
      TaxonomicName= frida_data["TaxonomicName"].values[0]
      text_kwargs = dict(ha='left', va='center', fontsize=12, color='C1')
      txt= f' ************************ \n Food Name:  {FødevareNavn},\n -------------------------- \n Shrinkage %:  {Svind_percent}%, \n -------------------------- \n Total Energy:  {Total_energy_kj}kj /{Total_energy_kacl}kacl,\n -------------------------- \n Protein:  {Protein_deklaration_g}g,\n -------------------------- \n Carbohydrate: {Kulhydrat_deklaration_g}g,\n -------------------------- \n Fat:  {Fedt_total_g}g,\n -------------------------- \n fiber: {Kostfibre_g}g,\n -------------------------- \n Scientific Name:  {TaxonomicName} \n ************************ '
      plt.text(0.1, 0.5, txt, **text_kwargs)
           
      plt.tight_layout()
      graph=get_graph()
      return graph


