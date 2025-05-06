import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib
import os

def train_rf_model():
    df = pd.read_csv("data/EXCERCISE.csv")
    df.columns = df.columns.str.strip()
    df.rename(columns={"Activity, Exercise or Sport (1 hour)": "Exercise"}, inplace=True)
    df["Calories per kg"] = pd.to_numeric(df["Calories per kg"], errors="coerce")
    df = df.dropna(subset=["Calories per kg"])

    weights = [50, 60, 70, 80, 90]
    data = []

    for _, row in df.iterrows():
        for w in weights:
            data.append({
                "Exercise": row["Exercise"],
                "Weight": w,
                "Calories per kg": row["Calories per kg"],
                "Estimated Burn": w * row["Calories per kg"]
            })

    model_df = pd.DataFrame(data)
    X = model_df[["Weight", "Calories per kg"]]
    y = model_df["Estimated Burn"]

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)

    os.makedirs("models", exist_ok=True)
    joblib.dump(model, "models/rf_exercise_model.pkl")
    print("✅ Random Forest model saved.")

if __name__ == "__main__":
    train_rf_model()
