from flask import Flask, render_template, request
import os, joblib
from utils.feature_extraction import extract_features

# Flask app initialize
app = Flask(__name__)

# Load trained ML model (absolute path safe for Render)
model_path = os.path.join(os.path.dirname(__file__), "models", "phishing_model.pkl")
model = joblib.load(model_path)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check():
    url = request.form["url"]
    features = extract_features(url)
    prediction = model.predict([features])[0]

    result = "Phishing" if prediction == 1 else "Legitimate"
    return render_template("result.html", url=url, result=result, features=features)

if __name__ == "__main__":
    # Local testing (Render will use gunicorn)
    app.run(debug=True)
