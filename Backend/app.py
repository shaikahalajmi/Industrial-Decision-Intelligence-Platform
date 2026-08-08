From flask import Flask, request, jsonify
import pandas as pd
import joblib
import os

app = Flask(__name__)

# Load trained machine failure model
MODEL_PATH = os.path.join(
    os.path.dirname(__file__),
    "industrial_failure_model.joblib"
)

model = joblib.load(MODEL_PATH)

# Optimized threshold for failure detection
THRESHOLD = 0.30


@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "Industrial Decision Intelligence API is running"
    })


@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        machine_data = pd.DataFrame([{
            "Type": data["Type"],
            "Air temperature [K]": data["Air temperature [K]"],
            "Process temperature [K]": data["Process temperature [K]"],
            "Rotational speed [rpm]": data["Rotational speed [rpm]"],
            "Torque [Nm]": data["Torque [Nm]"],
            "Tool wear [min]": data["Tool wear [min]"]
        }])

        # Calculate failure probability
        probability = model.predict_proba(machine_data)[0][1]
        prediction = int(probability >= THRESHOLD)

        # Decision intelligence
        if probability >= 0.70:
            risk_level = "Critical"
            recommended_action = (
                "Immediate inspection and maintenance required."
            )

        elif probability >= THRESHOLD:
            risk_level = "High"
            recommended_action = (
                "Schedule a maintenance inspection as soon as possible."
            )

        else:
            risk_level = "Low"
            recommended_action = (
                "Continue normal operation and monitoring."
            )

        return jsonify({
            "failure_probability": round(float(probability) * 100, 2),
            "failure_prediction": prediction,
            "risk_level": risk_level,
            "recommended_action": recommended_action
        })

    except Exception as error:
        return jsonify({
            "status": "error",
            "message": str(error)
        }), 400


if __name__ == "__main__":
    app.run(debug=True)
