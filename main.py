from flask import Flask, request
import pandas as pd
import numpy as np
from scipy.stats import norm
import joblib

app = Flask(__name__)

# Load model and residual std (update paths if needed)
print("🔄 Cargando modelo y residuos...")
model = joblib.load('/home/datv/mysite/best_model.pkl')
residual_std = joblib.load('/home/datv/mysite/residual_std.pkl')
print(f"✅ Todo cargado! Residual std: {residual_std:.4f}")

@app.route('/predice', methods=['POST'])
def predict():
    data = request.json
    features = data['features']
    confidence = data.get('confidence', 0.95)

    pred = model.predict([features])[0]

    z_score = norm.ppf(1 - (1 - confidence) / 2)
    margin = z_score * residual_std

    return {
        'prediction': float(pred),
        'lower': float(pred - margin),
        'upper': float(pred + margin),
        'confidence': confidence
    }

if __name__ == "__main__":
    app.run(port=8000, debug=True)
