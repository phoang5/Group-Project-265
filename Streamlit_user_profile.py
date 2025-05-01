import streamlit as st

st.header("Welcome to FitPulse!")
name = st.text_input("Your name (optional)")
age = st.number_input("Age", min_value=10, max_value=100, value=25)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
height = st.number_input("Height (cm)", min_value=100.0, max_value=250.0)
weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0)
goal = st.selectbox("Your primary fitness goal", ["Lose weight", "Gain muscle", "Maintain fitness"])
activity = st.selectbox("Activity level", ["Sedentary", "Light", "Moderate", "Active", "Very active"])
diet = st.selectbox("Dietary preference", ["Balanced", "Vegan", "Vegetarian", "High-protein", "Low-carb"])
allergies = st.multiselect("Food allergies (optional)", ["Nuts", "Gluten", "Dairy", "Eggs", "Soy"])
meal_types = st.multiselect("Preferred meal types", ["Breakfast", "Lunch", "Dinner", "Snacks"])
workouts = st.multiselect("Workout preference", ["Cardio", "Strength", "Yoga", "HIIT"])
freq = st.slider("Workout frequency per week", 0, 7, 3)
history = st.number_input("Months you've been actively exercising", 0, 60, 6)
target_weight = st.number_input("Target weight (kg)", min_value=30.0, max_value=200.0)
email = st.text_input("Email (optional, for reminders)")

# Example data dict
user_profile = {
    "name": name,
    "age": age,
    "gender": gender.lower(),
    "height_cm": height,
    "weight_kg": weight,
    "goal": goal.lower(),
    "activity_level": activity.lower(),
    "dietary_preference": diet.lower(),
    "allergies": [a.lower() for a in allergies],
    "preferred_meal_types": [m.lower() for m in meal_types],
    "workout_frequency_per_week": freq,
    "workout_preference": [w.lower() for w in workouts],
    "fitness_history_months": history,
    "target_weight_kg": target_weight,
    "email": email
}
