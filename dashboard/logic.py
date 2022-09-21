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
