from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np

with open("models/my_model.pkl", 'rb') as f:
    model = pickle.load(f)\

app = FastAPI()

class ImportValidation(BaseModel):
    food_name: float
    category_name: float
    carbs: float
    fats: float
    magnesium: float
    monounsaturated_fat: float
    net_carbs: float
    omega_3_DHA: float
    omega_3_DPA: float
    omega_3_EPA: float
    phosphorus: float
    polyunsaturated_fat: float
    protein: float
    saturated_fat: float
    vitamin_B3: float
    zinc: float
    sugar: float
    vitamin_E: float

@app.post('/predict')
async def predict(request: ImportValidation):
    input_for_model = np.array([[
        request.food_name,
        request.category_name,
        request.carbs,
        request.fats,
        request.magnesium,
        request.monounsaturated_fat,
        request.net_carbs,
        request.omega_3_DHA,
        request.omega_3_DPA,
        request.omega_3_EPA,
        request.phosphorus,
        request.polyunsaturated_fat,
        request.protein,
        request.saturated_fat,
        request.vitamin_B3,
        request.zinc,
        request.sugar,
        request.vitamin_E
    ]])
    predicted_calories = model.predict(input_for_model)
    return {"Predicted calories for such configuration: ": predicted_calories[0]}

@app.get("/")
def read_root():
    return {"message": "Welcome to the API for investigating calories level in the food!"}