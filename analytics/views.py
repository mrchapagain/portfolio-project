from django.shortcuts import render, redirect, get_object_or_404
from .apiauth import *
from .classifier import *
from job.models import Job
from blog.models import Blog

# Create your views here.
def  allanalytics(request):
    # Enter the Tweeter user-Id and see the data 
    tweeter_id= "DRNyheder" #input("Type Tweter-id which is after @, fx DRNyheder for DR News: ") # fxDRNyheder
    df_user_tweet= tweets_by_user(tweeter_id)
    # Top most liked tweets
    mostlike_df_user_tweet= df_user_tweet.loc[df_user_tweet.Likes.nlargest(10).index]
    #df_col= mostlike_df_user_tweet.index

    # Display sentiment df
    #df_sentiment=SentimentAnalysis(mostlike_df_user_tweet.reset_index())
    
    analyticss= mostlike_df_user_tweet

    wordclouds= wordcloud_plot(analyticss.index)
    sentiments= SentimentAnalysis(analyticss.reset_index())
    sentimentsplot= sentiment_plot(sentiments)
    
    return render(request, 'analytics/allanalytics.html', {'analyticss': analyticss, 'wordclouds': wordclouds, 'sentiments':sentiments, 'sentimentsplot':sentimentsplot})

#def analyticsdetail(request, analytics_id):
    #detailanalytics= get_object_or_404(Analytics, pk=analytics_id)
    #return render(request, 'aboutme/analyticsdetail.html', {'analytics': detailanalytics})

def index(request):
    if request.method == 'GET':
        return render(request, 'index-search.html')
