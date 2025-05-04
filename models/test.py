import pandas as pd

df = pd.read_csv("data/Meals.csv")
print("🧾 Columns:", df.columns.tolist())
print("📌 Sample Rows:\n", df.head(5))
