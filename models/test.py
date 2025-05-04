# check_columns.py
import pandas as pd

# Load the dataset
df = pd.read_csv("data/EXCERCISE.csv")

# Print raw column names
print("Raw columns:")
print(df.columns.tolist())

# Clean them for inspection
df.columns = df.columns.str.strip().str.replace('\ufeff', '')
print("\nCleaned columns:")
print(df.columns.tolist())
