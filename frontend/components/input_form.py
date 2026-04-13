import streamlit as st

def get_user_input():
    pregnancies = st.number_input("Pregnancies")
    glucose = st.number_input("Glucose")
    bp = st.number_input("Blood Pressure")
    skin = st.number_input("Skin Thickness")
    insulin = st.number_input("Insulin")
    bmi = st.number_input("BMI")
    dpf = st.number_input("Diabetes Pedigree")
    age = st.number_input("Age")

    return {
        "pregnancies": pregnancies,
        "glucose": glucose,
        "blood_pressure": bp,
        "skin_thickness": skin,
        "insulin": insulin,
        "bmi": bmi,
        "diabetes_pedigree": dpf,
        "age": age
    }