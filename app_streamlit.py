import streamlit as st
import requests

st.set_page_config(page_title="Flight Price Prediction", page_icon="✈️")

st.title("Flight Price Prediction")

departure_date = st.date_input("Departure Date")
arrival_date = st.date_input("Arrival Date")
source = st.selectbox("Source", ["Delhi", "Kolkata", "Mumbai", "Chennai"])
destination = st.selectbox("Destination", ["Cochin", "Delhi", "New Delhi", "Hyderabad", "Kolkata"])
stops = st.selectbox("Number of Stops", [0, 1, 2, 3, 4])
airline = st.selectbox("Airline", ["Air India", "GoAir", "IndiGo", "Jet Airways", "SpiceJet", "Trujet", "Vistara", "Vistara Premium economy"])

if st.button("Predict"):
    data = {
        "Dep_Time": departure_date.strftime("%Y-%m-%dT%H:%M"),
        "Arrival_Time": arrival_date.strftime("%Y-%m-%dT%H:%M"),
        "Source": source,
        "Destination": destination,
        "stops": stops,
        "airline": airline
    }

    response = requests.post("http://127.0.0.1:5000/predict", json=data)

    if response.status_code == 200:
        prediction_text = response.json()["prediction"]
        st.success(f"Predicted Flight Price: {prediction_text}")
    else:
        st.error("An error occurred while fetching the prediction.")


st.markdown("©2023 Chiamaka")
