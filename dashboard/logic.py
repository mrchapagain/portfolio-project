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

        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        #plt.title(f'"Total Energy in KJ: {df_food_name.Energy_KJ.values}"', fontsize=12)
        ax.text(1.30, 0.005, f'"Total Energy: {df_food_name.Energy_kj.item()} kj / {df_food_name.Energy_kcal.item()} kcal"', fontsize=12, verticalalignment='bottom', horizontalalignment='right', transform=ax.transAxes, color='red')

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

        fig, ax = plt.subplots()
        ax.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
        #plt.title(f'"Total CO2 contribution equivalent per KG: {df_fooditem_climate.Total_CO2_eq_perkg.values}"', fontsize=12)
        ax.text(1.30, 0.005, f'"Total CO2 contribution equivalent per KG in grams: {df_fooditem_climate.Total_CO2_eq_perkg.item()}"', fontsize=12, verticalalignment='bottom', horizontalalignment='right', transform=ax.transAxes, color='red')
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



  def comparision_barplot_climate(self, df_climate, df_fooditem_climate, foodname):
      self.df_climate=df_climate
      self.df_fooditem_climate= df_fooditem_climate
      self.foodname= foodname
      plt.switch_backend('AGG')

      plt.figure(figsize=(4,3))
      #plt.title(title, fontsize=8)
      #sns.bar(df_fooditem_climate.Analysis.unique(), df_fooditem_climate['Analysis'].value_counts(), color ='grey', width = 0.4)

      sns.barplot(data= df_fooditem_climate, x= ["Vegetables_Average","Meat/Poultry_Average",{foodname}], y= [1,2,3], palette= {"Vegetables_Average": "blue", "Meat/Poultry_Average": "red", {foodname}: "green"})

      #df_fooditem_climate['Analysis'].value_counts().plot(kind='bar', color= {"Neutral": "blue", "Negetive": "red", "Positive": "green"})
      plt.xticks(rotation=20)
      plt.xlabel('Name of Food Category')
      plt.ylabel('CO2 emission contribution')
      plt.tight_layout()
      graph=get_graph()
      return graph

