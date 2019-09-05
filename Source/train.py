import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from collections import defaultdict
from sklearn.model_selection import train_test_split
import nltk
nltk.download('stopwords')
from joblib import dump

# Loading 
input_train = pd.read_csv("input_train.csv")
output_train = pd.read_csv("output_train.csv")

# Finally adding the french stopwords
sw = set()
#sw.update(most_freq)   # Temporary commented otherwise would need to serialize them in order to load them in the api_container for prediction
sw.update(tuple(nltk.corpus.stopwords.words('french')))

# Random split 
X = input_train['question']
y = output_train['intention']
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.30, random_state=42)

# Classic TF-IDF with the computed stopword, not using stemming
count_vect = CountVectorizer(stop_words=sw)
X_train_counts = count_vect.fit_transform(X_train)
transformer = TfidfTransformer()
tfidf_vector_train = transformer.fit_transform(X_train_counts)

# NB should be little better than a SVM on an umballanced dataset
clf = MultinomialNB().fit(tfidf_vector_train, y_train)

pipeline = Pipeline([('vect', CountVectorizer(ngram_range=(1,2))), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB(alpha=0.01, class_prior = None, fit_prior = True))])

text_clf = pipeline.fit(X_train, y_train)

# Model persistence
model_filename = 'text_clf.joblib.z'
dump(text_clf, model_filename)

print("Training done !")