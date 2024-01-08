import gradio as gr
import sklearn
import joblib
import pandas as pd
from sklearn.tree import DecisionTreeClassifier


# copy all necessary features for encoding dna scaling in the same sequence from python codes
expected_inputs = ["age","gender","education","work_class","marital_status","race","is_hispanic","employment_commitment","wage_per_hour","working_week_per_year","industry_code_main","occupation_code_main","tax_status","citizenship"]

#numeric features
numerical =  ["age","wage_per_hour","working_week_per_year"]

#Categorical features
categoricals = ["gender","education","work_class","marital_status","race","is_hispanic","employment_commitment","industry_code_main","occupation_code_main","tax_status","citizenship"]

#load pipeline

def load_pipeline(file_path):
    pipeline = joblib.load(file_path)
    return pipeline

# load the pipeline
file_path_pipeline = "dev/dtree_pipeline.joblib"
loaded_pipeline = load_pipeline(file_path_pipeline)

# load the label encoder
file_path_encoder = "dev/labelencoderbal.joblib"
loaded_encoder = load_pipeline(file_path_encoder)

# Now you can use the loaded_pipeline for making predictions

def predict_income_limit(*args, pipeline=loaded_pipeline, encoder=loaded_encoder):
    try:
        input_data = pd.DataFrame([args], columns=expected_inputs)

        # Use the predict method for making predictions
        predicted_income_level = pipeline.predict(input_data)

        # Decode the predicted data using the label encoder
        decoded_income_level = encoder.inverse_transform(predicted_income_level)

        return decoded_income_level[0]

    except Exception as e:
        return f"Error: {str(e)}"
    
EmpAge = gr.Number(label="Age")
EmpGender = gr.Radio(label="Gender", choices=["male", "female"])
EmpEdu = gr.Dropdown(label="Education", choices=["Bachelors Degree", "High School Graduate", "Some College (No Degree)", "Masters Degree", "Associates Degree (Academic Program)", "Professional School Degree", "11th Grade", "9th Grade", "Children", "7th and 8th Grade", "10th Grade", "12th Grade No Diploma", "5th or 6th Grade", "Less than 1st Grade"])
EmpClass = gr.Dropdown(label="Work Class", choices=["Self-employed-not incorporated", "Private", "Federal government", "Local government", "Self-employed-incorporated", "State government", "Without pay", "Never worked"])
EmpMstatus = gr.Dropdown(label="Marital Status", choices=["Married-A F spouse present", "Never married", "Divorced", "Widowed", "Separated", "Married-spouse absent", "Married-civilian spouse present"])
EmpRace = gr.Dropdown(label="Race", choices=["White", "Black", "Asian or Pacific Islander", "Other"])
EmpHispanic = gr.Dropdown(label="Is Hispanic", choices=["All other", "Mexican-American", "Mexican (Puerto Rico Only)", "Central or South American", "Cuban", "Do not know", "Chicano", "Puerto Rican"])
EmpCommit = gr.Dropdown(label="Employment Commitment", choices=["Children or Armed Forces","Full-time schedules", "Not in labor force", "PT for non-econ reasons usually FT", "PT for econ reasons usually PT", "Unemployed full-time", "PT for econ reasons usually FT", "Unemployed part- time", "PT for non-econ reasons usually PT", "PT for econ reasons usually FT", "Unemployed part-time"])
EmpWage = gr.Number(label="Wage Per Hour")
EmpWorkweeks = gr.Number(label="Working Weeks Per Year")
EmpIndust = gr.Dropdown(label="Industry Code Main", choices=["Other professional services", "Retail trade", "Construction", "Finance insurance and real estate", "Manufacturing-nondurable goods", "Transportation", "Public administration", "Manufacturing-durable goods", "Business and repair services", "Mining", "Social services", "Educational services", "Health services", "Personal services except private HH", "Communications"])
EmpOccup = gr.Dropdown(label="Occupation Code Main", choices=["Executive admin and managerial", "Sales", "Other service", "Craft repair and kindred", "Laborers except construction", "Operatives and kindred", "Professional specialty", "Adm support including clerical", "Private household services", "Transport equipment operatives", "Technicians and related support", "Farming forestry and fishing", "Precision production craft & repair", "Machine operators assmblrs & inspctrs", "Protective services", "Transportation and material moving"])
EmpTax = gr.Dropdown(label="Tax Status", choices=["Single", "Joint both under 65", "Joint both 65+", "Joint one under 65 & one 65+", "Joint one under 65 & one 65+"])
EmpCitizen = gr.Dropdown(label="Citizenship", choices=["native", "foreign born- U S citizen by naturalization", "foreign born- Not a citizen of U S"])

   
 
# define the gradion
gr.Interface(
   inputs=[EmpAge, EmpGender, EmpEdu, EmpClass, EmpMstatus, EmpRace, EmpHispanic, EmpCommit, EmpWage, EmpWorkweeks, EmpIndust, EmpOccup, EmpTax, EmpCitizen],
   fn=predict_income_limit,
  outputs=gr.Label(),
   title="Employee Income Limit",
   description="Enter Employee information to predict Income limit",
   live=True
).launch(share=True, inbrowser=True)

