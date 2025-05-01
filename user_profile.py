user_input_schema = {
    "name": "string",  # optional for personalization
    "age": "int",
    "gender": "string",  # options: 'male', 'female', 'other'
    "height_cm": "float",  # for BMI
    "weight_kg": "float",
    "goal": "string",  # options: 'lose weight', 'gain muscle', 'maintain fitness'
    "activity_level": "string",  # options: 'sedentary', 'light', 'moderate', 'active', 'very active'
    "dietary_preference": "string",  # e.g., 'vegan', 'vegetarian', 'high-protein', 'balanced', 'low-carb'
    "allergies": ["string"],  # optional list: e.g., ['nuts', 'gluten']
    "preferred_meal_types": ["string"],  # e.g., ['breakfast', 'lunch', 'dinner', 'snacks']
    "workout_frequency_per_week": "int",
    "workout_preference": ["string"],  # e.g., ['cardio', 'strength', 'yoga']
    "fitness_history_months": "int",  # for progress prediction
    "target_weight_kg": "float",  # optional
    "email": "string"  # optional, for reminders/notifications
}
