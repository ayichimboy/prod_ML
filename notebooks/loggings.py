import numpy as np                     
import pandas as pd          
import matplotlib.pyplot as plt                          
import seaborn as sns 
from pathlib import Path

# File path -- for current folder and others
current_dir = Path(__file__).parent
parent_dir = Path(__file__).parent.parent
current_folder = Path.cwd()
file_path = current_dir/"penguins.csv"

df = pd.read_csv(file_path)


try:
    unque_species = df["species"].unique()
except Exception as e:
    print(f"Error {e}")





# Print Values 
print(f"Current Directory: {current_dir}")
print(f"Parent Directory: {parent_dir}")
print(f"Another Currentl Directory: {current_folder}")