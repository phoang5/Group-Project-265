def predict_calories(age, gender, weight, height, activity_level, goal):
    activity_multipliers = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Active": 1.55,
        "Very Active": 1.725
    }

    # Calculate BMR using Mifflin-St Jeor Equation
    if gender == "Male":
        bmr = 10 * weight + 6.25 * height - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height - 5 * age - 161

    tdee = bmr * activity_multipliers.get(activity_level, 1.2)

    # Adjust based on fitness goal
    if goal == "Lose Weight":
        return int(tdee - 500)  # Moderate deficit
    elif goal == "Gain Muscle":
        return int(tdee + 300)  # Slight surplus
    else:
        return int(tdee)        # Maintain weight
