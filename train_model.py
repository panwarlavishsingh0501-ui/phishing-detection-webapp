import pandas as pd
from sklearn.linear_model import LogisticRegression
import joblib
import os

# Dataset load karo
data = pd.read_csv("data/phishing_dataset.csv")

X = data.drop("label", axis=1)   # Features
y = data["label"]                # Target

# Model train karo
model = LogisticRegression(max_iter=1000)
model.fit(X, y)

# Save trained model
os.makedirs("models", exist_ok=True)
joblib.dump(model, "models/phishing_model.pkl")

print("✅ Trained phishing detection model saved successfully!")
