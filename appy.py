import streamlit as st
import pandas as pd
import numpy as np
import pickle
import joblib
from sklearn import preprocessing
from sklearn.svm import SVC
from sklearn.preprocessing import LabelEncoder


# Load the trained model and label encoder from pickle files
with open('svc.pkl', 'rb') as f:
    final_svm_model = pickle.load(f)


# Your list of diseases
diseases = [
    "(vertigo) Paroymsal  Positional Vertigo",
    "AIDS",
    "Acne",
    "Alcoholic hepatitis",
    "Allergy",
    "Arthritis",
    "Bronchial Asthma",
    "Cervical spondylosis",
    "Chicken pox",
    "Chronic cholestasis",
    "Common Cold",
    "Dengue",
    "Diabetes",
    "Dimorphic hemmorhoids(piles)",
    "Drug Reaction",
    "Fungal infection",
    "GERD",
    "Gastroenteritis",
    "Heart attack",
    "Hepatitis B",
    "Hepatitis C",
    "Hepatitis D",
    "Hepatitis E",
    "Hypertension",
    "Hyperthyroidism",
    "Hypoglycemia",
    "Hypothyroidism",
    "Impetigo",
    "Jaundice",
    "Malaria",
    "Migraine",
    "Osteoarthristis",
    "Paralysis (brain hemorrhage)",
    "Peptic ulcer diseae",
    "Pneumonia",
    "Psoriasis",
    "Tuberculosis",
    "Typhoid",
    "Urinary tract infection",
    "Varicose veins",
    "hepatitis A"
]

# Create a LabelEncoder and fit it to the diseases
label_encoder = LabelEncoder()
label_encoder.fit(diseases)

# Now label_encoder is a LabelEncoder object fitted on your diseases
# You can access the classes_ attribute
print(label_encoder.classes_)




# Load the DataFrame from a CSV file
train_df = pd.read_csv('Training.csv')

# Get the features and target
X = train_df.iloc[:,:-1]
y = train_df.iloc[:, -1]

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
# Function to recommend precautions for predicted disease
def recommend_precautions(predicted_disease):

    precautions_df = pd.read_csv("precautions_df.csv")

    precautions_recommendation = precautions_df[precautions_df["Disease"] == predicted_disease][["Precaution_1", "Precaution_2", "Precaution_3", "Precaution_4"]].values
    if len(precautions_recommendation) > 0:
        return precautions_recommendation[0]
    else:
        return ["No precautions recommendation found for this disease."]
# Function to recommend medications for predicted disease
def recommend_medication(predicted_disease):

    medication_df = pd.read_csv("medications.csv")

    medication_recommendation = medication_df[medication_df["Disease"] == predicted_disease]["Medication"].values
    if len(medication_recommendation) > 0:
        return medication_recommendation[0]
    else:
        return "No medication recommendation found for this disease."
# Function to recommend diet for predicted disease
def recommend_diet(predicted_disease):

    diet_df = pd.read_csv("diets.csv")

    diet_recommendation = diet_df[diet_df["Disease"] == predicted_disease]["Diet"].values
    if len(diet_recommendation) > 0:
        return diet_recommendation[0]
    else:
        return "No diet recommendation found for this disease."

# Defining the Function
def predictDisease(symptoms):
    # creating input data for our model
    input_data = [0] * len(data_dict["symptom_index"])
    for symptom in symptoms:
        index = data_dict["symptom_index"][symptom]
        input_data[index] = 1


    input_data = np.array(input_data).reshape(1,-1)
    svm_prediction = data_dict["predictions_classes"][final_svm_model.predict(input_data)[0]]
        # Predicted disease
    predicted_disease = svm_prediction

    # Recommendations for the predicted disease
    medication_recommendation = recommend_medication(predicted_disease)
    precautions_recommendation = recommend_precautions(predicted_disease)
    diet_recommendation = recommend_diet(predicted_disease)

    return predicted_disease, medication_recommendation, precautions_recommendation, diet_recommendation


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
