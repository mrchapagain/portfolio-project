# Analytics functions
import re
#from PIL import Image
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator 
from tkinter import *
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import seaborn as sns


import spacy.cli
#spacy.cli.download("en_core_web_lg")
#nlp = spacy.load('en_core_web_lg')
from nltk.stem.snowball import SnowballStemmer    


def SentimentAnalysis(df):
      # first clean the text
      def cleanText(text):
            text= re.sub(r'@[A-Za-z0-9]+', '',text) # Removed @mentions
            text= re.sub(r'#', '',text) # the '#' symbol
            text= re.sub(r':', '',text) # the ':' symbol
            text= re.sub(r'RT[\s]+', '',text) # Removed RT
            text= re.sub(r'https?:\/\/\s+', '',text) # Removed the hyper link
            return text

      text= df['Tweets']
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
      # add Analytics column in the data frame
      df['Analysis']= df['Polarity'].apply(getAnalysis)
      #show the data
      df_withsentiment= df
      return df_withsentiment
    
#def export(self):return self.df

#Plot the sentiment dataframe
def get_graph():
      buffer= BytesIO()
      plt.savefig(buffer, format='png')
      buffer.seek(0)
      image_png=buffer.getvalue()
      graph= base64.b64encode(image_png)
      graph= graph.decode('utf-8')
      buffer.close()
      return graph

def sentiment_plot(df_withsentiment, title):
      plt.switch_backend('AGG')
      plt.figure(figsize=(4,3))
      plt.title(title, fontsize=10)
      #plt.bar(df_withsentiment.Analysis.unique(), df_withsentiment['Analysis'].value_counts(), color ='grey', width = 0.4)
      #sns.barplot(df_withsentiment['Analysis'], df_withsentiment['Analysis'].value_counts())
      df_withsentiment['Analysis'].value_counts().plot(kind='bar')
      plt.xticks(rotation=20)
      plt.xlabel('Sentiment of the tweets')
      plt.ylabel('Counts of sentiments')
      plt.tight_layout()
      graph=get_graph()
      return graph

def wordcloud_plot(df_col, title):
      # Create stopword list
      stopwords = set(STOPWORDS)
      stopwords.update(['https', 'er', 'og', 't', 'co', 'en', 'før', 'fra', 'se', 'har', 'vil', 'nyt', 'end', 
      'kan', 'så', 'på', 'som', 'nu', 'ikke', 'men', 'om', 'vi', 'et', 'af', 'var'])
      plt.switch_backend('AGG')
      plt.figure(figsize=(4,3))
      plt.title(title, fontsize=10)
      allWords= ' '.join( [twts for twts in df_col] )
      wordcloud = WordCloud(stopwords=stopwords, max_words=50, width= 390, height=290, random_state=21, max_font_size= 100, background_color="skyblue").generate(allWords)
      plt.imshow(wordcloud, interpolation = "bilinear")
      plt.axis('off')
      plt.tight_layout()
      graph=get_graph()
      return graph


## Function to find most mentioned words with NLP
def most_mentioned_words(df_by_id):
      # Split all the sentances and creat the list of sentence of from the tweet columns
      list_of_sentences = [sentence for sentence in df_by_id.Tweets]

      lines = []
      for sentence in list_of_sentences:
            words = sentence.split()
            for w in words:
                  lines.append(w)

      # Removing Punctuation by using Regular Expression (RegEx)
      lines = [re.sub(r'[^A-Za-z0-9]+', '', x) for x in lines]
      lines2= []
      for word in lines:
            if word != '':
                  lines2.append(word)
      
      # Stemming the words to their root
      s_stemmer = SnowballStemmer(language='english')
      stem= []
      for word in lines2:
            stem.append(s_stemmer.stem(word))

      # Removing all the stop words
      stem2= []
      for word in stem:
            if word not in nlp.Defaults.stop_words:
                  stem2.append(word)
      # Time to creat Dataframe 
      df2 = pd.DataFrame(stem2)
      df2 = df2[0].value_counts()
      
      # Lets visualize
      def vis(df2):
            df2= df2[:20,]
            plt.figure()
            sns.barplot(df2.values, df2.index, alpha=1)
            plt.title(f'Top words Overall from Tweet search')
            plt.ylabel('Word from Tweet')
            plt.xlabel('Count of Words')
      return vis(df2)