import streamlit as st
from models.calorie_predictor import predict_calories
from models.exercise_recommender import recommend_exercises

# Page setup
st.set_page_config(page_title="FitPlan: Calorie & Workout Planner", layout="centered")
st.title("🔥 FitPlan: Calorie & Workout Planner")

# --- User Input ---
st.sidebar.header("Enter Your Details")
name = st.sidebar.text_input("Name", "User")
age = st.sidebar.slider("Age", 18, 65, 25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
current_weight = st.sidebar.number_input("Current Weight (kg)", min_value=30.0, max_value=200.0, value=75.0)
target_weight = st.sidebar.number_input("Target Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
height = st.sidebar.number_input("Height (cm)", min_value=130, max_value=220, value=170)
activity_level = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Active", "Very Active"])
fitness_goal = st.sidebar.selectbox("Fitness Goal", ["Lose Weight", "Gain Muscle", "Maintain Weight"])

# --- Generate Button ---
if st.button("🚀 Generate Plan"):
    ideal_cal = predict_calories(age, gender, target_weight, height, activity_level, fitness_goal)

    st.markdown(f"### 👋 Hello, {name}")
    st.markdown(f"🍽️ **Fitness Goal:** {fitness_goal}")
    st.markdown(f"🎯 **Target Weight:** {int(target_weight)} kg")
    st.success(f"🔥 Your ideal daily calorie intake to reach **{int(target_weight)}kg** is: **{int(ideal_cal)} kcal**")

    # --- Recommended Workouts ---
    st.markdown("## 🏋️ Recommended Workouts")
    gym_df, sport_df = recommend_exercises(ideal_cal, target_weight)

    with st.expander("💪 Gym-Based Workouts"):
        if gym_df.empty:
            st.warning("No gym workouts found in that calorie range.")
        else:
            for _, row in gym_df.iterrows():
                st.write(f"✅ {row['Exercise']} — burns approx **{int(row['Estimated Burn'])} kcal/hr**")

    with st.expander("⚽ Sports-Based Workouts"):
        if sport_df.empty:
            st.warning("No sports workouts found in that calorie range.")
        else:
            for _, row in sport_df.iterrows():
                st.write(f"✅ {row['Exercise']} — burns approx **{int(row['Estimated Burn'])} kcal/hr**")
