# Import Libraries
import streamlit as st                  
import pandas as pd             
import numpy as np                 
from pathlib import Path
import joblib
from myfuncitons import *


current_folder = Path(__file__).parent 
model_location = current_folder/"classify.joblib"
model = joblib.load(model_location)

# Make predictions
selected_columns = ['latitude', 'longitude', 'height_above_takeoff(feet)',
       'height_above_ground_at_drone_location(feet)',
       'ground_elevation_at_drone_location(feet)',
       'altitude_above_seaLevel(feet)', 'height_sonar(feet)', 'speed(mph)',
       'distance(feet)', 'mileage(feet)', 'satellites', 'gpslevel',
       'voltage(v)', 'max_altitude(feet)', 'max_ascent(feet)',
       'max_speed(mph)', 'max_distance(feet)', ' xSpeed(mph)', ' ySpeed(mph)',
       ' zSpeed(mph)', ' compass_heading(degrees)', ' pitch(degrees)',
       ' roll(degrees)', 'isPhoto', 'isVideo', 'rc_elevator', 'rc_aileron',
       'rc_throttle', 'rc_rudder', 'rc_elevator(percent)',
       'rc_aileron(percent)', 'rc_throttle(percent)', 'rc_rudder(percent)',
       'gimbal_heading(degrees)', 'gimbal_pitch(degrees)',
       'gimbal_roll(degrees)', 'battery_percent', 'current(A)',
       'battery_temperature(f)', 'altitude(feet)', 'ascent(feet)',
       'flycStateRaw']

st.set_page_config(page_title=None, 
                   page_icon=None, 
                   layout=None, 
                   initial_sidebar_state=None, 
                   menu_items=None)


st.title("Drone State Classifier 📈📊")
st.write("Simple streamlit app to upload and deploy datat for model ")
# st.header("Drone Behavior Detector")


uploaded_file = st.file_uploader("Upload an file", type=["csv", "xlsx"])

if uploaded_file:

    df = load_file(uploaded_file)
    st.dataframe(df.head())
    
    if "latitude" in df.columns and "longitude" in df.columns:

        map_df = df[["latitude", "longitude"]].copy()

        map_df["latitude"] = pd.to_numeric(map_df["latitude"], errors="coerce")
        map_df["longitude"] = pd.to_numeric(map_df["longitude"], errors="coerce")

        map_df = map_df.dropna()

        st.subheader("Drone Flight Map")
        st.map(map_df)

    else:
        st.warning("Latitude and longitude columns are missing.")

    # df.columns = df.columns.str.strip()

    missing_cols = [
        col for col in selected_columns
        if col not in df.columns
    ]

    if missing_cols:
        st.error(f"Missing columns: {missing_cols}")

    else:

        st.success("All model features found")

        cleaned_data = df[selected_columns]

        if st.button("Run Model"):

            with st.spinner("Running predictions..."):

                y_predict = model.predict(cleaned_data)

                pred_df = df.copy()
                pred_df["Predicted_State"] = y_predict

                st.dataframe(
                    pred_df[
                        ["Predicted_State"]
                    ].head()
                )

                csv = pred_df.to_csv(index=False)

                st.download_button(
                    label="Download Predictions",
                    data=csv,
                    file_name="drone_predictions.csv",
                    mime="text/csv"
                )