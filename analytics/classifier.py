# Create a function to compute Negetive, Neutral and Positive analysis
import re
from textblob import TextBlob
from wordcloud import WordCloud 
import matplotlib.pyplot as plt

# Libaries for sentiment analytics (NLP)
import spacy
import seaborn as sns


def wordcloud_plot(df_col):
      plt.figure(figsize=(15, 10))
      allWords= ' '.join( [twts for twts in df_col] )
      wordCloud = WordCloud(width= 1000, height=500, random_state=21, max_font_size= 119).generate(allWords)
      plt.imshow(wordCloud, interpolation = "bilinear")
      plt.axis('off')
      return plt

def SentimentAnalysis(df):
      # first clean the text
      text= df['Tweets']

      def cleanText(text):
            text= re.sub(r'@[A-Za-z0-9]+', '',text) # Removed @mentions
            text= re.sub(r'#', '',text) # the '#' symbol
            text= re.sub(r':', '',text) # the ':' symbol
            text= re.sub(r'RT[\s]+', '',text) # Removed RT
            text= re.sub(r'https?:\/\/\s+', '',text) # Removed the hyper link
            return text

      #clean tweets
      df['Tweets']= df['Tweets'].apply(cleanText)

      #function to get the subjectivity
      def getSubjectivity(text=df['Tweets']):
            return TextBlob(text).sentiment.subjectivity
      #function to ge the polarity
      def getPolarity(text=df['Tweets']):
            return TextBlob(text).sentiment.polarity
      #Create to new columns
      df['Subjectivity']= df['Tweets'].apply(getSubjectivity)
      df['Polarity']= df['Tweets'].apply(getPolarity)

      # Function to sentiment
      def getAnalysis(score):
            if score < 0: return 'Negetive'
            elif score == 0: return 'Neutral'
            else: return 'Positive'

      df['Analysis']= df['Polarity'].apply(getAnalysis)
      #show the data
      df= df[['Tweets', 'Likes', 'Time', 'Analysis']].set_index('Tweets')
      return df
    
def export(self):
      return self.df



#Plot the sentiment
# # Plot and visualize the counts
def sentiment_plot(df):
      plt.title('Sentiment Analysis of tweets')
      plt.xlabel('Sentiment')
      plt.ylabel('Counts')
      df['Analysis'].value_counts().plot(kind='bar')
      return plt
    