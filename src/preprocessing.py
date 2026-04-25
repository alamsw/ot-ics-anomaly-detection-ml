import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_data(path):
    return pd.read_csv(path)


def encode_categorical(df):
    df = df.copy()
    for col in df.select_dtypes(include='object').columns:
        if col != 'label':
            df[col] = LabelEncoder().fit_transform(df[col])
    return df


def scale_features(df):
    scaler = StandardScaler()
    X = df.drop('label', axis=1)
    X_scaled = scaler.fit_transform(X)
    return X_scaled


def prepare_data(path):
    df = load_data(path)
    
    df['label'] = df['label'].apply(lambda x: 0 if x == 0 else 1)
    
    df = encode_categorical(df)
    X = scale_features(df)
    y = df['label']

    print(df['label'].value_counts())
    
    return X, y

    