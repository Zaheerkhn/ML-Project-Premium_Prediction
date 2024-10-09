import streamlit as st
from predictor import predict

# Define the categorical columns and their options in a dictionary
categorical_columns = {
    "Gender": ['Male', 'Female'],
    "Region": ['Northeast', 'Northwest', 'Southeast', 'Southwest'],
    "Marital Status": ['Unmarried', 'Married'],
    "BMI Category": ['Overweight', 'Underweight', 'Normal', 'Obesity'],
    "Smoking Status": ['Regular', 'No Smoking', 'Occasional'],
    "Employment Status": ['Self-Employed', 'Freelancer', 'Salaried'],
    "Income Level": ['> 40L', '<10L', '10L - 25L', '25L - 40L'],
    "Medical History": ['High blood pressure', 'No Disease', 
                        'Diabetes & High blood pressure', 'Diabetes & Heart disease', 
                        'Diabetes', 'Diabetes & Thyroid', 'Heart disease', 
                        'Thyroid', 'High blood pressure & Heart disease'],
    "Insurance Plan": ['Silver', 'Bronze', 'Gold'],
    "Genetical Risk": [4, 3, 2, 1, 0, 5]
}

# Create input fields in a logical order using Streamlit's columns
st.title("Insurance Premium Prediction")

# Input fields for user input
col1, col2, col3 = st.columns(3)
gender = col1.selectbox("Gender", categorical_columns["Gender"])
age = col2.selectbox("Age", range(18, 101))
region = col3.selectbox("Region", categorical_columns["Region"])

col1, col2, col3 = st.columns(3)
marital_status = col1.selectbox("Marital Status", categorical_columns["Marital Status"])
number_of_dependants = col2.selectbox("Number of Dependants", range(0, 11))
bmi_category = col3.selectbox("BMI Category", categorical_columns["BMI Category"])

col1, col2, col3 = st.columns(3)
smoking_status = col1.selectbox("Smoking Status", categorical_columns["Smoking Status"])
employment_status = col2.selectbox("Employment Status", categorical_columns["Employment Status"])
income_lakhs = col3.selectbox("Income (in Lakhs)", range(1, 201))

col1, col2, col3 = st.columns(3)
medical_history = col1.selectbox("Medical History", categorical_columns["Medical History"])
insurance_plan = col2.selectbox("Insurance Plan", categorical_columns["Insurance Plan"])
genetical_risk = col3.selectbox("Genetical Risk", categorical_columns["Genetical Risk"])

# Define the input dictionary
input_dict = {
    "Gender": gender,
    "Age": age,
    "Region": region,
    "Marital Status": marital_status,
    "Number of Dependants": number_of_dependants,
    "BMI Category": bmi_category,
    "Smoking Status": smoking_status,
    "Employment Status": employment_status,
    "Income (in Lakhs)": income_lakhs,
    "Medical History": medical_history,
    "Insurance Plan": insurance_plan,
    "Genetical Risk": genetical_risk
}

if st.button('Predict'):
    prediction = predict(input_dict)  # Pass input_dict here
    st.success(f'Predicted Premium: {prediction}')
