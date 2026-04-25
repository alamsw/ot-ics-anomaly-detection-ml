from sklearn.ensemble import IsolationForest

def build_model():
    model = IsolationForest(
        n_estimators=100,
        contamination=0.1,
        random_state=42
    )
    return model