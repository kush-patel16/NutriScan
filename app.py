import streamlit as st
import json

# Load nutrition data from the JSON file
def load_nutrition_data():
    with open('nutrition_data.json', 'r') as file:
        data = json.load(file)
    return data

# Local Nutrition Data (imported from JSON file)
nutrition_data = load_nutrition_data()

# Streamlit UI
st.set_page_config(page_title="NutriScan", page_icon="🍽️", layout="wide")
st.title("🍽️ NutriScan - AI Food Analyzer & Nutrition Estimator")

# Add a description with formatting
st.markdown(""" 
    Welcome to NutriScan! 🍏🍎 Here you can estimate the nutritional values of various food items based on their weight. 
    Simply select a food item from the dropdown and enter its weight in grams to get nutritional details.

    ### Nutritional info will be calculated based on 1g values and multiplied by the entered weight.
""", unsafe_allow_html=True)

# Food Item Selection with a cleaner UI
food_item = st.selectbox("🍱 **Select a food item**", list(nutrition_data.keys()), index=0, help="Choose a food item from the list")

# Weight Input with a sleek and informative label
weight = st.number_input("⚖️ **Enter weight (grams)**", min_value=1, step=1, format="%d", help="Enter the weight of the selected food item in grams.")

# Button to trigger calculation
calculate_button = st.button("🔍 Calculate Nutrition", use_container_width=True)

# Nutrition Calculation
def get_nutrition(food, grams):
    food = food.lower()
    if food in nutrition_data:
        base = nutrition_data[food]
        factor = grams
        return {
            "Calories (kcal)": round(base["calories"] * factor, 2),
            "Protein (g)": round(base["protein"] * factor, 2),
            "Fat (g)": round(base["fat"] * factor, 2),
            "Carbohydrates (g)": round(base["carbs"] * factor, 2)
        }
    return None

# Display Results when button is clicked
if calculate_button:
    if food_item and weight:
        nutrition = get_nutrition(food_item, weight)

        if nutrition:
            st.subheader(f"🔍 **Selected Food: {food_item.title()}**")

            # Displaying Nutritional Info in a table format
            st.success("🍎 Nutritional Info Based on Your Input:")
            st.table(nutrition)

            # Add some informative text under the result
            st.markdown(""" 
                #### Nutrition Breakdown:
                - **Calories**: Provides energy.
                - **Protein**: Builds and repairs tissues.
                - **Fat**: Essential for cell function and energy.
                - **Carbohydrates**: Primary energy source for the body.
            """)
        else:
            st.warning("❌ Sorry, no nutrition data found for this food item. Please try another one.")
    else:
        st.error("⚠️ Please select a food item and enter a valid weight to calculate nutrition.")

# Footer with more info
st.markdown("""
    ---
    Made with ❤️ by NutriScan Team. For more info, please visit our GitHub(https://).
""")
