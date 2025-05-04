import streamlit as st
import os
import pandas as pd
from datetime import date
from models.calorie_predictor import predict_calories
from models.exercise_recommender import recommend_exercises
from models.meal_recommender import recommend_meals
from models.progress_predictor import estimate_goal_date

# --- Page Config ---
st.set_page_config(page_title="FitPlan", layout="centered")
st.markdown("<h1 style='color:#ff4b4b;'>🔥 FitPlan: Calorie, Workout & Meal Planner</h1>", unsafe_allow_html=True)

# --- Sidebar Form ---
st.sidebar.header("🧍 User Profile")

name = st.sidebar.text_input("Name", "User")
age = st.sidebar.slider("Age", 18, 65, 25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
height = st.sidebar.number_input("Height (cm)", min_value=130, max_value=220, value=170)
current_weight = st.sidebar.number_input("Current Weight (kg)", min_value=30.0, max_value=200.0, value=75.0)
target_weight = st.sidebar.number_input("Target Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
activity_level = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Active", "Very Active"])
fitness_goal = st.sidebar.selectbox("Fitness Goal", ["Lose Weight", "Gain Muscle", "Maintain Weight"])

# --- Generate Plan ---
if st.sidebar.button("🚀 Generate Plan"):

    # --- Calorie Logic ---
    ideal_cal = predict_calories(age, gender, target_weight, height, activity_level, fitness_goal)
    maintenance_cal = predict_calories(age, gender, current_weight, height, activity_level, "Maintain Weight")
    goal_date = estimate_goal_date(current_weight, target_weight, maintenance_cal, ideal_cal)

    # --- Summary Card View ---
    st.markdown("---")
    st.markdown("## 🎯 <span style='color:#f0f0f0;'>Your Personalized FitPlan</span>", unsafe_allow_html=True)

    st.markdown(f"""
    <div style="display: flex; flex-wrap: wrap; gap: 20px;">
        <div style="flex: 1; padding: 20px; border-radius: 10px; background-color: #2e2e2e;">
            <h4 style="color:#ffffff;">👤 Name</h4><p style="color:#dddddd;">{name}</p>
            <h4 style="color:#ffffff;">🏁 Fitness Goal</h4><p style="color:#dddddd;">{fitness_goal}</p>
            <h4 style="color:#ffffff;">📏 Current → Target</h4><p style="color:#dddddd;">{int(current_weight)} kg → <b>{int(target_weight)} kg</b></p>
        </div>
        <div style="flex: 1; padding: 20px; border-radius: 10px; background-color: #1f3b1f;">
            <h4 style="color:#ffffff;">🔥 Ideal Calorie Intake</h4>
            <p style="color:#d4edda;"><b>{int(ideal_cal)} kcal/day</b></p>
            <h4 style="color:#ffffff;">📅 Target Date</h4>
            <p style="color:#d4edda;"><b>{goal_date}</b></p>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("---")

    # --- Workout Suggestions ---
    st.subheader("🏋️ Recommended Workouts")
    gym_df, sport_df = recommend_exercises(ideal_cal, target_weight)

    with st.expander("💪 Gym Workouts"):
        if gym_df.empty:
            st.warning("No gym workouts found.")
        else:
            for _, row in gym_df.iterrows():
                st.markdown(f"<span style='color:#90ee90;'>✅ {row['Exercise']} — burns <b>{int(row['Estimated Burn'])} kcal/hr</b></span>", unsafe_allow_html=True)

    with st.expander("⚽ Sports Workouts"):
        if sport_df.empty:
            st.warning("No sports workouts found.")
        else:
            for _, row in sport_df.iterrows():
                st.markdown(f"<span style='color:#90ee90;'>✅ {row['Exercise']} — burns <b>{int(row['Estimated Burn'])} kcal/hr</b></span>", unsafe_allow_html=True)

    st.markdown("---")

    # --- Meal Plan Section ---
    st.subheader("🥗 Weekly Meal Plan")
    weekly_meals = recommend_meals(ideal_cal)

    for day, info in weekly_meals.items():
        with st.expander(f"📅 {day} — {info['total']} kcal"):
            for meal in info["meals"]:
                st.markdown(f"<span style='color:#e0e0e0;'>🍽️ <b>{meal['dish']}</b> — {meal['calories']} kcal at <i>{meal['location']}</i></span>", unsafe_allow_html=True)

# --- Progress Logger ---
st.markdown("## 📊 Daily Progress Tracker")

log_weight = st.number_input("📏 Today's Weight (kg)", min_value=30.0, max_value=200.0)
log_cals_eaten = st.number_input("🍽️ Calories Consumed Today", min_value=0)
log_cals_burned = st.number_input("🔥 Calories Burned Today", min_value=0)

if st.button("✅ Log Today's Progress"):
    log_entry = {
        "date": str(date.today()),
        "weight": log_weight,
        "calories_eaten": log_cals_eaten,
        "calories_burned": log_cals_burned
    }

    log_file = "data/progress_log.csv"
    if os.path.exists(log_file):
        df_log = pd.read_csv(log_file)
        df_log = df_log[df_log["date"] != log_entry["date"]]  # remove duplicates
        df_log = pd.concat([df_log, pd.DataFrame([log_entry])], ignore_index=True)
    else:
        df_log = pd.DataFrame([log_entry])

    df_log.to_csv(log_file, index=False)
    st.success("✅ Progress logged successfully!")

# --- Progress Charts ---
if os.path.exists("data/progress_log.csv"):
    df_log = pd.read_csv("data/progress_log.csv")
    df_log["date"] = pd.to_datetime(df_log["date"])
    df_log = df_log.sort_values("date")

    st.markdown("### 📉 Weight Trend")
    st.line_chart(df_log.set_index("date")["weight"])

    st.markdown("### 🔥 Calories Eaten vs. Burned")
    st.bar_chart(df_log.set_index("date")[["calories_eaten", "calories_burned"]])

    st.markdown("### 📋 Progress Log Table")
    st.dataframe(df_log.sort_values("date", ascending=False).reset_index(drop=True))
