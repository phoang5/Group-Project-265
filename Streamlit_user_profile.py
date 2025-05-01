import streamlit as st

# Collect user inputs
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

# Display user profile for confirmation
st.subheader("Your Profile Summary")
st.write(user_profile)

# Provide feedback based on the goal
st.subheader("Your Fitness Feedback")
if goal == "lose weight":
    st.write("To achieve weight loss, aim for a higher activity level, and a calorie deficit in your diet. Try to incorporate cardio and strength workouts.")
elif goal == "gain muscle":
    st.write("Focus on strength training and consume a high-protein diet to build muscle. Consider a moderate to high calorie intake to support muscle growth.")
else:
    st.write("Maintain your current weight by focusing on balanced workouts and a diet that matches your activity level.")

# Suggest daily meal plan based on dietary preferences
st.subheader("Your Daily Meal Plan")
if diet == "Balanced":
    st.write("For a balanced diet, aim to consume a mix of proteins, carbohydrates, and healthy fats in every meal.")
    st.write("**Breakfast**: Oats with berries and almonds, scrambled eggs, and green tea.")
    st.write("**Lunch**: Grilled chicken breast with quinoa and vegetables.")
    st.write("**Dinner**: Baked salmon, sweet potatoes, and steamed broccoli.")
    st.write("**Snacks**: Greek yogurt with honey, apple slices with peanut butter.")
elif diet == "Vegan":
    st.write("For a vegan diet, focus on plant-based proteins and nutrients.")
    st.write("**Breakfast**: Chia seed pudding with almond milk, fruit, and nuts.")
    st.write("**Lunch**: Quinoa salad with chickpeas, avocado, cucumber, and olive oil dressing.")
    st.write("**Dinner**: Stir-fried tofu with vegetables and brown rice.")
    st.write("**Snacks**: Hummus with carrot sticks, almond butter on whole grain toast.")
elif diet == "Vegetarian":
    st.write("For a vegetarian diet, include a variety of plant-based and dairy proteins.")
    st.write("**Breakfast**: Smoothie with spinach, banana, almond milk, and protein powder.")
    st.write("**Lunch**: Grilled vegetable wrap with hummus and feta cheese.")
    st.write("**Dinner**: Lentil curry with brown rice and steamed spinach.")
    st.write("**Snacks**: Cottage cheese with mixed nuts, apple with peanut butter.")
elif diet == "High-protein":
    st.write("For a high-protein diet, focus on lean meats, eggs, and legumes.")
    st.write("**Breakfast**: Scrambled eggs with spinach and turkey bacon.")
    st.write("**Lunch**: Grilled chicken with sweet potatoes and green beans.")
    st.write("**Dinner**: Beef steak with quinoa and steamed asparagus.")
    st.write("**Snacks**: Protein shake, boiled eggs, cottage cheese.")
elif diet == "Low-carb":
    st.write("For a low-carb diet, limit your carbohydrate intake and focus on fats and proteins.")
    st.write("**Breakfast**: Avocado toast with poached eggs.")
    st.write("**Lunch**: Chicken salad with leafy greens, cheese, and olive oil dressing.")
    st.write("**Dinner**: Grilled salmon with zucchini noodles.")
    st.write("**Snacks**: Almonds, cheese sticks, hard-boiled eggs.")
