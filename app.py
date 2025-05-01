import streamlit as st
from models.calorie_predictor import estimate_calories

st.set_page_config(page_title="Fitness App Beta", layout="centered")
st.title("🔥 FitPlan: Calorie & Workout Planner")

# --- Sidebar Form ---
st.sidebar.header("User Profile")

name = st.sidebar.text_input("Name")
age = st.sidebar.slider("Age", 18, 35)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
height = st.sidebar.slider("Height (cm)", 100, 250)
weight = st.sidebar.slider("Current Weight (kg)", 30, 200)
target_weight = st.sidebar.slider("Target Weight (kg)", 30, 200)
goal = st.sidebar.selectbox("Fitness Goal", ["Lose Weight", "Gain Muscle", "Maintain Fitness"])
activity_level = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Active", "Very Active"])

# --- Prediction Trigger ---
if st.sidebar.button("Generate Plan"):
    st.subheader(f"Hello, {name or 'User'} 👋")
    st.markdown(f"🍒 **Fitness Goal:** {goal}")
    st.markdown(f"⚖️ **Target Weight:** {target_weight} kg")

    # Use target weight unless goal is maintenance
    adjusted_weight = target_weight if goal != "Maintain Fitness" else weight

    ideal_cal = estimate_calories(age, gender, adjusted_weight, height, activity_level, goal)

    st.success(f"🔥 Your ideal daily calorie intake to reach **{target_weight}kg** is: **{ideal_cal} kcal**")
