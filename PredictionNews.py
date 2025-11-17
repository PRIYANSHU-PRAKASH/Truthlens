
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from textblob import TextBlob

def sentiment(tweet):							#Sentiment analysis of news
        analysis = TextBlob(tweet)
       
        if analysis.sentiment.polarity > 0:
            return 'positive'
        elif analysis.sentiment.polarity == 0:
            return 'positive'
        else:
            return 'negative'   

def process(path,X_test):
	df = pd.read_csv(path)
	print(df.head())
	X_train=df["text"]
	y = df.label
	
	X_test=[X_test]

	#X_test=["Iran reportedly makes new push for uranium concessions in nuclear talks"]  Example format for testing
	
	print(X_train)
	print(X_test)
	
	tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)    # This removes words which appear in more than 70% of the articles
	tfidf_train = tfidf_vectorizer.fit_transform(X_train) 
	tfidf_test = tfidf_vectorizer.transform(X_test)

	
	clf = MultinomialNB(alpha=.01, fit_prior=True)
	clf.fit(tfidf_train, y)
	pred1 = clf.predict(tfidf_test)
	print(pred1)
	
	pred2 =sentiment(str(X_test))
	print(pred2)

	return pred1[0],pred2


