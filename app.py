from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the model at startup
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get temperature from form
        temp = request.form.get('temperature')
        if not temp:
            return jsonify({'error': 'Temperature is required'}), 400

        # Validate input: must be numeric
        try:
            temp = float(temp)
        except ValueError:
            return jsonify({'error': 'Temperature must be a number'}), 400

        # Make prediction
        prediction = model.predict(np.array([[temp]]))[0]
        # Round to 2 decimal places
        prediction = round(prediction, 2)

        return jsonify({'prediction': prediction})

    except Exception as e:
        return jsonify({'error': 'An error occurred during prediction'}), 500

if __name__ == '__main__':
    app.run(debug=True)