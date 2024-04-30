## Disease Classification and Drug Recommendation System
This system predicts diseases from symptoms and recommends medication, precautions, and diet tailored to each disease, enhancing health management.

## Introduction
Healthcare management can be significantly enhanced through the use of advanced technologies such as machine learning. This Disease Classification and Drug Recommendation System is designed to assist healthcare professionals and individuals in accurately diagnosing diseases based on reported symptoms and providing personalized recommendations for medication, precautions, and diet.

By leveraging machine learning algorithms, particularly Support Vector Machines (SVM), this system analyzes a wide range of symptoms and their correlations with various diseases. SVM is chosen for its ability to effectively handle high-dimensional data and nonlinear relationships, making it well-suited for disease classification tasks. The predictive model is trained on a comprehensive dataset containing symptom profiles and corresponding diagnoses, allowing it to learn complex patterns and make accurate predictions.

Once symptoms are inputted into the system, it employs the trained SVM model to predict the most likely disease and offers tailored recommendations for effective treatment and management. With the ability to rapidly identify diseases and provide targeted recommendations, this system aims to streamline healthcare processes, improve patient outcomes, and empower individuals to take proactive measures for their health and well-being.

## Getting Started
Prerequisites

Python 3.x

Training and testing datasets (provided in CSV format)
### Usage
Run the ipynb file.
Enter symptoms separated by commas when prompted.
View the predicted disease along with recommended medication, precautions, and diet.
### Example Usage
Enter the symptoms separated by commas: Muscle Pain, Headache, Nausea, High Fever, Sweating, Vomiting

Predicted Disease: Malaria
Recommended Medication: Antimalarial drugs, Antipyretics, Antiemetic drugs, IV fluids, Blood transfusions
Recommended Precautions: Consult nearest hospital, avoid oily food, avoid non veg food, keep mosquitos out
Recommended Diet: Malaria Diet, Hydration, High-Calorie Diet, Soft and bland foods, Oral rehydration solutions



