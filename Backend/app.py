From flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Industrial Decision Intelligence Platform API is running"
    })

@app.route("/machines")
def machines():
    df = pd.read_csv("../predictive_maintenance.csv")

    return jsonify({
        "total_records": len(df),
        "columns": list(df.columns),
        "sample_data": df.head(5).to_dict(orient="records")
    })

if __name__ == "__main__":
    app.run(debug=True)
