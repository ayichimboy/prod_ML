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


st.title("Drone State Classifier 📈📊")
st.header("Drone Behavior Detector")


uploaded_file = st.file_uploader("Upload an image", type=["csv", "xlsx"])

if uploaded_file:
    
    try:
        df = load_file(uploaded_file)
        st.success("Data Successfully Loaded 😀")
        st.write(df)     
    except Exception as e:
        print(f"Error: {e}")
        

# Make predictions
selected_columns = [
       'height_above_takeoff(feet)',
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
       'gimbal_roll(degrees)', 'battery_percent', 'voltageCell1',
       'voltageCell2', 'voltageCell3', 'voltageCell4', 'voltageCell5',
       'voltageCell6', 'current(A)', 'battery_temperature(f)',
       'altitude(feet)', 'ascent(feet)', 'flycStateRaw', 'flycState']
      

if selected_columns in uploaded_file.columns:
    st.write("Selected Columns Present in data")
    st.success("Selected Columns Present in data")
else:
    st.write("Selected Columns Not Present in data")
    st.error("Selected Columns Not Present in data")
    
cleaned_data = uploaded_file[selected_columns]
y_pred = model.predict(cleaned_data)

