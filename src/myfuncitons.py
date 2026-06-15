# Import Libraries

import pandas as pd             
import numpy as np                     
import joblib
from pathlib import Path

def load_file(df):
    if df.endswith('.csv'):
        df = pd.read_csv(df)
    elif df.endswith('.xlsx'):
        df = pd.read_excel(df)
    return df