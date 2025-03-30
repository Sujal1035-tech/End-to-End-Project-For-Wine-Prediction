from flask import Flask, render_template, request
import pandas as pd
from mlProject.pipeline.prediction import PredictionPipeline  # Ensure correct path

app = Flask(__name__)  # Initialize Flask app

# Feature names exactly as seen during training
FEATURE_NAMES = [
    "fixed acidity", "volatile acidity", "citric acid", "residual sugar",
    "chlorides", "free sulfur dioxide", "total sulfur dioxide", "density",
    "pH", "sulphates", "alcohol"
]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract form data and map to correct feature names
        data = {name: float(request.form[name.replace(" ", "_")]) for name in FEATURE_NAMES}

        # Convert to DataFrame
        df = pd.DataFrame([data])

        # Prediction
        predictor = PredictionPipeline()
        prediction = predictor.predict(df)  # Ensure it returns a valid response

        return render_template('result.html', prediction=f"Predicted Wine Quality: {round(prediction[0], 2)}")

    except Exception as e:
        print(f"Error: {e}")
        return render_template("index.html", prediction_text=f"Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
