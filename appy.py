import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn import preprocessing
from sklearn.svm import SVC

# Load the trained model and label encoder from pickle files
with open('svc.pkl', 'rb') as f:
    final_svm_model = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

# Your existing code for creating symptom index dictionary
symptoms = X.columns.values
symptom_index = {}
for index, value in enumerate(symptoms):
    symptom = " ".join([i.capitalize() for i in value.split("_")])
    symptom_index[symptom] = index

data_dict = {
    "symptom_index":symptom_index,
    "predictions_classes":label_encoder.classes_
}

# Your existing code for prediction, precautions, medication, and diet recommendation
# ...

# Load the data files
precautions_df = pd.read_csv("precautions_df.csv")
medication_df = pd.read_csv("medications.csv")
diet_df = pd.read_csv("diets.csv")

def main():
    # Custom CSS for the title
    st.markdown("""
    <style>
    .reportview-container .main .block-container {
        padding: 14px;
    }
    .title {
        background-color: green;
        padding: 14px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title"><h1>Disease Prediction System</h1></div>', unsafe_allow_html=True)
    st.markdown("Google")


    # User input symptoms
    symptoms = st.text_input("Enter the symptoms separated by commas:")

    if st.button("Predict"):
        symptoms_list = [symptom.strip() for symptom in symptoms.split(",")]
        predicted_disease, medication_recommendation, precautions_recommendation, diet_recommendation = predictDisease(symptoms_list)

        # Display the results
        st.write("Predicted Disease:", predicted_disease)
        st.write("Recommended Medication:", medication_recommendation)
        st.write("Recommended Precautions:")
        for precaution in precautions_recommendation:
            st.write("-", precaution)
        st.write("Recommended Diet:", diet_recommendation)

if __name__ == "__main__":
    main()
