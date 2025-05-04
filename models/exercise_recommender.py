import pandas as pd

def recommend_exercises(calorie_target, weight_kg):
    try:
        df = pd.read_csv("data/EXCERCISE.csv")
        print("🧾 Columns after loading:", df.columns.tolist())

        df.columns = df.columns.str.strip()
        df.rename(columns={"Activity, Exercise or Sport (1 hour)": "Exercise", "Type": "Type"}, inplace=True)

        df["Estimated Burn"] = df["Calories per kg"] * weight_kg
        df["Calorie Gap"] = abs(df["Estimated Burn"] - calorie_target)

        sorted_df = df.sort_values("Calorie Gap")

        gym_mask = df["Type"].str.upper().str.strip() == "GYM"
        sport_mask = df["Type"].str.upper().str.contains("SPORT", na=False)  # Substring match

        gym_df = sorted_df[gym_mask].copy()
        sport_df = sorted_df[sport_mask].copy()

        print("✅ Final GYM columns:", gym_df.columns.tolist())
        print("✅ Final SPORT columns:", sport_df.columns.tolist())

        print("🔍 GYM DataFrame preview:")
        print(gym_df.head())

        print("🔍 SPORT DataFrame preview:")
        print(sport_df.head())

        # Limit to top 7 results
        return gym_df.head(7)[["Exercise", "Estimated Burn"]], sport_df.head(7)[["Exercise", "Estimated Burn"]]

    except Exception as e:
        print("🚨 Error in recommend_exercises:", str(e))
        return pd.DataFrame(), pd.DataFrame()
