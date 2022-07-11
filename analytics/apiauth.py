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

##Tweets from user
# Function to obtain tweet from specific user account
def tweets_by_user(user):
      limit=300
      tweets_obj= tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode="extended").items(limit)
      
      # Create Data Frame
      columns= ['Tweets', 'Likes', 'Time', 'User']
      tweets = []
      for i in tweets_obj:
        tweets.append([i.full_text, i.favorite_count, i.created_at, i.user.screen_name])

      df_by_id= pd.DataFrame(tweets, columns=columns)
      df_by_id['Time']=df_by_id['Time'].apply(lambda x: x.strftime('%Y-%m-%d'))

      #now lets make only tweets thats has not Re-Tweeted!
      df_by_id= df_by_id[~df_by_id.Tweets.str.contains("RT")].set_index('Tweets')
      
      return df_by_id

def export(self):           
    return self.df


