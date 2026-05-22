import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib
import numpy as np
from src.classifier.pipeline_features import build_embedding_matrix
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report


df = pd.read_csv("data/processed/training_data.csv")

# vector embedded features
X = build_embedding_matrix(df["text"])


# Labels
y = df["severity"]

# Save embeddings and labels for future use
np.save("models/train_embeddings.npy", X)
np.save("models/train_labels.npy", y)


# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)

model.fit(X_train, y_train)

predictions = model.predict(X_test)

print(classification_report(y_test, predictions))

# Save model
joblib.dump(model, "models/classifier.pkl")
print("Model trained and saved.")