import pandas as pd
import random

def recommend_meals(calorie_target, csv_path="data/Meals.csv"):
    try:
        df = pd.read_csv(csv_path)
        df.columns = df.columns.str.strip()

        # Identify meal columns and corresponding calorie columns
        stations = [col for col in df.columns if "cal)" not in col and col not in ["Day", "Column1"]]
        cal_cols = [col for col in df.columns if "(cal)" in col]
        dish_map = {dish: dish + " (cal)" for dish in stations}

        weekly_plan = {}

        for _, row in df.iterrows():
            day = row["Day"]
            selected = []
            total_cals = 0

            random.shuffle(stations)  # shuffle for variety

            for dish_col in stations:
                cal_col = dish_map[dish_col]
                dish = row[dish_col]
                cals = row[cal_col]

                if pd.notna(dish) and pd.notna(cals) and total_cals + cals <= calorie_target * 1.1:
                    # Extract location from column name
                    location = dish_col.split(" - ")[0].strip()
                    selected.append({
                        "dish": dish,
                        "calories": int(cals),
                        "location": location
                    })
                    total_cals += cals

                if total_cals >= calorie_target * 0.9:
                    break

            weekly_plan[day] = {
                "meals": selected,
                "total": int(total_cals)
            }

        return weekly_plan

    except Exception as e:
        print("🚨 Error in recommend_meals:", e)
        return {}
