import streamlit as st

#front page setting
st.set_page_config(
    page_title = "Sustainable Student Assistant",
    page_icon = "🌱",
    layout = "wide"
)

#heading
st.title("Sustsainable Student Assitsant")
st.write(
    "Make sustainable choices, save money, "
    "and understand your environmental impact."
)

st.divider()

#dashboard summary
st.header("Your Dasboard")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Sustainability Score", "72/100")
with col2:
    st.metric("Food Score", "70/100")
with col3:
    st.metric("Transport Score", "75/100")
st.info(
    "Welcome! Your sustainable journey starts here. "
    "Start logging your everyday activities to track your progress."
)

st.divider()

#main sections
st.header("Explore your Sustainability")

food_tab, transport_tab, waste_tab = st.tabs(
    ["Food", "Transport", "Waste Reduction"]
)

with food_tab:
    st.subheader("Food Tracker")
    st.write(
        "Log your meals and explore their estimated "
        "environmental impact."
        )
    #data for development only
    meals = {
        "Beef burger": 3.0,
        "Chicken wrap": 1.0,
        "Vegetable pasta":0.5,
        "Vegan curry": 0.4,
        "Cheese pizza": 1.2
    }

    if "logged_meals" not in st.session_state:
        st.session_state.logged_meals = []

        #user can select a meal
    selected_meal = st.selectbox(
        "What did you eat?",
        list(meals.keys())
    )

    if st.button("Add Meal"):
        meal_data = {
            "name": selected_meal,
            "emissions": meals[selected_meal]
        }

        st.session_state.logged_meals.append(meal_data)
        st.success(f"{selected_meal} added to your food log!")

    st.divider()

    st.subheader("Today's Food Log")

    if st.session_state.logged_meals:
        total_emissions = sum(
            meal["emissions"]
            for meal in st.session_state.logged_meals
        )

        for meal in st.session_state.logged_meals:
            st.write(
                f"{meal['name']} - "
                f"{meal['emissions']:.2f} kg CO2e"
            )

    else:
        st.info("You haven't logged any meals yet.")


with transport_tab:
    st.subheader("Transport Tracker")
    st.write("Explore how your travel choices affect the environment.")

    transport = st.selectbox(
        "How do you usually travel?",
        ["Walking", "Cycling", "Bus", "Train", "Car"]
    )

    st.write(f"Selected Transport: **{transport}**")
    st.caption("Calculating carbon emissions...")

with waste_tab:
    st.subheader("Waste Reduction")
    st.write("Explore ways to reduce waste and recycle more.")

    action = st.selectbox(
        "Choose a sustainable action you have done:",
        [
            "Recycled an item",
            "Used a reusable bottle",
            "Avoided a disposable cup",
            "Reduced food waste"
        ]
    )

    st.write (f"Selected action: **{action}**")
    st.caption("Activity tracking and scoring coming next!")

st.divider()

st.caption(
    "Sustainable Student Assistant | A student personal project"
)