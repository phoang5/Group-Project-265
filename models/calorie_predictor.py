def estimate_calories(age, gender, weight_kg, height_cm, activity_level, goal):
    # --- BMR calculation using Mifflin-St Jeor formula ---
    if gender == "Male":
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        bmr = 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

    # --- Activity multiplier ---
    activity_factors = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Active": 1.55,
        "Very Active": 1.725
    }
    calories = bmr * activity_factors.get(activity_level, 1.2)

    # --- Goal adjustment ---
    if goal == "Lose Weight":
        calories -= 700  # safe deficit
    elif goal == "Gain Muscle":
        calories += 300  # controlled surplus

    return max(1200, int(calories))

