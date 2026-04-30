from flask import Flask, render_template, request
import os, joblib
import pandas as pd
from utils.feature_extraction import extract_features

app = Flask(__name__)

# Load trained ML model
model_path = os.path.join(os.path.dirname(__file__), "models", "phishing_model.pkl")
model = joblib.load(model_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    url = request.form["url"]

    # Extract features as dict
    features = extract_features(url)

    # Convert dict → DataFrame with same feature names
    feature_df = pd.DataFrame([features])

    # Predict
    prediction = model.predict(feature_df)[0]
    result = "Phishing" if prediction == 1 else "Legitimate"

    # Pass dict to template
    return render_template("result.html", url=url, result=result, features=features)

if __name__ == "__main__":
    app.run(debug=True)
