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
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/1fbb4566-5ee1-436e-8bba-b032c470ce0d)
 
 
## Evaluation
 
The evaluation metrics for the Decision Tree model include accuracy, precision, recall, and F1-score. Detailed information about the model's performance can be found in the respective sections of the project.
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/244891dc-c899-425d-97b9-d5f5e36bfebe)
 
## Deployment
 
The Decision Tree model was deployed using various frameworks for interactive user interfaces:
 
1. **Streamlit App**
   - A user-friendly web app created with Streamlit for exploring predictions interactively.
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/bec6286b-d98f-49a1-97ec-12ca8433a841)
snapshot of code to build streamlit app
 
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/02d1c9ed-8dd3-4938-b050-36ed7c05e78d)
snapshot of app
 
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/ef945bd5-b292-46d3-98ed-ada85bb23315)
snapshot of response message after prediction
 
2. **Gradio App**
   - Another web app created with Gradio, providing a simple and intuitive interface for making predictions.
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/ef68e6ed-d202-429e-bb4b-d32652d4fa24)
snapshot of code to build gradio app
 
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/b8e72429-9c1f-4171-9432-0cac4ab102f5)
snapshot demonstrating performance of gradio app
 
3. **FastAPI**
   - A web API built with FastAPI to serve predictions programmatically.
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/f5b14c9d-3b8c-4bf4-bb12-95e104556e7e)
snapshot of code for building fastapi
 
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/ef9f8ccd-6099-43ae-9132-b801ef124b0f)
snapsot of performance of fastapi
 
4. **Dockerize the Application**
 
* Write a Dockerfile to containerize your FastAPI application.
 
* Build the Docker image.
 
* Run the Docker container.
![image](https://github.com/doeabla/Income_prediction_app/assets/137217264/302e9c75-f6c1-47a1-b476-257eec151f9d)
snapshot of dockerfile
 
## Usage
 
- Clone the repository:
 
```bash
git clone https://github.com/doeabla/Income_prediction_app.git

```
 
- Install dependencies:
 
```bash
pip install -r requirements.txt
```
- Run the Streamlit App:
```bash
streamlit run streamapp.py
```
- Run the Gradio App:
 
```bash
python gradapp.py
```
- Run FastAPI:
```bash
uvicorn main:app --reload
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
 
Find contanerized API on [Dockerhub](https://hub.docker.com/repository/docker/abladoe/income_predict/general)