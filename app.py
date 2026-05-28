from flask import Flask, render_template, request
import pickle
import numpy as np

# Load Model
with open("SLR_MODEL.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template("index.html")


# Prediction Route
@app.route('/predict', methods=['POST'])
def predict():

    try:
        # Get input value
        experience = float(request.form['experience'])

        # Convert into array for prediction
        features = np.array([[experience]])

        # Predict salary
        prediction = model.predict(features)

        output = round(prediction[0], 2)

        return render_template(
            "index.html",
            prediction_text=f"Predicted Salary is ₹ {output}"
        )

    except:
        return render_template(
            "index.html",
            prediction_text="Please Enter Valid Input"
        )


if __name__ == "__main__":
    app.run(debug=True)