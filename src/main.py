# Import necessary libraries and modules
from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
import pandas as pd


# file path for saved pipeline and label encoder
file_path_pipeline= os.path.abspath("dev/dtree_pipeline.joblib")
file_path_label = os.path.abspath("dev/labelencoderbal.joblib")

pipeline = joblib.load(file_path_pipeline)
encoder = joblib.load(file_path_label)

# Create a FastAPI instance
app = FastAPI()

# Define a Pydantic model for input data
class InputData(BaseModel):
    age: int
    gender: str
    education: str
    work_class: str
    marital_status: str
    race: str
    is_hispanic: str
    employment_commitment: str
    wage_per_hour: float
    working_week_per_year: int
    industry_code_main: str
    occupation_code_main: str
    tax_status: str
    citizenship: str

 

    # Define a Pydantic model for the prediction result
class PredictionResult(BaseModel):
    pprediction: str  

# Define a route for the root endpoint
@app.get("/")
def Income_limit_home():
    # Return a simple message for the root endpoint
    return "Income limit prediction"

# Define a route for the prediction endpoint with HTTP POST method
@app.post("/predict", response_model=PredictionResult)

def predict(data: InputData):
    # Convert all string values to lowercase
    data_dict_lower = {key: value.lower() if isinstance(value, str) else value for key, value in data.dict().items()}
    
    # Create a DataFrame using the lowercase values
    df = pd.DataFrame([data_dict_lower])

    # Make predictions using the pre-trained model
    predicted_income_level = pipeline.predict(df)

    # Decode the predicted data using the label encoder
    decoded_outcome = encoder.inverse_transform(predicted_income_level)

    # Get the prediction
    prediction = decoded_outcome[0]

    # Return the prediction result in the specified format
    return PredictionResult(pprediction=prediction)

