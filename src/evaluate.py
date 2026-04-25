import os
import joblib
import pandas as pd
from preprocessing import prepare_data
from sklearn.metrics import classification_report, confusion_matrix

# Base directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Paths
test_path = os.path.join(BASE_DIR, "data", "nsl_kdd_test.csv")
model_path = os.path.join(BASE_DIR, "outputs", "model.pkl")

# Load data
X_test, y_test = prepare_data(test_path)

# Load model
model = joblib.load(model_path)

# Predict
preds = model.predict(X_test)

# Convert Isolation Forest output
# -1 = anomaly → 1
#  1 = normal → 0
preds = [1 if p == -1 else 0 for p in preds]

# Evaluation
print("Classification Report:")
print(classification_report(y_test, preds))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, preds))
print(classification_report(y_test, preds, zero_division=0))