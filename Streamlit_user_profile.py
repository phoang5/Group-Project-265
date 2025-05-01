import streamlit as st

# Header
st.markdown("<h1 style='text-align: center;'>Welcome to FitPulse!</h1>", unsafe_allow_html=True)

# Collect user inputs
with st.form(key='user_form'):
    st.subheader("Please fill in your details:")
    
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
    
    submit_button = st.form_submit_button("Submit")

# Process the form data after submission
if submit_button:
    # Create user profile dictionary
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

    # Beautified Profile Summary Section
    st.markdown("<h2 style='text-align: center;'>Your Profile Summary</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 20px; font-weight: bold;'>Name: {name}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px;'>Age: {age} | Gender: {gender.capitalize()} | Height: {height} cm | Weight: {weight} kg</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px;'>Goal: {goal.capitalize()} | Activity Level: {activity.capitalize()} | Workout Frequency: {freq} days/week</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='font-size: 18px;'>Diet: {diet.capitalize()} | Allergies: {', '.join(allergies) if allergies else 'None'}</p>", unsafe_allow_html=True)
    
    # Add divider line for better separation
    st.markdown("<hr style='border-top: 2px solid #B0C4DE;'>", unsafe_allow_html=True)

    # Meal Plan based on Dietary Preferences with more variety
    st.markdown("<h2 style='text-align: center;'>Your Daily Meal Plan</h2>", unsafe_allow_html=True)
    
    # Balanced Diet Option
    if diet == "Balanced":
        # Display meals with icons for variety
        st.markdown("**Breakfast Options**: 🥣🍓")
        st.markdown("1. Oats with berries, almonds, scrambled eggs, and green tea.")
        st.markdown("2. Whole grain toast with avocado, eggs, and a smoothie. 🥑🍞")

        st.markdown("**Lunch Options**: 🍗🥗")
        st.markdown("1. Grilled chicken breast with quinoa and steamed vegetables.")
        st.markdown("2. Turkey and avocado wrap with a side of fresh salad. 🥙🥑")

        st.markdown("**Dinner Options**: 🐟🍠")
        st.markdown("1. Baked salmon with sweet potatoes and steamed broccoli.")
        st.markdown("2. Grilled chicken stir-fry with mixed vegetables and rice. 🍚🍗")

        st.markdown("**Snacks Options**: 🍏🍯")
        st.markdown("1. Greek yogurt with honey, apple slices, and peanut butter.")
        st.markdown("2. Protein bar or a handful of almonds. 🥜")

    # Vegan Diet Option
    elif diet == "Vegan":
        st.markdown("**Breakfast Options**: 🌱🍓")
        st.markdown("1. Chia seed pudding with almond milk, fruit, and nuts. 🥥🍇")
        st.markdown("2. Vegan banana pancakes with maple syrup. 🍌🥞")

        st.markdown("**Lunch Options**: 🥗🌿")
        st.markdown("1. Quinoa salad with chickpeas, avocado, cucumber, and olive oil dressing. 🥑🍅")
        st.markdown("2. Hummus and veggie wrap with a side of sweet potato fries. 🍠🌯")

        st.markdown("**Dinner Options**: 🍚🌶")
        st.markdown("1. Stir-fried tofu with mixed vegetables and brown rice. 🍚🥦")
        st.markdown("2. Vegan curry with lentils, chickpeas, and spinach served with quinoa. 🥙🍛")

        st.markdown("**Snacks Options**: 🍏🥒")
        st.markdown("1. Hummus with carrot sticks and almond butter on whole grain toast. 🥕🍞")
        st.markdown("2. Fruit salad with a sprinkle of chia seeds. 🍉🍊")

    # Additional Diet Options (Vegetarian, High-protein, Low-carb)
    elif diet == "Vegetarian":
        st.markdown("**Breakfast Options**: 🍌🥑")
        st.markdown("1. Smoothie with spinach, banana, almond milk, and protein powder. 🥤🍌")
        st.markdown("2. Avocado toast with poached eggs and a side of fresh fruit. 🍞🍊")

        st.markdown("**Lunch Options**: 🥙🧀")
        st.markdown("1. Grilled vegetable wrap with hummus and feta cheese. 🧆🥒")
        st.markdown("2. Mediterranean salad with falafel and tzatziki sauce. 🥗🍅")

        st.markdown("**Dinner Options**: 🍛🍴")
        st.markdown("1. Lentil curry with brown rice and steamed spinach. 🍛🍚")
        st.markdown("2. Roasted vegetable and quinoa stuffed peppers. 🌶🍚")

        st.markdown("**Snacks Options**: 🧀🥜")
        st.markdown("1. Cottage cheese with mixed nuts and apple slices. 🍏🥜")
        st.markdown("2. Greek yogurt with chia seeds and a drizzle of honey. 🍯🥄")

    elif diet == "High-protein":
        st.markdown("**Breakfast Options**: 🍳🥓")
        st.markdown("1. Scrambled eggs with spinach, turkey bacon, and whole-grain toast. 🍞🍳")
        st.markdown("2. Protein smoothie with spinach, banana, and almond butter. 🍌🥑")

        st.markdown("**Lunch Options**: 🥩🥗")
        st.markdown("1. Grilled chicken with sweet potatoes and green beans. 🍠🍗")
        st.markdown("2. Tuna salad with mixed greens and balsamic vinaigrette. 🥗🐟")

        st.markdown("**Dinner Options**: 🥩🥔")
        st.markdown("1. Beef steak with quinoa and steamed asparagus. 🥩🍚")
        st.markdown("2. Grilled salmon with roasted Brussels sprouts and brown rice. 🐟🍚")

        st.markdown("**Snacks Options**: 🧀🥤")
        st.markdown("1. Protein shake, boiled eggs, or cottage cheese. 🥛🍳")
        st.markdown("2. Almond butter on whole grain toast. 🥜🍞")

    elif diet == "Low-carb":
        st.markdown("**Breakfast Options**: 🥑🍳")
        st.markdown("1. Avocado toast with poached eggs and a side of tomatoes. 🍞🍅")
        st.markdown("2. Omelet with spinach, cheese, and mushrooms. 🍄🍳")

        st.markdown("**Lunch Options**: 🥗🥒")
        st.markdown("1. Chicken salad with leafy greens, cheese, and olive oil dressing. 🥗🧀")
        st.markdown("2. Grilled salmon with zucchini noodles and a side of asparagus. 🐟🍜")

        st.markdown("**Dinner Options**: 🍗🥦")
        st.markdown("1. Grilled chicken breast with roasted cauliflower. 🐔🌸")
        st.markdown("2. Pork chops with a side of sautéed spinach and garlic. 🐖🍽")

        st.markdown("**Snacks Options**: 🧀🥒")
        st.markdown("1. Almonds, cheese sticks, or hard-boiled eggs. 🥚🧀")
        st.markdown("2. Celery with peanut butter or hummus. 🥒🥜")

    # Add another divider line for final separation
    st.markdown("<hr style='border-top: 2px solid #B0C4DE;'>", unsafe_allow_html=True)

    # Optionally, display the email for confirmation
    if email:
        st.markdown(f"<p style='font-size: 18px; font-weight: bold;'>A reminder will be sent to: {email}</p>", unsafe_allow_html=True)
