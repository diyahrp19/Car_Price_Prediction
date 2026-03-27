import streamlit as st
import requests

st.title("Car Price Predictor")

# Inputs
year = st.slider("Year of Manufacture", 1990, 2023, 2015, step=1)
mileage = st.slider("Mileage (km)", 0, 300000, 80000, step=1000)
engine_size = st.slider("Engine Size (liters)", 1.0, 5.0, 2.0, step=0.1)
horsepower = st.slider("Horsepower", 50, 400, 150, step=5)
doors = st.selectbox("Number of Doors", [2, 3, 4, 5], index=2)

# Predict button
if st.button("Predict Price"):
    url = "https://car-price-prediction-1upd.onrender.com/predict"  # Replace with your API URL

    data = {
        "year": year,
        "mileage": mileage,
        "engine_size": engine_size,
        "horsepower": horsepower,
        "doors": doors
    }

    try:
        response = requests.post(url, json=data)
        response.raise_for_status()
        result = response.json()

        st.success(f"Predicted Car Price: ${result.get('predicted_price')}")
    except requests.exceptions.RequestException as e:
        st.error(f"Error contacting the server: {e}")
    except ValueError:
        st.error("Invalid response from server")
