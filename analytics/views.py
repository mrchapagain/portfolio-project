from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from .apiauth import *
from .classifier import *
from .models import Tweetid, Tweetkeyword


# Create your views here.
def keyword_tosearch(request):
    keywords= request.POST['keyword']
    # use function defined on classifier.py to get the dataframe from keyword
    df_by_keywords = tweets_by_keywords(keywords)

    #lets use word cloud function to get the wordcloud figure
    rows=df_by_keywords.shape[0]
    title= f'Word-Cloud of {rows} tweets from keyword:{keywords}'
    kwordclouds= wordcloud_plot(df_by_keywords.Tweets, title)

    # use function to get dataframe with sentiment Analytic column
    ksentiments= SentimentAnalysis(df_by_keywords)[['Tweets', 'Created_at', 'User', 'Likes', 'Analysis']].sort_values('Likes', ascending=False, ignore_index=True)
    ksentiments_top20=ksentiments.head(10)#loc[df_by_keywords.Likes.nlargest(10).index].reset_index(drop=True)[['Created_at', 'Tweets', 'Likes', 'User', 'Analysis']]
    df_title_keyword= f'10 latest Tweets detail with keyword "{keywords}"'

    # Plot the Analytics columns of the sentiment dataframe
    rows=ksentiments.shape[0]
    title=f'Sentiment Analysis of {rows} tweets from keyword:{keywords}'
    ksentimentsplot= sentiment_plot(ksentiments, title)

    # Plot of the most mentioned text from Keyword search dataframe 
    kmostmentionword= most_mentioned_words(ksentiments,  keywords)

    #Keyword list for user input
    user_id_dict= Tweetid.objects.all()
    keyword_dict= Tweetkeyword.objects.all()

    return render(request, 'analytics/allanalytics.html', {"df_title_keyword":df_title_keyword, 'keywords':keywords, 'kwordclouds': kwordclouds, 'user_id_dict':user_id_dict,  'ksentiments_top20':ksentiments_top20, 'ksentimentsplot':ksentimentsplot, 'kmostmentionword': kmostmentionword, 'keyword_dict':keyword_dict})


def userid_tosearch(request):
    tweeter_id= request.POST['userid']
    # use function defined on classifier.py to get the dataframe from user_id which gives fataframe with index
    df_user_tweet= tweets_by_user(tweeter_id)

    #lets use word cloud function to get the wordcloud figure
    rows_userid=df_user_tweet.shape[0]
    title_userid= f'Word-Cloud of {rows_userid} tweets from user-Id: {tweeter_id}'
    wordclouds= wordcloud_plot(df_user_tweet.Tweets, title_userid)

    # use function to get dataframe with sentiment Analytic column for 10 most liked tweets
    df_user_tweet_sentiment= SentimentAnalysis(df_user_tweet)[['Tweets', 'Likes', 'Created_at', 'Analysis']].sort_values('Likes', ascending=False, ignore_index=True)
    sentiments= df_user_tweet_sentiment.head(10)
    df_title_userid= f'10 latest Tweets detail with tweet_id "{tweeter_id}"'

    # Plot the Analytics columns of the sentiment dataframe
    rows_keyword=df_user_tweet_sentiment.shape[0]
    title_keyword= f'Sentiment Analysis of {rows_keyword} tweets from {tweeter_id}'
    sentimentsplot= sentiment_plot(df_user_tweet_sentiment, title_keyword)

    # Plot of the most mentioned text from Keyword search dataframe 
    mostmentionword= most_mentioned_words(df_user_tweet_sentiment,  tweeter_id)
    # user_id list for user input choice
    user_id_dict= Tweetid.objects.all()
    keyword_dict= Tweetkeyword.objects.all()
    
    return render(request, 'analytics/allanalytics.html', {"df_title_userid":df_title_userid, 'tweeter_id':tweeter_id, 'wordclouds': wordclouds, 'sentiments':sentiments, 'sentimentsplot':sentimentsplot, 'mostmentionword': mostmentionword, 'user_id_dict':user_id_dict, 'keyword_dict':keyword_dict})


# Create your views here.
def  allanalytics(request):
    user_id_dict= Tweetid.objects.all()
    keyword_dict= Tweetkeyword.objects.all()

    #Dataframe by tweet_id
    tweeter_id= "AltingetFood" # temporary tweeter id
    df_user_tweet= tweets_by_user(tweeter_id)

    #get the wordd cloud function to get the wordcloud figure
    #rows_userid=df_user_tweet.shape[0]
    #title_userid= f'Word-Cloud of {rows_userid} tweets from user-Id: "{tweeter_id}"'
    #wordclouds= wordcloud_plot(df_user_tweet.Tweets, title_userid)

    # Get the dataframe with the temporary tweeter_id
    df_user_tweet_sentiment= SentimentAnalysis(df_user_tweet)[['Tweets', 'Likes', 'Created_at', 'Analysis']].sort_values('Likes', ascending=False, ignore_index=True)
    sentiments= df_user_tweet_sentiment.head(10)
    df_title_userid= f'10 latest Tweets detail with tweet_id "{tweeter_id}"'

    keywords= "Nordic Diet" # Temprorary keyword
    # get the the dataframe from temporary keyword
    df_by_keywords = tweets_by_keywords(keywords)
    
    #Get the wordcloud figure
    rows=df_by_keywords.shape[0]
    title= f'Word-Cloud of {rows} tweets from keyword: "{keywords}"'
    kwordclouds= wordcloud_plot(df_by_keywords.Tweets, title)

    # Get dataframe from temprory keyword with sentiment Analytic column
    #ksentiments= SentimentAnalysis(df_by_keywords)[['Tweets', 'Created_at', 'User', 'Likes', 'Analysis']].sort_values('Likes', ascending=False, ignore_index=True)
    #ksentiments_top20=ksentiments.head(10)#loc[df_by_keywords.Likes.nlargest(10).index].reset_index(drop=True)[['Created_at', 'Tweets', 'Likes', 'User', 'Analysis']]

    return render(request, 'analytics/allanalytics.html', {"df_title_userid":df_title_userid, "tweeter_id":tweeter_id, "keywords":keywords, 'user_id_dict':user_id_dict, 'keyword_dict':keyword_dict, "sentiments":sentiments, "kwordclouds":kwordclouds})

#def analyticsdetail(request, analytics_id):
    #detailanalytics= get_object_or_404(Analytics, pk=analytics_id)
    #return render(request, 'aboutme/analyticsdetail.html', {'analytics': detailanalytics})