import pandas as pd
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
import joblib

df = pd.read_csv('reviews.tsv', delimiter='\t')
corpus = []
for i in range(0, 11198):
    review = re.sub(pattern='[^a-zA-Z]', repl=' ', string=df['content'][i])
    review = review.lower()
    review_words = review.split()
    review_words = [word for word in review_words if not word in set(
        stopwords.words('english'))]
    ps = PorterStemmer()
    review = [ps.stem(word) for word in review_words]
    review = ' '.join(review)
    corpus.append(review)
cv = CountVectorizer(max_features=50)
X = cv.fit_transform(corpus).toarray()
y = df.score
joblib.dump(cv, "assets/cv.pkl")
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
classifier = MultinomialNB(alpha=0.2)
classifier.fit(X_train, y_train)
joblib.dump(classifier, "assets/model.pkl")