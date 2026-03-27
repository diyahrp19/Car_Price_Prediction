from flask import Flask, request, jsonify
import pickle
import os

app = Flask(__name__)

# Load trained model
model = pickle.load(open('car_model.pkl', 'rb'))

@app.route('/')
def home():
    return "Car Price Prediction API Running"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json

    features = [
        data['year'],        # Year of manufacture
        data['mileage'],     # Mileage in km
        data['engine_size'], # Engine size in liters
        data['horsepower'],  # Horsepower
        data['doors']        # Number of doors
    ]

    prediction = model.predict([features])[0]

    return jsonify({
        'predicted_price': round(float(prediction), 2)  # Price in USD
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)