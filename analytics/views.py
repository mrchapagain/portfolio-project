from django.shortcuts import render

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
    #kmostmentionword= most_mentioned_words(ksentiments,  keywords)

    #Keyword list for user input
    user_id_dict= Tweetid.objects.all()
    keyword_dict= Tweetkeyword.objects.all()
    vis_title= f'Visualization of Twitter analytics from choosen "Keywords": {keywords}"'

    return render(request, 'analytics/allanalytics.html', {"df_title_keyword":df_title_keyword, 'keywords':keywords, 'kwordclouds': kwordclouds, 'user_id_dict':user_id_dict,  'ksentiments_top20':ksentiments_top20, 'ksentimentsplot':ksentimentsplot, 'keyword_dict':keyword_dict, "vis_title":vis_title})


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
    #mostmentionword= most_mentioned_words(df_user_tweet_sentiment,  tweeter_id)
    # user_id list for user input choice
    user_id_dict= Tweetid.objects.all()
    keyword_dict= Tweetkeyword.objects.all()
    vis_title= f'Visualization of Twitter analytics from choosen "User_id": {tweeter_id}'


    
    return render(request, 'analytics/allanalytics.html', {"df_title_userid":df_title_userid, 'tweeter_id':tweeter_id, 'wordclouds': wordclouds, 'sentiments':sentiments, 'sentimentsplot':sentimentsplot, 'user_id_dict':user_id_dict, 'keyword_dict':keyword_dict, "vis_title":vis_title})


# Create your views here.
def  allanalytics(request):
    user_id_dict= Tweetid.objects.all()
    keyword_dict= Tweetkeyword.objects.all()

    #Latest Twitter trends as dataframe
    woeid_dict= {"Denmark":23424796, "Sweden": 23424954, "UK":23424975, "USA" :2488042, "Brazil":23424768, "Ukraine":23424976, "India":23424848}
    sentiments= tweets_trends(woeid_dict).iloc[:20, :]
    tweeter_id= list(woeid_dict.keys())
    df_title_userid= f'20 latest Twiteer (#) trends per countries: "{tweeter_id}"'
    vis_title= "Visualization of Twitter trends of latest 24 hours"

    return render(request, 'analytics/allanalytics.html', {"df_title_userid":df_title_userid, "sentiments":sentiments, "tweeter_id":tweeter_id, 'user_id_dict':user_id_dict, 'keyword_dict':keyword_dict, "vis_title":vis_title})