from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load("hiring_fraud_model.pkl")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        input_values = [float(data[key]) for key in data]
        prediction = model.predict([input_values])[0]
        result = "Fraud Detected" if prediction == 1 else "Legitimate Hiring"
        return jsonify({"prediction": result})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(debug=True)
