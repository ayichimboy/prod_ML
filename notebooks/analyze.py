from loader import *
from pathlib import Path

current_folder = Path(__file__).parent
current_dir = Path.cwd()
file = current_folder/"penguins.csv"


df = pd.read_csv(file)
print(df.head())
print(df.info())