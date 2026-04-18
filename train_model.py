from sklearn.linear_model import LogisticRegression
import joblib
import os

# Ensure models folder exists
os.makedirs("models", exist_ok=True)

# Dummy model banate hain (sirf testing ke liye)
dummy_model = LogisticRegression()
joblib.dump(dummy_model, "models/phishing_model.pkl")

print("Dummy model saved successfully!")
