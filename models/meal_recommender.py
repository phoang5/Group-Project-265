import pandas as pd
from sklearn.neighbors import NearestNeighbors
import random

def recommend_meals(calorie_target, csv_path="data/Meals.csv"):
    try:
        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.strip()

        # Identify columns
        stations = [col for col in df.columns if "cal)" not in col and col not in ["Day", "Column1"]]
        cal_cols = [col for col in df.columns if "(cal)" in col]
        dish_map = {dish: dish + " (cal)" for dish in stations}

        # Flatten to a meal list
        meal_rows = []
        for _, row in df.iterrows():
            for dish_col in stations:
                cal_col = dish_map[dish_col]
                dish = row.get(dish_col)
                cals = row.get(cal_col)
                day = row["Day"]
                location = dish_col.split(" - ")[0].strip()

                if pd.notna(dish) and pd.notna(cals):
                    try:
                        meal_rows.append({
                            "day": day,
                            "dish": dish,
                            "calories": int(cals),
                            "location": location
                        })
                    except ValueError:
                        continue

        meal_df = pd.DataFrame(meal_rows)
        if meal_df.empty:
            raise ValueError("Meal DataFrame is empty after processing.")

        # Fit KNN on calorie values
        knn = NearestNeighbors(n_neighbors=min(10, len(meal_df)))
        knn.fit(meal_df[["calories"]])

        weekly_plan = {}
        for day in meal_df["day"].unique():
            day_meals = meal_df[meal_df["day"] == day].reset_index(drop=True)
            if day_meals.empty:
                continue

            neighbors = min(10, len(day_meals))
            knn_day = NearestNeighbors(n_neighbors=neighbors)
            knn_day.fit(day_meals[["calories"]])
            _, indices = knn_day.kneighbors([[calorie_target]])

            selected = []
            total_cals = 0

            for idx in indices[0]:
                if idx >= len(day_meals): continue
                meal = day_meals.iloc[idx]
                if total_cals + meal["calories"] <= calorie_target * 1.1:
                    selected.append({
                        "dish": meal["dish"],
                        "calories": meal["calories"],
                        "location": meal["location"]
                    })
                    total_cals += meal["calories"]

                if total_cals >= calorie_target * 0.9:
                    break

            weekly_plan[day] = {
                "meals": selected,
                "total": total_cals
            }

        return weekly_plan

    except Exception as e:
        print("🚨 Error in recommend_meals:", e)
        return {}
