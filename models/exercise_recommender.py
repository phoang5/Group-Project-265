import pandas as pd
from sklearn.ensemble import RandomForestRegressor

def recommend_exercises(calorie_target, weight_kg):
    try:
        # Load and clean data
        df = pd.read_csv("data/EXCERCISE.csv")
        df.columns = df.columns.str.strip()
        df.rename(columns={"Activity, Exercise or Sport (1 hour)": "Exercise", "Type ": "Type"}, inplace=True)

        # Feature Engineering
        df["Calories per kg"] = pd.to_numeric(df["Calories per kg"], errors="coerce")
        df = df.dropna(subset=["Calories per kg"])  # remove rows with missing

        # Train Random Forest model
        X_train = pd.DataFrame({
            "Calories per kg": df["Calories per kg"],
            "Weight": [weight_kg] * len(df)
        })
        y_train = df["Calories per kg"] * weight_kg

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Predict
        X_predict = pd.DataFrame({
            "Calories per kg": df["Calories per kg"],
            "Weight": [weight_kg] * len(df)
        })
        df["Estimated Burn"] = model.predict(X_predict)
        df["Calorie Gap"] = abs(df["Estimated Burn"] - calorie_target)

        sorted_df = df.sort_values("Calorie Gap")

        # Filter by type
        gym_mask = df["Type"].str.upper().str.strip() == "GYM"
        sport_mask = df["Type"].str.upper().str.contains("SPORT", na=False)

        gym_df = sorted_df[gym_mask].copy()
        sport_df = sorted_df[sport_mask].copy()

        return gym_df.head(7)[["Exercise", "Estimated Burn"]], sport_df.head(7)[["Exercise", "Estimated Burn"]]

    except Exception as e:
        print("🚨 Error in recommend_exercises:", str(e))
        return pd.DataFrame(), pd.DataFrame()
