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
        # Get form values correctly
        data = [
            float(request.form['qualification_match']),
            float(request.form['experience_years']),
            float(request.form['interview_rounds']),
            float(request.form['time_to_hire_days']),
            float(request.form['referral_connection']),
            float(request.form['salary_increase_percent'])
        ]

        # Predict with the model
        prediction = model.predict([data])
        result = "🚨 Fraud Detected" if prediction[0] == 1 else "✅ Legitimate Hiring"

        return render_template('index.html', prediction_text=result)

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(debug=True)
