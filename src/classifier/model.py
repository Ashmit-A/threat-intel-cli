from src.classifier.baseline import classify_threat

class ThreatClassifier:

    def __init__(self, model=None):
        self.model = model

    def predict(self, features):
        if self.model:
            return self.model.predict(features)
        else:
            return classify_threat(features)