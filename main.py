from flask import Flask
from flask import request
import pandas as pd
import numpy as np
from scipy.stats import norm
import joblib



app = Flask(__name__)

print("🔄 Cargando modelo y residuos...")
model = joblib.load('best_model.pkl')
residual_std = joblib.load('residual_std.pkl')
print(f"✅ Todo cargado! Residual std: {residual_std:.4f}")

@app.route('/predice', methods=['POST'])
def predict():

        # Obtener datos
        data = request.json
        features = data['features']
        confidence = data.get('confidence', 0.95)
        # Predicción
        pred = model.predict([features])[0]

        # Intervalo
        z_score = norm.ppf(1 - (1-confidence)/2)
        margin = z_score * residual_std

        return {
        'prediction': float(pred),
        'lower': float(pred - margin),
        'upper': float(pred + margin),
        'confidence': confidence
        }


if __name__ == "__main__":
    app.run(port=8000, debug=True)
