from flask import Flask, render_template, request
import joblib
from utils.feature_extraction import extract_features

app = Flask(__name__)

# Load trained ML model
model = joblib.load("models/phishing_model.pkl")

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

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
