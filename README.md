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

## 📁 Outputs

- `model.pkl` → trained anomaly detection model  
- `results.csv` → prediction results with anomaly scores for each sample

## 📊 Visualizations

### Confusion Matrix
![Confusion Matrix](outputs/confusion_matrix.png)

### Anomaly Score Distribution
![Anomaly Scores](outputs/anomaly_scores.png)

### Top detected anomalous network events
       actual_label  predicted_label  anomaly_score
11765             0                1      -0.172046
967               1                1      -0.147219
19577             1                1      -0.146050
17619             1                1      -0.142540
19839             1                1      -0.140538
2421              0                1      -0.138778
3445              1                1      -0.136717
3621              1                1      -0.136243
2433              1                1      -0.134725
20555             0                1      -0.133757

## ⚠️ Challenges

- Imbalanced dataset significantly impacts anomaly detection performance
- Model sensitivity depends on contamination parameter

## 🔧 Improvements

- Tuned contamination parameter to improve anomaly detection
- Future work includes:
  - Autoencoder-based detection
  - Data balancing techniques
    
## 🧠 Key Takeaways

- Implemented anomaly detection pipeline using Isolation Forest  
- Addressed real-world challenges such as dataset imbalance  
- Applied ML techniques to simulate OT/ICS intrusion detection scenarios  
- Demonstrated end-to-end workflow: data → model → evaluation → results  

## 🎯 Relevance

This project reflects real-world use cases in:
- OT network monitoring  
- Threat detection systems  
- Security analytics platforms
    
## 🔐 Relevance to OT Security
This project simulates anomaly detection mechanisms used in industrial cybersecurity platforms (e.g., OT network monitoring and threat detection systems).

## 🚀 Future Improvements
- Deep learning (Autoencoders)
- Real-time detection pipeline
- Integration with SIEM tools

## 👤 Author
Syed Wasi Alam
