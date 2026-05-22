from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()

def fit_vectorizer(texts):

    X = vectorizer.fit_transform(texts)

    return X

def transform_text(texts):

    return vectorizer.transform(texts)