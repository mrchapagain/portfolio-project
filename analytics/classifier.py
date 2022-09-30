# Analytics functions
import re
from textblob import TextBlob
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import seaborn as sns
import pandas as pd

#Librarry for stoppwworods (Spacy is better than NLTK)

from spacy.lang.en.stop_words import STOP_WORDS as en_stop #stopwords in English
from spacy.lang.da.stop_words import STOP_WORDS as da_stop #stopwords in Danish
final_stopwords= en_stop.union(da_stop)

#import spacy.cli
#spacy.cli.download("en_core_web_lg")
#nlp = spacy.load('en_core_web_lg')
#from nltk.stem.snowball import SnowballStemmer   
#s_stemmer = SnowballStemmer(language='english') 

#Libraruies for Lexicon Normalization (Stemming & Lemmatization)
import nltk
#nltk.download('omw-1.4')
#nltk.download('wordnet')

#for stemming
#from nltk.stem.snowball import SnowballStemmer   
#s_stemmer = SnowballStemmer(language='english') 
#for Lemmatization
from nltk.stem.wordnet import WordNetLemmatizer


# Function to clean text
def cleanText(text):
      text= re.sub(r'@[A-Za-z0-9]+', '',text) # Removed @mentions
      text= re.sub(r'#', '',text) # the '#' symbol
      text= re.sub(r':', '',text) # the ':' symbol
      text= re.sub(r'RT[\s]+', '',text) # Removed RT
      text= re.sub(r'https?:\/\/\s+', '',text) # Removed the hyper link
      return text

def SentimentAnalysis(df):
      text= df['Tweets']
      #clean tweets
      df['Tweets']= text.apply(cleanText)

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
      plt.title(title, fontsize=8)
      #plt.bar(df_withsentiment.Analysis.unique(), df_withsentiment['Analysis'].value_counts(), color ='grey', width = 0.4)
      sns.countplot(data= df_withsentiment, x= 'Analysis', palette= {"Neutral": "blue", "Negetive": "red", "Positive": "green"})
      #df_withsentiment['Analysis'].value_counts().plot(kind='bar', color= {"Neutral": "blue", "Negetive": "red", "Positive": "green"})
      plt.xticks(rotation=20)
      plt.xlabel('Sentiment of the tweets')
      plt.ylabel('Counts of sentiments')
      plt.tight_layout()
      graph=get_graph()
      return graph

def wordcloud_plot(df_col, title):
      #lets clean the xext first
      df_col= df_col.apply(cleanText)
      # Create stopword list
      final_stopwords.update(['https', 'er', 'og', 't', 'co', 'A', 't','The'])
      plt.switch_backend('AGG')
      plt.figure(figsize=(8,4))
      plt.title(title, fontsize=8)
      allWords= ' '.join( [twts for twts in df_col] )
      wordcloud = WordCloud(stopwords=final_stopwords, max_words=100, width= 800, height=400, random_state=21, max_font_size= 75, background_color="skyblue").generate(allWords)
      plt.imshow(wordcloud, interpolation = "bilinear")
      plt.axis('off')
      plt.tight_layout()
      graph=get_graph()
      return graph


## Function to find most mentioned words with NLP
def most_mentioned_words(df_by_id, keyword):
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
      
      # Removing all the stop words
      stem= []
      for word in lines2:
            if word not in final_stopwords: #nlp.Defaults.stop_words:
                  stem.append(word)
                              
      # Stemming the words to their root
      #s_stemmer = SnowballStemmer(language='english')
      #stem2= []
      #for word in stem:
            #stem2.append(s_stemmer.stem(word))

      # Lematization all the stop words
      lem = WordNetLemmatizer()
      stem3=[]
      for word in stem:
            stem3.append(lem.lemmatize(word))

      # Time to creat Dataframe 
      df2 = pd.DataFrame(stem3)
      df2 = df2[0].value_counts()
      
      # Lets visualize
      def vis(df2):
            df2= df2[:10,]
            plt.switch_backend('AGG')
            plt.figure(figsize=(4,3))
            sns.barplot(df2.values, df2.index, alpha=1)
            #plt.xticks(rotation=20)
            plt.title(f'Top {df2.index.shape} words from Tweet search with {keyword}', fontsize=8)
            plt.ylabel('Word from Tweet')
            plt.xlabel('Count of Words')
            plt.tight_layout()
            graph=get_graph()
            return graph
      return vis(df2)
      
