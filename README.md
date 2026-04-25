# AI-Based Anomaly Detection for OT/ICS Network Traffic

## 📌 Overview
This project implements a machine learning-based anomaly detection system designed to simulate intrusion detection in Operational Technology (OT) environments.

## 🎯 Objective
Detect abnormal network behavior using unsupervised learning techniques, aligned with industrial cybersecurity monitoring use cases.

## 🧠 Approach
- Data preprocessing and feature engineering
- Isolation Forest for anomaly detection
- Evaluation using classification metrics

## 📊 Dataset
NSL-KDD dataset (network intrusion detection benchmark)

## Data Preprocessing
Data preprocessing and dataset conversion from NSL-KDD format were performed using Jupyter Notebook (see notebooks folder).

## ⚙️ Technologies Used
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib

## 📓 Notebooks

- `01_data_exploration.ipynb` → data analysis and preprocessing
- `02_model_execution.ipynb` → model training and evaluation workflow
  
## 📊 Results & Observations

- Dataset is highly imbalanced (~99% attack traffic)
- Isolation Forest achieved:
  - High recall for normal traffic (~80%)
  - Moderate detection of anomalous activity (~40%)

## ⚠️ Challenges

- Imbalanced dataset significantly impacts anomaly detection performance
- Model sensitivity depends on contamination parameter

## 🔧 Improvements

- Tuned contamination parameter to improve anomaly detection
- Future work includes:
  - Autoencoder-based detection
  - Data balancing techniques

## 🔐 Relevance to OT Security
This project simulates anomaly detection mechanisms used in industrial cybersecurity platforms (e.g., OT network monitoring and threat detection systems).

## 🚀 Future Improvements
- Deep learning (Autoencoders)
- Real-time detection pipeline
- Integration with SIEM tools

## 👤 Author
Syed Wasi Alam
