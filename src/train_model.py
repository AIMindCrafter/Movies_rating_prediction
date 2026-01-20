"""
Train the movie rating prediction model

This script trains a Logistic Regression model for sentiment analysis
using the IMDB dataset.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import pickle
import os

def train_model(data_path=None):
    """
    Train the sentiment analysis model
    
    Args:
        data_path: Path to the IMDB dataset CSV file (default: auto-detect from script location)
    """
    print("Loading dataset...")
    
    # Auto-detect path if not provided
    if data_path is None:
        script_dir = os.path.dirname(os.path.abspath(__file__))
        project_root = os.path.dirname(script_dir)
        data_path = os.path.join(project_root, 'archive', 'IMDB Dataset.csv')
    
    # Check if dataset exists
    if not os.path.exists(data_path):
        print(f"Error: Dataset not found at {data_path}")
        print("Please download the IMDB dataset and place it in the archive/ directory")
        print("Dataset: https://www.kaggle.com/datasets/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews")
        return
    
    # Load data
    df = pd.read_csv(data_path)
    print(f"Dataset loaded: {len(df)} reviews")
    
    # Prepare data
    X = df['review']
    y = df['sentiment'].map({'positive': 1, 'negative': 0})
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )
    
    print("Vectorizing text...")
    # Vectorize text
    vectorizer = TfidfVectorizer(max_features=5000)
    X_train_vec = vectorizer.fit_transform(X_train)
    X_test_vec = vectorizer.transform(X_test)
    
    print("Training model...")
    # Train model
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train_vec, y_train)
    
    # Evaluate
    y_pred = model.predict(X_test_vec)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"\nModel Accuracy: {accuracy:.4f}")
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred, target_names=['Negative', 'Positive']))
    
    # Save model and vectorizer
    print("\nSaving model and vectorizer...")
    
    # Use absolute path to save models
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    app_dir = os.path.join(project_root, 'app')
    os.makedirs(app_dir, exist_ok=True)
    
    model_path = os.path.join(app_dir, 'model.pkl')
    vectorizer_path = os.path.join(app_dir, 'vectorizer.pkl')
    
    with open(model_path, 'wb') as f:
        pickle.dump(model, f)
    
    with open(vectorizer_path, 'wb') as f:
        pickle.dump(vectorizer, f)
    
    print("Model and vectorizer saved successfully!")
    print(f"Files saved:")
    print(f"  - {model_path}")
    print(f"  - {vectorizer_path}")

if __name__ == "__main__":
    train_model()
