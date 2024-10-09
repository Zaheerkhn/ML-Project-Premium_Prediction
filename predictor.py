from joblib import load
import pandas as pd

# Load models and scalers
model_young = load("Artifacts/model_young.joblib")
model_rest = load("Artifacts/model_rest.joblib")
scaler_young = load("Artifacts/scaler_young.joblib")
scaler_rest = load("Artifacts/scaler_rest.joblib")

def calculate_risk_scores(medical_history):
    # Define risk scores
    risk_scores = {
        "diabetes": 6,
        "heart disease": 8,
        "high blood pressure": 6,
        "thyroid": 5,
        "no disease": 0,
        "none": 0
    }

    # Process medical history
    diseases = medical_history.lower().split(" & ")
    total_risk_score = sum(risk_scores.get(disease, 0) for disease in diseases)
    
    # Normalize the risk score
    max_score = 2 * max(risk_scores.values())  # Maximum possible score if two diseases
    normalized_risk_score = (total_risk_score) / (max_score)
    
    return normalized_risk_score

def preprocess_input(input_dict):
    # Define encoding for insurance_plan and income_level
    insurance_plan_encoding = {'Bronze': 1, 'Silver': 2, 'Gold': 3}
    income_level_encoding = {'<10L': 1, '10L - 25L': 2, '> 40L': 3, '25L - 40L': 4}

    # Initialize the output dictionary with expected columns and default values
    preprocessed_data = {
        'age': 0,
        'number_of_dependants': 0,
        'income_level': 0,  # Added this field
        'income_lakhs': 0,
        'insurance_plan': 0,
        'genetical_risk': 0,
        'normalized_risk_score': 0,
        'gender_Male': 0,
        'region_Northwest': 0,
        'region_Southeast': 0,
        'region_Southwest': 0,
        'marital_status_Unmarried': 0,
        'bmi_category_Obesity': 0,
        'bmi_category_Overweight': 0,
        'bmi_category_Underweight': 0,
        'smoking_status_Occasional': 0,
        'smoking_status_Regular': 0,
        'employment_status_Salaried': 0,
        'employment_status_Self-Employed': 0,
    }

    # Assign numeric values
    preprocessed_data['age'] = input_dict['Age']
    preprocessed_data['number_of_dependants'] = input_dict['Number of Dependants']
    preprocessed_data['income_lakhs'] = input_dict['Income (in Lakhs)']  # Keep this field as it is
    preprocessed_data['genetical_risk'] = input_dict['Genetical Risk']

    # Encode insurance_plan
    preprocessed_data['insurance_plan'] = insurance_plan_encoding[input_dict['Insurance Plan']]

    # Assign income_level based on income_lakhs
    if input_dict['Income (in Lakhs)'] < 10:
        preprocessed_data['income_level'] = 1
    elif 10 <= input_dict['Income (in Lakhs)'] < 25:
        preprocessed_data['income_level'] = 2
    elif 25 <= input_dict['Income (in Lakhs)'] < 40:
        preprocessed_data['income_level'] = 3
    else:
        preprocessed_data['income_level'] = 4  # For '> 40L'

    # Manually assign values for categorical features
    preprocessed_data['gender_Male'] = 1 if input_dict['Gender'] == 'Male' else 0
    preprocessed_data['region_Northwest'] = 1 if input_dict['Region'] == 'Northwest' else 0
    preprocessed_data['region_Southeast'] = 1 if input_dict['Region'] == 'Southeast' else 0
    preprocessed_data['region_Southwest'] = 1 if input_dict['Region'] == 'Southwest' else 0
    preprocessed_data['marital_status_Unmarried'] = 1 if input_dict['Marital Status'] == 'Unmarried' else 0
    preprocessed_data['bmi_category_Obesity'] = 1 if input_dict['BMI Category'] == 'Obesity' else 0
    preprocessed_data['bmi_category_Overweight'] = 1 if input_dict['BMI Category'] == 'Overweight' else 0
    preprocessed_data['bmi_category_Underweight'] = 1 if input_dict['BMI Category'] == 'Underweight' else 0
    preprocessed_data['smoking_status_Occasional'] = 1 if input_dict['Smoking Status'] == 'Occasional' else 0
    preprocessed_data['smoking_status_Regular'] = 1 if input_dict['Smoking Status'] == 'Regular' else 0
    preprocessed_data['employment_status_Salaried'] = 1 if input_dict['Employment Status'] == 'Salaried' else 0
    preprocessed_data['employment_status_Self-Employed'] = 1 if input_dict['Employment Status'] == 'Self-Employed' else 0

    # Convert to DataFrame
    df = pd.DataFrame([preprocessed_data])
    df['normalized_risk_score'] = calculate_risk_scores(input_dict['Medical History'])
    df = handle_scaling(input_dict['Age'], df)
    return df

def handle_scaling(age, df):
    # Scale age and income_lakhs column
    if age <= 25:
        scaler_object = scaler_young
    else:
        scaler_object = scaler_rest

    cols_to_scale = scaler_object['cols_to_scale']
    scaler = scaler_object['scaler']

    # Use a placeholder to keep the same column structure
    df['income_level'] = df['income_level']  # Retain this field for scaling
    df[cols_to_scale] = scaler.transform(df[cols_to_scale])

    return df   

def predict(input_dict):
    input_df = preprocess_input(input_dict)

    if input_dict['Age'] <= 25:
        prediction = model_young.predict(input_df)
    else:
        prediction = model_rest.predict(input_df)

    return int(prediction)

