from flask import Flask, render_template, request
import os, joblib
import pandas as pd
from utils.feature_extraction import extract_features

app = Flask(__name__)

# Load trained ML model
model_path = os.path.join(os.path.dirname(__file__), "models", "phishing_model.pkl")
model = joblib.load(model_path)

# Risk score function
def calculate_score(features):
    score = 0

    # HTTPS missing → risky
    if features["has_https"] == 0:
        score += 30

    # Suspicious words present → risky
    if features["suspicious_words"] == 1:
        score += 40

    # Long URL → risky
    if features["url_length"] > 100:
        score += 30

    return min(score, 100)  # normalize to 100

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    url = request.form["url"]

    # Extract features
    features = extract_features(url)

    # ML prediction
    feature_df = pd.DataFrame([features])
    prediction = model.predict(feature_df)[0]
    result = "Phishing" if prediction == 1 else "Legitimate"

    # Risk score
    risk_score = calculate_score(features)

    return render_template("result.html", url=url, result=result, score=risk_score, features=features)

if __name__ == "__main__":
    app.run(debug=True)
