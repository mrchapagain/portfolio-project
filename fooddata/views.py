from django.shortcuts import render
from .datavis import *
from .models import Country_Name, Trendskeyword,  TimeFrame


def keyword_tosearch(request):
    kw_choosen= request.POST['key_words']
    kw_choosen= [kw_choosen]
    tf_choosen= request.POST['time_frame']
    
    # Lets define variables for user input
    keyword_dict= [{"Healthy Diet":"Healthy Diet", "Protein Diet": "Protein Diet", "Healthy Food": "Healthy Food"}] #Trendskeyword.objects.all()
    tf_dict = {"today-12months":'today 12-m', "today-5years":'today 5-y'} #TimeFrame.objects.all()
    
    pn_dict = {"denmark": "DK", "united_states": "US", "russia": "RU", "sweden": "SE", "india": "IN", "germany": "DE"} #Country_Name.objects.all()
    st_dict = {"Default":"", "Image": "image", "News": "news"}
    cat_dict = { "All":0, "Health": 45, "Food_Drink": 71}
    
    # Lets call the function to get trends object
    trends= pytrends_func(kw_choosen, tf_choosen)

    # calling function for interest over time then get the graph with relavent function
    df_trends_overtime = gt_trends_over_time(trends, kw_choosen)
    # Visual function - display_lineplot(df, x, kw_list, title, x_label, y_label)
    vis_trends_overtime= display_lineplot(df_trends_overtime, "date", kw_choosen, title= f'Keyword Web Search of {kw_choosen} Interest Over Time', x_label= "date", y_label="Trends over time")

    #calling function for Interest by region 
    df_trends_byregion= gt_trends_byregion(trends, kw_choosen)
    # Visual function - display_lineplot(df, x, kw_list, title, x_label, y_label)
    vis_trends_byregion= display_barplot(df_trends_byregion.iloc[:10,:], "geoName", kw_choosen, f'Top 10 google-search trends of keywors: "{kw_choosen}" by regions')

    #calling function for releted quries 
    df_trends_reletedquries= gt_related_queries(trends, kw_choosen)
    df_trends_rq10= df_trends_reletedquries.iloc[:10, :]
    df_title_keyword= f'10 Releted Quries from google search trends with keyword "{ kw_choosen }"'

    # Visual function - display_lineplot(df, x, kw_list, title, x_label, y_label)
    vis_trends_reletedquries= wordcloud_plot(df_trends_reletedquries.iloc[:, 0:2], f'Word-cloud of releted queries for google-search with \n keyword- "{kw_choosen[0]}"')
    #for kw in kw_choosen: wordcloud_plot(df_trends_reletedquries.iloc[:, 0:2], f'Word-cloud of releted queries for google-search with \n keyword- "{kw}"')

    return render(request, 'fooddata/allfooddatas.html', {"tf_dict":tf_dict, 'kw_choosen':kw_choosen, "keyword_dict":keyword_dict, "vis_trends_overtime":vis_trends_overtime, "vis_trends_byregion":vis_trends_byregion, "df_trends_rq10":df_trends_rq10, "df_title_keyword":df_title_keyword, "vis_trends_reletedquries":vis_trends_reletedquries})
    

def timeframe_tosearch(request):
    #tf_choosen= request.POST['time_frame']

    # Lets define variables for user input
    keyword_dict= [{"Healthy Diet":"Healthy Diet", "Protein Diet": "Protein Diet", "Healthy Food": "Healthy Food"}] #Trendskeyword.objects.all()
    tf_dict = {"today-12months":'today 12-m', "today-5years":'today 5-y'} #TimeFrame.objects.all()
    timeframe= tf_dict["today-5years"]
    kw_list= ["Healthy Diet", "Protein Diet"] # list(keyword_dict[0].values())
    
    pn_dict = {"united_states": "US", "russia": "RU", "sweden": "SE", "india": "IN", "germany": "DE"} #Country_Name.objects.all()
    st_dict = {"Default":"", "Image": "image", "News": "news"}
    cat_dict = { "All":0, "Health": 45, "Food_Drink": 71}

    # Lets call the function to get trends object
    trends= pytrends_func(kw_list, timeframe)

    # calling function for trends of the year
    df_trends_ofyears = gt_topics_ofthe_year(trends)
    df_title_toy= f'Top 5 rows from the google trends of the years'

    # calling function for latest trending searches 
    df_trends_latestsearch = latest_trending_searches(trends, pn_dict.keys())
    df_title_ls= f'Top 5 rows from the google latest trending searches within last 24 hours'

    # calling function for Realtime search trends
    #df_trends_realtime = realtime_search_trends(trends, pn_dict)
    #df_title_rt= f'Top 5 rows from the google realtime searching trends within last 24 hours'
 
    return render(request, 'fooddata/allfooddatas.html', {"df_title_toy":df_title_toy, "df_title_ls":df_title_ls, "keyword_dict":keyword_dict, 'pn_dict':pn_dict, "tf_dict":tf_dict, "df_trends_ofyears":df_trends_ofyears, "df_trends_latestsearch":df_trends_latestsearch})


def allfooddatas(request):
    # Lets define variables for user input
    keyword_dict= [{"Healthy Diet":"Healthy Diet", "Protein Diet": "Protein Diet", "Healthy Food": "Healthy Food"}] #Trendskeyword.objects.all()
    tf_dict = {"today-12months":'today 12-m', "today-5years":'today 5-y'} #TimeFrame.objects.all()
    timeframe= tf_dict["today-5years"]
    kw_list= ["Healthy Diet", "Protein Diet"] # list(keyword_dict[0].values())
    
    pn_dict = {"denmark": "DK", "united_states": "US", "russia": "RU", "sweden": "SE", "india": "IN", "germany": "DE"} #Country_Name.objects.all()
    st_dict = {"Default":"", "Image": "image", "News": "news"}
    cat_dict = { "All":0, "Health": 45, "Food_Drink": 71}


    # Lets call the function to get trends object
    trends= pytrends_func(kw_list, timeframe)
    
    # calling function for trends of the year
    df_trends_ofyears = gt_topics_ofthe_year(trends)
    df_title_toy= f'Top 5 rows from the google trends of the years'

    # calling function for latest trending searches 
    df_trends_latestsearch = latest_trending_searches(trends, pn_dict.keys())
    df_title_ls= f'Top 5 rows from the google latest trending searches within last 24 hours'


    return render(request, 'fooddata/allfooddatas.html', {"keyword_dict":keyword_dict, "pn_dict":pn_dict, "tf_dict":tf_dict, "st_dict":st_dict, "cat_dict":cat_dict, "df_trends_ofyears":df_trends_ofyears, "df_title_toy":df_title_toy, "df_trends_latestsearch":df_trends_latestsearch, "df_title_ls":df_title_ls}) 