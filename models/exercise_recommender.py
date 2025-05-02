import pandas as pd

def recommend_exercises(calorie_target, weight_kg, num_exercises=5):
    try:
        # Load the exercise dataset
        df = pd.read_csv("data/exercise_dataset.csv")

        # Calculate estimated calories burned for the user's weight
        df["Estimated Burn"] = df["Calories per kg"] * weight_kg

        # Find the closest matches to the calorie target
        df["Calorie Gap"] = abs(df["Estimated Burn"] - calorie_target)
        sorted_df = df.sort_values("Calorie Gap")

        # Return the top N matches
        return sorted_df[["Exercise or Sport (1 hour)", "Estimated Burn"]].head(num_exercises)

    except Exception as e:
        return pd.DataFrame({"Error": [str(e)]})

