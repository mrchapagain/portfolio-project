from django.shortcuts import render, redirect, get_object_or_404
from .apiauth import *
from .classifier import *


# Create your views here.
def  allanalytics(request):
    tweeter_id= "DRNyheder" #input("Type Tweter-id which is after @, fx DRNyheder for DR News: ") # fxDRNyheder
    # lets use the function to ge the dataframe which gives fataframe with index
    df_user_tweet= tweets_by_user(tweeter_id)

    #lets use word cloud function to get the wordcloud figure
    rows=df_user_tweet.shape[0]
    title= f'Word-Cloud of {rows} tweets from {tweeter_id}'
    wordclouds= wordcloud_plot(df_user_tweet.Tweets, title)

    # use function to get dataframe with sentiment Analytic column for 10 most liked tweets
    df_user_tweet_sentiment= SentimentAnalysis(df_user_tweet)[['Tweets', 'Likes', 'Time', 'Analysis']]
    sentiments= df_user_tweet_sentiment.loc[df_user_tweet_sentiment.Likes.nlargest(10).index].reset_index(drop=True)

    # Plot the Analytics columns of the sentiment dataframe
    rows=df_user_tweet_sentiment.shape[0]
    title= f'Sentiment Analysis of {rows} tweets from {tweeter_id}'
    sentimentsplot= sentiment_plot(df_user_tweet_sentiment, title)
    
    return render(request, 'analytics/allanalytics.html', {'wordclouds': wordclouds, 'sentiments':sentiments, 'sentimentsplot':sentimentsplot})

#def analyticsdetail(request, analytics_id):
    #detailanalytics= get_object_or_404(Analytics, pk=analytics_id)
    #return render(request, 'aboutme/analyticsdetail.html', {'analytics': detailanalytics})

def  keywordsearch(request):
    #Get the data by typing keywords and look Sentiment Analytics
    keywords= "Health" 
    #input('Type the word you want to search tweet by: ')
    df_by_keywords = tweets_by_keywords(keywords)

    # Top 10 recent tweets from keywords search and lets rearrange columns and index
    kanalyticss= df_by_keywords.head(20) #.loc[df_by_keywords.Likes.nlargest(10).index].reset_index(drop=True)[['Created_at', 'Tweets', 'Likes', 'User']]

    #lets use word cloud function to get the wordcloud figure
    rows=df_by_keywords.shape[0]
    title= f'Word-Cloud of {rows} tweets from {keywords}'
    kwordclouds= wordcloud_plot(df_by_keywords.Tweets, title)

    # use function to get dataframe with sentiment Analytic column
    ksentiments= SentimentAnalysis(df_by_keywords)[['Tweets', 'Created_at', 'User', 'Analysis']]
    ksentiments_top20=ksentiments.head(20)

    # Plot the Analytics columns of the sentiment dataframe
    rows=ksentiments.shape[0]
    title=f'Sentiment Analysis of {rows} tweets from {keywords}'
    ksentimentsplot= sentiment_plot(ksentiments, title)

    # Plot of the most mentioned text from Keyword search dataframe 
    #kmostmentionword= most_mentioned_words(df_by_keywords)
    
    return render(request, 'analytics/keywordsearch.html', {'kanalyticss': kanalyticss, 'kwordclouds': kwordclouds, 'ksentiments_top20':ksentiments_top20, 'ksentimentsplot':ksentimentsplot}) #   , 'kmostmentionword':kmostmentionword

def index(request):
    if request.method == 'GET':         
        return render(request, 'analytics/index-search.html', {'analyticss': analyticss, 'wordclouds': wordclouds, 'sentiments':sentiments, 'sentimentsplot':sentimentsplot})



# Create your views here.
def result(request):
    if request.method == 'POST':
                  
        return render(request, 'analytics/result.html', {'analyticss': analyticss, 'wordclouds': wordclouds, 'sentiments':sentiments, 'sentimentsplot':sentimentsplot})