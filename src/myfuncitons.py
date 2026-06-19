# Import Libraries

import pandas as pd             
import numpy as np                     
import joblib
from pathlib import Path
import streamlit as st

@st.cache_data
def load_file(df):
    if df.name.endswith('.csv'):
        df = pd.read_csv(df)
    elif df.name.endswith('.xlsx'):
        df = pd.read_excel(df)
    return df