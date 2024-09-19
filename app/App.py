from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/')
def home():
    return "Welcome to the Iris Classification API!"

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        df = pd.DataFrame(data)

        # Check if the DataFrame has the correct columns
        required_columns = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
        if not all(col in df.columns for col in required_columns):
            return jsonify({"error": "Missing required columns"}), 400

        # Make predictions using the trained model
        predictions = model.predict(df)

        # Map numerical labels back to species names
        species_map = {0: 'setosa', 1: 'versicolor', 2: 'virginica'}
        predictions = [species_map[pred] for pred in predictions]

        return jsonify({"predictions": predictions})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
