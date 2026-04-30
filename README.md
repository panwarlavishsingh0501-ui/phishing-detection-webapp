# 🚀 Hybrid Risk Scoring Based Anomaly Detection System for Phishing Website Identification

## 📌 Overview
This is a **Flask-based web application** that detects phishing websites using a **Hybrid Risk Scoring + Machine Learning model**.  
It evaluates URLs based on multiple features and provides:
- **Prediction (Phishing / Legitimate)**
- **Risk Score (0–100%)**
- **Feature Breakdown**

---

## 🛠️ Tech Stack
- Python 3
- Flask (Web Framework)
- scikit-learn (ML Model)
- pandas (Data Handling)
- joblib (Model Persistence)
- HTML + CSS (Frontend Styling)
- Render (Deployment)

---

## 📂 Project Structure
phishing-detection-webapp/
│
├── data/                     # Dataset (CSV)
├── models/                   # Saved ML model (phishing_model.pkl)
├── utils/                    # Feature extraction script
│   └── feature_extraction.py
├── templates/                # HTML templates
│   ├── index.html
│   └── result.html
├── static/css/               # CSS styling
│   └── style.css
├── app.py                    # Flask application
├── train_model.py            # Model training script
├── requirements.txt          # Dependencies
└── README.md                 # Project documentation
