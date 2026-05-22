# import joblib
# import pandas as pd
# from src.classifier.vectorizer import transform_text


# class ThreatClassifier:

#     def __init__(self):

#         self.model = joblib.load("models/classifier.pkl")
#         self.vectorizer = joblib.load("models/vectorizer.pkl")

#     def predict(self, text):
#         if self.model is None:
#             raise ValueError("Model not loaded")
        
#         X = self.vectorizer.transform([text])
#         prediction = self.model.predict(X)

#         return prediction[0]

import joblib
import numpy as np
from src.classifier.embeddings import generate_embedding

class ThreatClassifier:

    def __init__(self):
        self.model = joblib.load("models/classifier.pkl")

    def predict(self, text):

        embedding = generate_embedding(text)
        X = np.array([embedding])

        return self.model.predict(X)[0]