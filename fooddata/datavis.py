
# import function from Analytics clasification where visualization function is created
from analytics.classifier import get_graph

# import necessary libaries
import pandas as pd
import numpy as np

from pytrends.request import TrendReq

import matplotlib.pyplot as plt
import seaborn as sns
from seaborn import load_dataset

import warnings
warnings.filterwarnings("ignore")

import re
from textblob import TextBlob
from wordcloud import WordCloud

from spacy.lang.en.stop_words import STOP_WORDS as en_stop #stopwords in English
from spacy.lang.da.stop_words import STOP_WORDS as da_stop #stopwords in Danish
final_stopwords= en_stop.union(da_stop)


#Start to write function
"""
# Connect to google and Build Payload
The build_payload method from Pytrends is used to build a list of keywords that want to search in Google Trends. Can also specify the timeframe to gather data and the category to query the data from.

*kw_list:* list of the target search terms 

*cat:* Category to narrow result fx. Art, Entertainment.[link for category](https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories)

*timeframe:* Date to start from fx. Defaults to last 5yrs is 'today 5-y' or Everything is 'all'

*geo:* Location of interest represent by two letter country abbreviation fx. United States is 'US' or Defaults to World

*gprop:* What Google property to filter to fx. "image" or "news" default to web searches
"""

# Function for connecting google and build playload
def pytrends_func(kw_list, timeframe):
    # Configuring connection wich receives two important parameters; hl (hosting language) & tz (timezone).timeframe=from_date+' '+today_date
    trends = TrendReq(hl='en-US', tz= 360, timeout=(10,25))
    # Update playload
    trends.build_payload(kw_list=kw_list, cat=0, timeframe=timeframe, geo= '', gprop='') #timeframe='today 5-y', cat 0(all), 45(Health), Food & Drink: 71
    # return the trends object
    return trends

"""
kw_list = ["protein diet", "Healthy diet"] 
trends= pytrends_func(kw_list, 'today 12-m')
"""


# Function to Disply in the figure
def display_lineplot(df, x, kw_list, title, x_label, y_label):
    """ The function will take x & value including title, x_label & y_label then display the figure"""
    fig, ax = plt.subplots(figsize= (10, 5))  #Alt-figsize= (10, 5)#, layout='constrained'
    
    # loop over columns to dorw line-plot and add to the figure
    for col in kw_list:
        ax.plot(df[x], df[col], label = col)

    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid(b = True, color ='grey', linestyle ='-.', linewidth = 0.5, alpha = 0.2)# Add x, y gridlines.    #ax.grid(axis= "y")
    
    plt.tight_layout()
    graph=get_graph()
    return graph



def display_barplot(df, x_col, kw_list, title):
    fig, ax = plt.subplots(figsize= (10, 5))
    # Create x-label and width for bars
    x= np.arange(len(df[x_col]))
    
    # loop over columns to drow bar-plot and add to the figure
    for col in kw_list:
        x= x-0.4
        ax.bar(x, df[col], width=0.4, label= col)
        x += 0.2

    plt.title(title, fontsize=12)
    plt.xticks(x, [i for i in df[x_col]], rotation=60)
    plt.xlabel(x_col)
    plt.ylabel("Values")
    plt.legend()  
    plt.grid(axis= "y")

    plt.tight_layout()
    graph=get_graph()
    return graph   


def cleanText(text):
    text= re.sub(r'@[A-Za-z0-9]+', '',text) # Removed @mentions
    text= re.sub(r'#', '',text) # the '#' symbol
    text= re.sub(r':', '',text) # the ':' symbol
    text= re.sub(r'RT[\s]+', '',text) # Removed RT
    text= re.sub(r'https?:\/\/\s+', '',text) # Removed the hyper link
    return text
      
#Function for word-cloud
def wordcloud_plot(releted_queries, title):
    #lets clean the xext first
    releted_queries["query"]= releted_queries["query"].apply(cleanText)
    # Create stopword list
    final_stopwords.update(['https', 'er', 'og', 't', 'co', 'A', 't','The'])
    
    plt.figure(figsize=(10,5))
    allWords= ' '.join( [twts for twts in releted_queries["query"]] )
    wordcloud = WordCloud(stopwords=final_stopwords, max_words=300, width= 800, height=400, random_state=21, max_font_size= 150, background_color="skyblue").generate(allWords)
    
    plt.imshow(wordcloud, interpolation = "bilinear")
    plt.title(title, fontsize=15)
    plt.axis('off')
    plt.tight_layout()
    
    plt.tight_layout()
    graph=get_graph()
    return graph
  

""" 
for kw in kw_list:
      wordcloud_plot(releted_queries.iloc[:, 0:2], f'Word-cloud of releted queries for google-search with \n keyword- "{kw}"')
"""


# function to extract interest over time
def gt_trends_over_time(trends, kw_list):
    # Interest Over Time
    data_over_time= trends.interest_over_time().drop(columns='isPartial')
    data_over_time = data_over_time.reset_index(drop=False)
    return data_over_time

"""
display(gt_trends_over_time(trends, kw_list).tail())
data_over_time= gt_trends_over_time(trends, kw_list)

# Disply figure as lineplot
display_lineplot(data_over_time, "date", kw_list, title= f'Keyword Web Search of {kw_list} Interest Over Time', x_label= "date", y_label="Trends over time")
"""


# Function for Historical hourly interest
def gt_hh_trends(trends,kw_list):
    # Historical Hourly Interest (The hourly interest of the keyword)
    hourly_trends= trends.get_historical_interest(kw_list, year_start=2022, month_start=9, day_start=1, hour_start=0, year_end=2022, month_end=9, day_end=25, hour_end=0, cat=0, sleep=0)
    hourly_trends = hourly_trends.reset_index().drop(columns='isPartial')
    return hourly_trends[hourly_trends[kw_list[0]]> 0]

"""
data_hourly_trends=gt_hh_trends(trends, kw_list)
display(data_hourly_trends.head())

# Disply figure as lineplot
display_lineplot(data_hourly_trends, "date", kw_list, title= f'Hourly search trends of "{kw_list}"', x_label= "date", y_label="Hourly trends rate")
"""


# Function for interest by region
def gt_trends_byregion(trends, kw_list):
    #trends= pytrends_func(["Healthy diet"], 'today 12-m', geo='', gprop='')
    # resolution can be either CITY, COUNTRY or REGION
    trends_by_region= trends.interest_by_region(resolution= 'COUNTRY', inc_low_vol=False, inc_geo_code=False)

    trends_by_region = trends_by_region.sort_values(by=kw_list[0], ascending=False).reset_index()
    return trends_by_region

"""
df_byregion= gt_trends_byregion(trends, kw_list)
display(df_byregion.head())

display_barplot(df_byregion.iloc[:10,:], "geoName", kw_list, f'Top 10 google-search trends of keywors: "{kw_list}" by regions')
"""


#function for releted queries
def gt_related_queries(trends, kw_list):
    # Related Queries (keywords that are closely tied to a primary keyword of the choice)
    related_queries= trends.related_queries()
    df= pd.DataFrame()# Empty dataframe
    for kw in kw_list:
        df1= related_queries[kw]['top']
        df= pd.concat([df, df1], axis = 1)
    #df.style.set_caption("f'10 Releted Quries from google search trends with keyword { kw_list }'")
    return df

"""
releted_queries=gt_related_queries(trends, kw_list)
releted_queries.head()

"""


# Function for trends of the year
def gt_topics_ofthe_year(trends):
    df= pd.DataFrame()# Empty dataframe
    # loop over the year to extract data for each year and put in dataframe as columns
    for year in range(2004, 2022):
        trending = trends.top_charts(year, hl= "en-US", tz=300, geo= "GLOBAL")
        df[year]= trending.title     
    return df.head(10) #.iloc[:, 9:19]

"""
gt_topics_ofthe_year(trends)
"""


# Function to get latest trending searches in specific countries
def latest_trending_searches(trends, country_dict_keys):
    df_trends= pd.DataFrame()# Empty dataframe
    for country_key in country_dict_keys:
        df_trends[country_key] = trends.trending_searches(pn= country_key)
    return df_trends.head(10)

"""
country_dict= {"denmark": "DK", "united_states": "US", "russia": "RU", "sweden": "SE", "india": "IN", "germeny": "DE"}
latest_trending_searches(trends, country_dict_keys)
"""


# Function for Realtime Search Trends
def realtime_search_trends(trends, country_dict):
    df_trends= pd.DataFrame()# Empty dataframe

    for country_key, country_val in country_dict.items():
        df_trends[country_key] = trends.realtime_trending_searches(pn=country_val)["title"]
        
    return df_trends.head(10)

"""
country_dict= {"denmark": "DK", "united_states": "US", "russia": "RU", "sweden": "SE", "india": "IN", "germeny": "DE"}
realtime_search_trends(trends, country_dict)
"""




################### for map-plot
# function yo display in map
def display_mapplot(df_byregion, kw_list):
    from pycountry_convert import country_alpha2_to_continent_code, country_name_to_country_alpha2

    # Data with two columns
    for kw in kw_list:
        df_byregion[f'{kw}_%']= df_byregion[kw].apply(lambda x: x*0.01)

    # Conversion to Alpha 2 codes and Continents
    #function to convert to alpah2 country codes and continents
    def get_continent(col):
        try:
            cn_a2_code =  country_name_to_country_alpha2(col)
        except:
            cn_a2_code = 'Unknown' 
        try:
            cn_continent = country_alpha2_to_continent_code(cn_a2_code)
        except:
            cn_continent = 'Unknown'
            return (cn_a2_code, cn_continent)

    #Apply function to get Alpha 2 codes and Continents
    df_byregion["codes"]= df_byregion["geoName"].apply(get_continent)
    df_byregion["Country"]= df_byregion["codes"].apply(lambda x: x[0])
    df_byregion["Continent"]= df_byregion["codes"].apply(lambda x: x[1])

    # Get longitude and latitude
    #function to get longitude and latitude data from country name
    from geopy.geocoders import Nominatim

    geolocator = Nominatim()
    def geolocate(country):
        try:
            # Geolocate the center of the country
            loc = geolocator.geocode(country)
            # And return latitude and longitude
            return (loc.latitude, loc.longitude)
        except:
            # Return missing value
            return (0, 0)

    # Apply function to get Alpha 2 codes and Continents
    df_byregion["Geolocate"]= df_byregion["Country"].apply(geolocate)
    df_byregion["Latitude"]= df_byregion["Geolocate"].apply(lambda x: x[0])
    df_byregion["Longitude"]= df_byregion["Geolocate"].apply(lambda x: x[1])
    
    
    ## Create a world map
    # Create a world map to show distributions of users 
    import folium
    from folium.plugins import MarkerCluster

    #empty map
    world_map= folium.Map(tiles="cartodbpositron")
    marker_cluster = MarkerCluster().add_to(world_map)

    #for each coordinate, create circlemarker of user percent
    for i in range(len(df_byregion)):
        lat = df_byregion.iloc[i]['Latitude']
        long = df_byregion.iloc[i]['Longitude']
        radius=5
        popup_text = """Country : {}, <br> %of search: {}<br>"""
        popup_text = popup_text.format(df_byregion.iloc[i]['geoName'], df_byregion.iloc[i][kw_list[0]])

        folium.CircleMarker(location = [lat, long], radius=radius, popup= popup_text, fill =True).add_to(marker_cluster)
    #show the map
    return world_map

"""
# display(df_byregion)
# display_mapplot(df_byregion.iloc[:20,:], kw_list)
"""