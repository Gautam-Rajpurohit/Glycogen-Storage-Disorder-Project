from flask import Flask, render_template, request
import pickle
import numpy as np

# Initialize the Flask app
app = Flask(__name__)

# Load the trained GSD model
with open('gsd_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Define the home route that serves the form
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction route that processes the form submission
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract input values from the form
        input_features = [float(request.form[f'param{i+1}']) for i in range(9)]  # 9 input parameters
        blood_sugar = input_features[0]  # param1 is Blood Sugar

        # Initialize result message
        result = ""
        override = False

        # Check if Blood Sugar is above 100
        if blood_sugar > 100:
            result = 'Negative for GSD'
            override = True
        else:
            # Convert to array for model input
            input_array = np.array([input_features])

            # Use the model to make a prediction
            prediction = model.predict(input_array)

            # Convert the prediction result to a readable format
            result = 'Positive for GSD' if prediction[0] == 1 else 'Negative for GSD'

        # Additional message if override occurred
        if override:
            override_message = ""
        else:
            override_message = None

    except Exception as e:
        result = 'Error in processing the input. Please ensure all values are correct.'
        override_message = None

    # Render the result back to the form page
    return render_template('index.html', prediction_text=result, override_message=override_message)

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
