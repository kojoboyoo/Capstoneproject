# Income Prediction Project
 
This project aims to predict income levels based on various demographic features using machine learning. The predictive model is built using CatBoost, Decision Tree, and Logistic Regression algorithms. The best-performing model, Decision Tree, achieved an accuracy of 97%.
 
![income_prediction](https://github.com/doeabla/Income_prediction_app/assets/137217264/58793d76-b0c1-4af9-95db-cb1c6c4d1412)
 
 
## Table of Contents
- [Introduction](#introduction)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Modeling](#modeling)
- [Evaluation](#evaluation)
- [Deployment](#deployment)
- [Usage](#usage)
- [Acknowledgments](#acknowledgments)
 
## Introduction
 
The growing disparity in income distribution poses a significant challenge, especially in developing nations. Traditional methods of monitoring income levels between census years are costly and may lack accuracy. This project addresses this issue by employing machine learning to predict income levels, offering a more efficient and precise alternative for policymakers.
 
## Exploratory Data Analysis (EDA)
For this project, datasets provided on [Zindi](https://zindi.africa/competitions/income-prediction-challenge-for-azubian/data) was used. Below are steps followed to complete this project.
 
#### 1. Load and Analyze Data:
 
* Load the train and test datasets.
 
* Analyze and preprocess the data.
 
* Explore the distribution of features and the target variable.
 
#### 2. Train a Machine Learning Model:
 
* Split the dataset into features (X) and target (y).
 
* Balance the dataset
 
* Create pipeline 
- EDA was performed to understand the distribution of income across various demographic features.
- Visualizations were created to analyze the relationships between age, gender, education, work class, marital status, race, etc., with income levels.
 
## Modeling
 
Three machine learning models were used for predicting income levels:
 
1. **CatBoost**
2. **Decision Tree**
3. **Logistic Regression**
 
The Decision Tree model outperformed others, achieving an accuracy of 97%.
#### 3. Save the Model:
 
* After training the model, save it using joblib so that it can be loaded later for predictions.
(<img width="843" alt="Screenshot 2024-01-11 at 9 42 11 PM" src="https://github.com/kojoboyoo/Capstoneproject/assets/137324360/2ad21062-8413-4f7a-bb11-3219b39532ea">
)
 
 
## Evaluation
 
The evaluation metrics for the Decision Tree model include accuracy, precision, recall, and F1-score. Detailed information about the model's performance can be found in the respective sections of the project.
<img width="543" alt="Screenshot 2024-01-11 at 9 47 46 PM" src="https://github.com/kojoboyoo/Capstoneproject/assets/137324360/214a518f-49ce-4e3a-9255-ce7976a8062d">

 
## Deployment
 
The Decision Tree model was deployed using various frameworks for interactive user interfaces:
 
1. **Streamlit App**
   - A user-friendly web app created with Streamlit for exploring predictions interactively.
<img width="871" alt="Screenshot 2024-01-11 at 9 51 33 PM" src="https://github.com/kojoboyoo/Capstoneproject/assets/137324360/7c491e8f-4df0-4ec3-9cf3-cf691fc91e87">

snapshot of code to build streamlit app
 
<img width="620" alt="Screenshot 2024-01-11 at 9 53 48 PM" src="https://github.com/kojoboyoo/Capstoneproject/assets/137324360/ea443568-7f5c-4999-8da2-40fb1aa86eb6">

snapshot of app
 
<img width="593" alt="Screenshot 2024-01-11 at 9 56 09 PM" src="https://github.com/kojoboyoo/Capstoneproject/assets/137324360/da9680c0-788e-4db1-a966-f57928f740dd">

snapshot of response message after prediction
 
2. **Gradio App**
   - Another web app created with Gradio, providing a simple and intuitive interface for making predictions.
<img width="717" alt="Screenshot 2024-01-11 at 10 03 35 PM" src="https://github.com/kojoboyoo/Capstoneproject/assets/137324360/3354fe7b-0804-4503-a4ce-9d89d10c7660">

snapshot of code to build gradio app
 
<img width="1560" alt="Screenshot 2024-01-11 at 10 12 11 PM" src="https://github.com/kojoboyoo/Capstoneproject/assets/137324360/b840f5db-9249-4313-b424-27544417506f">

snapshot demonstrating performance of gradio app
 
3. **FastAPI**
   - A web API built with FastAPI to serve predictions programmatically.
<img width="1084" alt="Screenshot 2024-01-12 at 7 35 10 AM" src="https://github.com/kojoboyoo/Capstoneproject/assets/137324360/9d5c369a-bc53-49b1-9054-637daf3d887a">

snapshot of code for building fastapi
 
<img width="1159" alt="Screenshot 2024-01-12 at 7 18 39 AM" src="https://github.com/kojoboyoo/Capstoneproject/assets/137324360/39128c4d-19ef-4d70-a9f7-c23f61faac02">

snapsot of performance of fastapi
 
4. **Dockerize the Application**
 
* Write a Dockerfile to containerize your FastAPI application.
 
* Build the Docker image.
 
* Run the Docker container.
<img width="886" alt="Screenshot 2024-01-12 at 7 21 00 AM" src="https://github.com/kojoboyoo/Capstoneproject/assets/137324360/448ba663-4480-4737-b588-4de866a480c0">

snapshot of dockerfile
 
## Usage
 
- Clone the repository:
 
```bash
git clone https://github.com/kojoboyoo/Capstoneproject.git
cd income-prediction
```
 
- Install dependencies:
 
```bash
pip install -r requirements.txt
```
- Run the Streamlit App:
```bash
streamlit run src/streamapp.py
```
- Run the Gradio App:
 
```bash
python src/gradapp.py
```
- Run FastAPI:
```bash
uvicorn src.main:app --reload
```
 
Access the respective URLs provided in the console for each deployment.
 
## Acknowledgements
We extend our sincere gratitude to Azubi Africa for providing us with the invaluable opportunity to be part of their educational programs. The experience gained during our time as students has been truly enriching and impactful. We appreciate the dedication of the mentors, instructors, and the entire Azubi Africa team for their unwavering support and commitment to our learning journey.
 
 
## Authors
| Name | GitHub link |
| ---- | ---- |
| Doe Edinam                   | https://github.com/doeabla         |
| Enoch Taylor-Nketiah         | https://github.com/kojoboyoo       |
| Kofi Asare Bamfo             | https://github.com/akbamfo         |
 
 
| Project |	Name |Streamlit_App | Gradio_App| Fast_Api|
| ---- | -----| ----- | ----- | ----- |
| Capstone| Income_Prediction_Project |	[Streamapp](http://localhost:8501/) | [Gradapp](https://eeaca88f56287038da.gradio.live/) | [Fast_Api](http://127.0.0.1:8000/docs#/default/predict_predict_post)|
 
Find contanerized API on [Dockerhub](https://hub.docker.com/repository/docker/kojoboyoo/income_limits1/general)
