from flask import Flask, request, jsonify
import joblib
import pandas as pd
import logging
import datetime

app = Flask(__name__)

# Configure logging
logging.basicConfig(
    filename='logs/predictions.log',
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

# Load trained model
model = joblib.load("models/model.pkl")

# Home Route
@app.route("/")
def home():
    return "ML API Running (KBNT)"

# Health Check Endpoint for Monitoring
@app.route("/health")
def health():
    return jsonify({
        "status": "healthy",
        "timestamp": str(datetime.datetime.now())
    })

# Prediction Endpoint
@app.route("/predict", methods=["POST"])
def predict():

    try:
        # Get JSON input
        data = request.json

        # Convert to DataFrame
        input_df = pd.DataFrame([data])

        # Make prediction
        prediction = model.predict(input_df)[0]

        # Log request and prediction
        logging.info(
            f"Input: {data}, Prediction: {prediction}"
        )

        # Return prediction
        return jsonify({
            "prediction": int(prediction)
        })

    except Exception as e:

        logging.error(f"Prediction Error: {str(e)}")

        return jsonify({
            "error": str(e)
        }), 500

# Run Flask App
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
