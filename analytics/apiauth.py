# Necessary libaries
from tweepy import OAuthHandler
from tweepy import API
import tweepy
import pandas as pd
import warnings
warnings.filterwarnings("ignore")
import time


#Necessary information form tweet account
consumer_key='hYt37U1prLMj2LBfWaH3VfwAP'
consumer_secret='8sOKCBqlh0NLEByi3IjQ1mjlhTVhAtFzoOLqU9w5vn0qjmdAR1'
access_token='14970816-bxUWKHaeQvNpVP7nNzgOwWe2Sa3dsLAposBrhuhsg'
access_token_secret='nqioC9WEH7XFXpMU6KxmKuplZ4SIwmcgKAUzQYc1E2bXo'

#Tweepy authentication
auth = OAuthHandler(consumer_key, consumer_secret) # Consumer key authentication
auth.set_access_token(access_token, access_token_secret) # Access key authentication
api = API(auth)  # Set up the API with the authentication handler

##Obtaining Tweets from user ID
# Function to obtain tweet from specific user account
def tweets_by_user(user):
      limit=300
      tweets_obj= tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode="extended").items(limit)
              
      # Create Data Frame
      columns= ['Tweets', 'Likes', 'Created_at', 'User']
      tweets = []
      for i in tweets_obj:
            tweets.append([i.full_text, i.favorite_count, i.created_at, i.user.screen_name])

      df_by_id= pd.DataFrame(tweets, columns=columns)
      df_by_id['Created_at']=df_by_id['Created_at'].apply(lambda x: x.strftime('%Y-%m-%d'))

      #now lets make only tweets thats has not Re-Tweeted!
      df_by_id= df_by_id[~df_by_id.Tweets.str.contains("RT")]
              
      return df_by_id
            
            
# Obtaining tweet using keywords or Hastag
def tweets_by_keywords(keywords):
      limit=300
      api_methods=['search_tweets', 'search_30_day', 'search_full_archive', 'search_users', 'search_geo']
      tweets_obj= tweepy.Cursor(api.search_tweets, q=keywords, count=100, tweet_mode="extended").items(limit)
      # Create Data Frame
      columns= ['Tweets', 'Likes', 'Created_at', 'User']
      tweets = []
      for i in tweets_obj:
            tweets.append([i.full_text, i.favorite_count, i.created_at, i.user.screen_name])
      df_by_keywords= pd.DataFrame(tweets, columns=columns)
      df_by_keywords['Created_at']= df_by_keywords['Created_at'].apply(lambda x: x.strftime('%Y-%m-%d'))

      #now lets make only tweets thats has not Re-Tweeted!
      #df_by_keywords= df_by_keywords[~df_by_keywords.Tweets.str.contains("RT")] # better to use that has retweeted
      return df_by_keywords

def tweets_trends(woeid_dict):
      df=pd.DataFrame()

      for country, woeid in woeid_dict.items():
        # fetching the trends
        trends= api.get_place_trends(id= woeid, exclude = "hashtags") #tweepy.Cursor(api.trends_available, id= woeid)
        df_list= []
        df1=pd.DataFrame()
        for value in trends:
          for trend in value['trends']:
            df_list.append(trend['name'])
        df1[country]= df_list
        df= pd.concat([df, df1[country]], axis = 1)
      return df




 

 

 

 
