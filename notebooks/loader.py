import pandas as pd       
import numpy as np            
import matplotlib.pyplot as plt           
import seaborn as sns    
import openpyxl    
import numpy as np  


# load my file 
def file_loader(df):
    if df.endswith(".csv"):
        return pd.read_csv(df)
    elif df.endswith(".xlsx"):
        return pd.read_excel(df)
        
def clean_data(df):
    dx = df.copy()
    
    return dx