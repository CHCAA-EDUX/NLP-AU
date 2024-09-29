from sklearn.feature_extraction.text import CountVectorizer

texts = ["This is a text", "This is another text", "This is also a text"]
vectorizer = CountVectorizer()
embeddings = vectorizer.fit_transform(texts)

vectorizer.get_feature_names_out()
# array(['also', 'another', 'is', 'text', 'this'])

embeddings.toarray()
# array([[0, 0, 1, 1, 1],
#        [0, 1, 1, 1, 1],
#        [1, 0, 1, 1, 1]])


# tokenization
texts = ["isn't this a word?"]
vectorizer = CountVectorizer()

embeddings = vectorizer.fit_transform(texts)
vectorizer.get_feature_names_out()

embeddings = vectorizer.fit_transform(["CASING MATTERS!"])
vectorizer.get_feature_names_out()

# N grams
texts = ["This is a text", "This is another text", "This is also a text"]

vectorizer = CountVectorizer(ngram_range=(1, 3))
embeddings = vectorizer.fit_transform(texts)
vectorizer.get_feature_names_out()


# tf-idf
from sklearn.feature_extraction.text import TfidfVectorizer

texts = ["This is a text", "This is another text", "This is also a text"]
vectorizer = TfidfVectorizer()

embeddings = vectorizer.fit_transform(texts)

vectorizer.get_feature_names_out()

embeddings.toarray()