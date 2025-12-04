from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
MODEL_PATH = 'model/realistic_model.pkl'
with open(MODEL_PATH, 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract data from the form
        data = request.form
        
        # Debug print to see what data we're getting
        print(f"Received data: {dict(data)}")
        
        features = np.array([
            float(data['pclass']),
            float(data['age']),
            float(data['sibsp']),
            float(data['parch']),
            float(data['fare']),
            1.0 if data['sex'] == 'male' else 0.0
        ]).reshape(1, -1)

        print(f"Features: {features}")

        # Make prediction
        prediction = model.predict(features)
        print(f"Prediction: {prediction}")
        
        result = 'Survived' if prediction[0] == 1 else 'Did not survive'
        
        print(f"Result: {result}")

        return jsonify({'result': result})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

# For gunicorn deployment
application = app