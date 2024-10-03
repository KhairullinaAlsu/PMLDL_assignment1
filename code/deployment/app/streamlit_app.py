import streamlit as st
import requests
# Create input fields for all attributes in the PredictionRequest model
food_name = st.number_input("food_name", value=-1.718773)
category_name = st.number_input("category_name", value=-0.721422)
carbs = st.number_input("carbss",value=-0.637615)
fats = st.number_input("fats", value=-0.563601)
magnesium = st.number_input("magnesium", value=-0.324305)
monounsaturated_fat = st.number_input("monounsaturated_fat", value=-0.456377)
net_carbs = st.number_input("net_carbs",  value=-0.604605)
omega_3_DHA = st.number_input("omega_3_DHA",  value=-0.082812)
omega_3_DPA = st.number_input("Omega_3_DPA",  value=-0.088039)
omega_3_EPA = st.number_input("Omega_3_EPA", value=-0.079675)
phosphorus = st.number_input("phosphorus", value=-0.782426)
polyunsaturated_fat = st.number_input("polyunsaturated_fat", value=-0.314146)
protein = st.number_input("protein",value=-0.880450)
saturated_fat = st.number_input("saturated_fat", value=-0.421848)
vitamin_B3 = st.number_input("vitamin_B3",value=-0.515631)
zinc = st.number_input("zinc",value=-0.419736)
sugar = st.number_input("sugar", value=-0.495401)
vitamin_E = st.number_input("vitamin_E",value=-0.203543)



# Prediction button
if st.button("Show calories"):
    # Prepare the payload for the API request
    input_data = {
        "food_name": food_name,
        "category_name": category_name,
        "carbs": carbs,
        "fats": fats,
        "magnesium": magnesium,
        "monounsaturated_fat": monounsaturated_fat,
        "net_carbs": net_carbs,
        "omega_3_DHA": omega_3_DHA,
        "omega_3_DPA": omega_3_DPA,
        "omega_3_EPA": omega_3_EPA,
        "phosphorus": phosphorus,
        "polyunsaturated_fat": polyunsaturated_fat,
        "protein": protein,
        "saturated_fat": saturated_fat,
        "vitamin_B3": vitamin_B3,
        "zinc": zinc,
        "sugar": sugar,
        "vitamin_E": vitamin_E
    }
    response = requests.post("http://fastapi:8080/predict", json=input_data)
    if response.status_code == 422:
        st.error(f"Error 422: {response.json()}")
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted calories: {result}")
    else:
        st.error(f"Error: {response.status_code}")
