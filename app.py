from flask import Flask, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load model
model = joblib.load("models/model.pkl")

# Home route
@app.route("/")
def home():

    return """
    <h1 style="color:blue;"> Flight Duration Prediction API</h1>

    <form action="/predict" method="post">

        <label>Distance Travelled (KM):</label>

        <input type="number" name="distance" required><br><br>

        <input type="submit" value="Predict Flight Time">

    </form>
    """

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():

    try:

        distance = float(request.form["distance"])

        input_df = pd.DataFrame({
            "DistanceKM": [distance]
        })

        prediction = model.predict(input_df)

        predicted_hours = float(prediction[0])

        return f"""
        <h1 style="color:blue;">Flight Duration Prediction Result</h1>

        <hr>

        <p><b>Distance Travelled:</b> {distance} KM</p>

        <p><b>Estimated Flight Duration:</b> {round(predicted_hours, 2)} Hours</p>

        <br>

        <a href="/">Predict Another Flight</a>
        """

    except Exception as e:

        return f"Error: {str(e)}"

# Run app
if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)