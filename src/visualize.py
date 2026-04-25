import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
results_path = os.path.join(BASE_DIR, "outputs", "results.csv")
fig_path = os.path.join(BASE_DIR, "outputs", "confusion_matrix.png")

df = pd.read_csv(results_path)

cm = confusion_matrix(df["actual_label"], df["predicted_label"])

plt.figure()
plt.imshow(cm)
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.colorbar()

for i in range(cm.shape[0]):
    for j in range(cm.shape[1]):
        plt.text(j, i, cm[i, j], ha="center", va="center")

plt.savefig(fig_path)
plt.close()

print(f"Saved: {fig_path}")

plt.figure()
df["anomaly_score"].hist(bins=50)
plt.title("Anomaly Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

score_fig = os.path.join(BASE_DIR, "outputs", "anomaly_scores.png")
plt.savefig(score_fig)
plt.close()

print(f"Saved: {score_fig}")