import streamlit as st
from models.calorie_predictor import predict_calories
from models.exercise_recommender import recommend_exercises
from models.meal_recommender import recommend_meals

# --- Page Config ---
st.set_page_config(page_title="FitPlan", layout="centered")
st.title("🔥 FitPlan: Calorie, Workout & Meal Planner")

# --- Sidebar Form ---
st.sidebar.header("User Profile")

name = st.sidebar.text_input("Name", "User")
age = st.sidebar.slider("Age", 18, 65, 25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
height = st.sidebar.number_input("Height (cm)", min_value=130, max_value=220, value=170)
current_weight = st.sidebar.number_input("Current Weight (kg)", min_value=30.0, max_value=200.0, value=75.0)
target_weight = st.sidebar.number_input("Target Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
activity_level = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Active", "Very Active"])
fitness_goal = st.sidebar.selectbox("Fitness Goal", ["Lose Weight", "Gain Muscle", "Maintain Weight"])

# --- Button to Generate Plan ---
if st.sidebar.button("🚀 Generate Plan"):

    # --- Calorie Calculation ---
    ideal_cal = predict_calories(age, gender, target_weight, height, activity_level, fitness_goal)

    st.markdown(f"### 👋 Hello, {name}")
    st.markdown(f"🎯 **Goal:** {fitness_goal} → **{int(target_weight)} kg**")
    st.success(f"🔥 Ideal daily calorie intake: **{int(ideal_cal)} kcal**")

    # --- Workout Recommendations ---
    st.markdown("## 🏋️ Recommended Workouts")
    gym_df, sport_df = recommend_exercises(ideal_cal, target_weight)

    with st.expander("💪 Gym Workouts"):
        if gym_df.empty:
            st.warning("No gym workouts found.")
        else:
            for _, row in gym_df.iterrows():
                exercise = row.get("Exercise", "Unknown")
                burn = int(row.get("Estimated Burn", 0))
                st.write(f"✅ {exercise} — burns **{burn} kcal/hr**")

    with st.expander("⚽ Sports Workouts"):
        if sport_df.empty:
            st.warning("No sports workouts found.")
        else:
            for _, row in sport_df.iterrows():
                exercise = row.get("Exercise", "Unknown")
                burn = int(row.get("Estimated Burn", 0))
                st.write(f"✅ {exercise} — burns **{burn} kcal/hr**")

    # --- Meal Plan ---
    st.markdown("## 🥗 Weekly Meal Plan")
    weekly_meals = recommend_meals(ideal_cal)

    for day, info in weekly_meals.items():
        with st.expander(f"📅 {day} — {info['total']} kcal"):
            for meal in info["meals"]:
                st.write(f"🍽️ **{meal['dish']}** — {meal['calories']} kcal at _{meal['location']}_")
