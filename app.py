import numpy as np
from flask import Flask, request, jsonify, render_template
import joblib

# Create the flask app
app = Flask(__name__)

# Load the trained model
model = joblib.load('house_price_model.pkl')

# Define the homepage route
@app.route('/')
def home():
    # Render the index.html template
    return render_template('index.html')

# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the values from the form and convert them to floating-point numbers
    features = [float(x) for x in request.form.values()]
    
    # Put the features into a NumPy array in the correct shape for the model
    final_features = [np.array(features)]
    
    # Make a prediction using the loaded model
    prediction = model.predict(final_features)

    # Format the output to be a currency string
    output = f"${prediction[0]:,.2f}"

    # Render the index.html page again, but this time with the prediction text
    return render_template('index.html', prediction_text=f'Predicted House Price: {output}')

# Run the app
if __name__ == "__main__":
    app.run(debug=True)