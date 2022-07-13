from django.shortcuts import render, redirect, get_object_or_404
from .apiauth import *
from .classifier import *
from job.models import Job
from blog.models import Blog
from django.shortcuts import HttpResponse

# Create your views here.
def  allanalytics(request):
    tweeter_id= "DRNyheder" #input("Type Tweter-id which is after @, fx DRNyheder for DR News: ") # fxDRNyheder
    # lets use the function to ge the dataframe which gives fataframe with index
    df_user_tweet= tweets_by_user(tweeter_id)

    # Top 10 most liked tweets and lets rearrange columns and index
    analyticss= df_user_tweet.loc[df_user_tweet.Likes.nlargest(10).index].reset_index(drop=True)[['Tweets', 'Likes', 'Time']]

    #lets use word cloud function to get the wordcloud figure
    wordclouds= wordcloud_plot(df_user_tweet.Tweets)

    # use function to get dataframe with sentiment Analytic column
    sentiments= SentimentAnalysis(df_user_tweet)[['Tweets', 'Likes', 'Time', 'Analysis']]

    # Plot the Analytics columns of the sentiment dataframe 
    sentimentsplot= sentiment_plot(sentiments)
    
    return render(request, 'analytics/allanalytics.html', {'analyticss': analyticss, 'wordclouds': wordclouds, 'sentiments':sentiments, 'sentimentsplot':sentimentsplot})

#def analyticsdetail(request, analytics_id):
    #detailanalytics= get_object_or_404(Analytics, pk=analytics_id)
    #return render(request, 'aboutme/analyticsdetail.html', {'analytics': detailanalytics})

def  keywordsearch(request):
    #Get the data by typing keywords and look Sentiment Analytics
    keywords= "Protein" #input('Type the word you want to search tweet by: ')
    df_by_keywords = tweets_by_keywords(keywords)

    # Top 10 most liked tweets from keywords search and lets rearrange columns and index
    kanalyticss= df_by_keywords.loc[df_by_keywords.Likes.nlargest(10).index].reset_index(drop=True)[['Time', 'Tweets', 'Likes', 'User']]

    #lets use word cloud function to get the wordcloud figure
    kwordclouds= wordcloud_plot(df_by_keywords.Tweets)

    # use function to get dataframe with sentiment Analytic column
    ksentiments= SentimentAnalysis(df_by_keywords)[['Tweets', 'Likes', 'Time', 'User', 'Analysis']]

    # Plot the Analytics columns of the sentiment dataframe 
    ksentimentsplot= sentiment_plot(ksentiments)

    # Plot of the most mentioned text from Keyword search dataframe 
    most_mentioned_words(df_user_tweet)
    
    return render(request, 'analytics/allanalytics.html', {'kanalyticss': kanalyticss, 'kwordclouds': kwordclouds, 'ksentiments':ksentiments, 'ksentimentsplot':ksentimentsplot})


def index(request):
    if request.method == 'GET':
        tweeter_id= "DRNyheder" #input("Type Tweter-id which is after @, fx DRNyheder for DR News: ") # fxDRNyheder
        # lets use the function to ge the dataframe which gives fataframe with index
        df_user_tweet= tweets_by_user(tweeter_id)

        # Top 10 most liked tweets and lets rearrange columns and index
        analyticss= df_user_tweet.loc[df_user_tweet.Likes.nlargest(10).index].reset_index(drop=True)[['Tweets', 'Likes', 'Time']]

        #lets use word cloud function to get the wordcloud figure
        wordclouds= wordcloud_plot(df_user_tweet.Tweets)

        # use function to get dataframe with sentiment Analytic column
        sentiments= SentimentAnalysis(df_user_tweet)[['Tweets', 'Likes', 'Time', 'Analysis']]

        # Plot the Analytics columns of the sentiment dataframe 
        sentimentsplot= sentiment_plot(sentiments)

        
        return render(request, 'analytics/index-search.html', {'analyticss': analyticss, 'wordclouds': wordclouds, 'sentiments':sentiments, 'sentimentsplot':sentimentsplot})



# Create your views here.
def result(request):
    if request.method == 'POST':
        tweeter_id= "DRNyheder" #input("Type Tweter-id which is after @, fx DRNyheder for DR News: ") # fxDRNyheder
        # lets use the function to ge the dataframe which gives fataframe with index
        df_user_tweet= tweets_by_user(tweeter_id)

        # Top 10 most liked tweets and lets rearrange columns and index
        analyticss= df_user_tweet.loc[df_user_tweet.Likes.nlargest(10).index].reset_index(drop=True)[['Tweets', 'Likes', 'Time']]

        #lets use word cloud function to get the wordcloud figure
        wordclouds= wordcloud_plot(df_user_tweet.Tweets)

        # use function to get dataframe with sentiment Analytic column
        sentiments= SentimentAnalysis(df_user_tweet)[['Tweets', 'Likes', 'Time', 'Analysis']]

        # Plot the Analytics columns of the sentiment dataframe 
        sentimentsplot= sentiment_plot(sentiments)
    
        return render(request, 'analytics/result.html', {'analyticss': analyticss, 'wordclouds': wordclouds, 'sentiments':sentiments, 'sentimentsplot':sentimentsplot})