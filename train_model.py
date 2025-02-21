import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Sample dataset
data = {
    'qualification_match': [1, 0, 1, 0, 1, 0, 0, 1, 1, 0],
    'experience_years': [5, 1, 10, 2, 8, 1, 0, 7, 6, 1],
    'interview_rounds': [3, 1, 4, 1, 3, 2, 1, 3, 3, 1],
    'time_to_hire_days': [30, 3, 45, 2, 40, 4, 1, 35, 32, 2],
    'referral_connection': [0, 1, 0, 1, 0, 1, 1, 0, 0, 1],
    'salary_increase_percent': [10, 100, 5, 90, 12, 85, 95, 8, 7, 80],
    'hiring_fraud': [0, 1, 0, 1, 0, 1, 1, 0, 0, 1]  # 1 = Fraud, 0 = Legitimate
}

df = pd.DataFrame(data)

# Prepare dataset
X = df.drop(columns=['hiring_fraud'])
y = df['hiring_fraud']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'hiring_fraud_model.pkl')

print("✅ Model trained and saved as 'hiring_fraud_model.pkl'")
