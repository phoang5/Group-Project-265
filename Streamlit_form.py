import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="FitPulse Student Form", layout="centered")
st.title("🏋‍♂ FitPulse - Student Profile Form")

# Form to collect student input
with st.form("student_form"):
    name = st.text_input("Name")
    age = st.slider("Age", 18, 35)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    height = st.number_input("Height (cm)", min_value=100, max_value=250)
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200)
    
    goal = st.selectbox("Fitness Goal", ["Lose Weight", "Gain Muscle", "Maintain Fitness"])
    activity_level = st.selectbox("Activity Level", ["Sedentary", "Lightly Active", "Active", "Very Active"])
    diet_pref = st.multiselect("Dietary Preferences", ["Vegetarian", "Vegan", "Keto", "Gluten-Free", "No Restrictions"])
    time_per_day = st.slider("Workout Time per Day (mins)", 10, 120)

    submitted = st.form_submit_button("Submit")

    if submitted:
        student_data = {
            "Timestamp": datetime.datetime.now(),
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Height": height,
            "Weight": weight,
            "Goal": goal,
            "Activity Level": activity_level,
            "Dietary Preferences": ", ".join(diet_pref),
            "Workout Time (mins/day)": time_per_day
        }

        st.success("✅ Data submitted successfully!")
        st.write(pd.DataFrame([student_data]))

        # Save to CSV
        df = pd.DataFrame([student_data])
        df.to_csv("student_inputs.csv", mode='a', header=not pd.io.common.file_exists("student_inputs.csv"), index=False)
