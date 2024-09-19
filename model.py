import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import joblib

# Function to train and save the model
def train_model():
    # Load the dataset from the CSV file
    df = pd.read_csv('iris.csv')
    
    # Prepare features and target variable
    X = df[['sepal_length', 'sepal_width', 'petal_length', 'petal_width']]
    y = df['species'].map({'setosa': 0, 'versicolor': 1, 'virginica': 2})
    
    # Split the data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train a simple model (Logistic Regression)
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # Save the trained model using joblib
    joblib.dump(model, 'model.pkl')
    
    print("Model training completed and saved as 'model.pkl'")

# Function to load the trained model
def load_model():
    model = joblib.load('model.pkl')
    return model

if __name__ == "__main__":
    train_model()
