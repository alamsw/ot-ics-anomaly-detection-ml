import os
from preprocessing import prepare_data
from model import build_model
import joblib

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

data_path = os.path.join(BASE_DIR, "data", "nsl_kdd_train.csv")
output_path = os.path.join(BASE_DIR, "outputs", "model.pkl")

# Load data
X, y = prepare_data(data_path)

# Train model
model = build_model()
model.fit(X)

# Save model
joblib.dump(model, output_path)

print("Model trained and saved successfully.")