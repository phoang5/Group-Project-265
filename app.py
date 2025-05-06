import streamlit as st
import os
import pandas as pd
from datetime import date
from models.calorie_predictor import predict_calories
from models.exercise_recommender import recommend_exercises
from models.meal_recommender import recommend_meals
from models.progress_predictor import estimate_goal_date

# --- Page Config ---
st.set_page_config(page_title="FitPulse", layout="centered")
st.title("🔥 FitPulse: Calorie, Workout & Meal Planner")

# --- Sidebar ---
st.sidebar.header("User Profile")

name = st.sidebar.text_input("Name", "User")
age = st.sidebar.slider("Age", 18, 65, 25)
gender = st.sidebar.selectbox("Gender", ["Male", "Female"])
height = st.sidebar.number_input("Height (cm)", min_value=130, max_value=220, value=170)
current_weight = st.sidebar.number_input("Current Weight (kg)", min_value=30.0, max_value=200.0, value=75.0)
target_weight = st.sidebar.number_input("Target Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
activity_level = st.sidebar.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Active", "Very Active"])
fitness_goal = st.sidebar.selectbox("Fitness Goal", ["Lose Weight", "Gain Muscle", "Maintain Weight"])

generate = st.sidebar.button("🚀 Generate Plan")

# --- Calculate values upfront ---
ideal_cal = predict_calories(age, gender, target_weight, height, activity_level, fitness_goal)
maintenance_cal = predict_calories(age, gender, current_weight, height, activity_level, "Maintain Weight")
goal_date = estimate_goal_date(current_weight, target_weight, maintenance_cal, ideal_cal)
gym_df, sport_df = recommend_exercises(ideal_cal, target_weight)
weekly_meals = recommend_meals(ideal_cal)

# --- Tabs ---
tab1, tab2, tab3, tab4 = st.tabs(["🏠 Overview", "🏋️ Workouts", "🥗 Meals", "📅 Progress Tracker"])

# --- Overview Tab ---
with tab1:
    st.subheader("🎯 Your Personalized FitPulse Plan")
    st.markdown(f"""
    <div style="display: flex; flex-wrap: wrap; gap: 20px;">
        <div style="flex: 1; min-width: 250px; padding: 20px; border-radius: 10px; background-color: #1f2b38;">
            <h4>👤 Name</h4><p>{name}</p>
            <h4>🏁 Goal</h4><p>{fitness_goal}</p>
            <h4>📏 Weight</h4><p>{int(current_weight)} kg → <b>{int(target_weight)} kg</b></p>
        </div>
        <div style="flex: 1; min-width: 250px; padding: 20px; border-radius: 10px; background-color: #22303c;">
            <h4>🔥 Ideal Intake</h4><p><b>{int(ideal_cal)} kcal/day</b></p>
            <h4>📅 Estimated Goal Date</h4><p><b>{goal_date}</b></p>
        </div>
    </div>
    """, unsafe_allow_html=True)

# --- Workouts Tab ---
with tab2:
    st.subheader("🏋️ Recommended Workouts")
    with st.expander("💪 Gym-Based Workouts"):
        if gym_df.empty:
            st.warning("No gym workouts found.")
        else:
            for _, row in gym_df.iterrows():
                st.write(f"✅ {row['Exercise']} — burns approx **{int(row['Estimated Burn'])} kcal/hr**")

    with st.expander("⚽ Sports-Based Workouts"):
        if sport_df.empty:
            st.warning("No sports workouts found.")
        else:
            for _, row in sport_df.iterrows():
                st.write(f"✅ {row['Exercise']} — burns approx **{int(row['Estimated Burn'])} kcal/hr**")

# --- Meals Tab ---
with tab3:
    st.subheader("🥗 Weekly Meal Plan")
    for day, info in weekly_meals.items():
        with st.expander(f"📅 {day} — {info['total']} kcal"):
            for meal in info["meals"]:
                st.write(f"🍽️ **{meal['dish']}** — {meal['calories']} kcal at _{meal['location']}_")

# --- Progress Tab ---
with tab4:
    st.subheader("📊 Daily Progress Tracker")
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
            df_log = df_log[df_log["date"] != log_entry["date"]]
            df_log = pd.concat([df_log, pd.DataFrame([log_entry])], ignore_index=True)
        else:
            df_log = pd.DataFrame([log_entry])

        df_log.to_csv(log_file, index=False)
        st.success("✅ Progress logged successfully!")

    if os.path.exists("data/progress_log.csv"):
        df_log = pd.read_csv("data/progress_log.csv")
        df_log["date"] = pd.to_datetime(df_log["date"])
        df_log = df_log.sort_values("date")

        st.markdown("### 📉 Weight Trend")
        st.line_chart(df_log.set_index("date")["weight"])

        st.markdown("### 🔥 Calories Eaten vs Burned")
        st.bar_chart(df_log.set_index("date")[["calories_eaten", "calories_burned"]])

        st.markdown("### 📋 Progress Log")
        st.dataframe(df_log.sort_values("date", ascending=False).reset_index(drop=True))
