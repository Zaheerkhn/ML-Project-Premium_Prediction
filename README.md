# Insurance Premium Prediction

Welcome to the Insurance Premium Prediction project! This web application leverages machine learning to predict insurance premiums based on user inputs, helping individuals understand their potential insurance costs based on various factors.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Model Details](#model-details)

## Overview

This project is designed to provide users with an intuitive interface to estimate their insurance premiums based on personal and medical information. It utilizes machine learning models trained on historical data to deliver accurate predictions.

## Features

- **User-Friendly Interface**: Simple and clean layout for easy navigation.
- **Input Fields**: Collects various user attributes, including age, number of dependants, income level, insurance plan, and medical history.
- **Real-Time Predictions**: Instant predictions based on user inputs using two distinct machine learning models for different age groups.

## Technologies Used

- **Frontend**: Streamlit
- **Backend**: Python
- **Machine Learning**: XGBoost
- **Data Handling**: Pandas
- **Serialization**: Joblib

## Installation

To set up the project locally, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/insurance-premium-prediction.git
   cd insurance-premium-prediction
   
2. **Create a virtual environment (optional but recommended)**:
    ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   
3. **Install the required packages**:
    ```bash
   pip install -r requirements.txt
   
4. **Run the Streamlit app**:
   ```bash
   streamlit run main.py

## Usage
1. Open the Streamlit app in your web browser (usually at http://localhost:8501).
2. Fill in the required fields such as age, number of dependants, income, insurance plan, gender, medical history, etc.
3. Click the "Predict" button to receive your estimated insurance premium.

## How It Works
1. Data Input: Users enter their details into the app.
2. Data Preprocessing: The input data is preprocessed, including encoding categorical variables and normalizing numerical values.
3. Model Prediction: Based on the user's age, the relevant machine learning model is utilized to predict the insurance premium.
4. Output: The app displays the predicted insurance premium to the user.

## Model Details
The project includes two models:
* Model for Young Users (model_young): Trained on data for users aged 25 and below.
* Model for Older Users (model_rest): Trained on data for users above 25.
  Both models are saved in the Artifacts/ directory as joblib files, alongside their respective scalers.
