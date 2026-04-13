import streamlit as st
from components.input_form import get_user_input
from components.result_display import show_result
from utils.api_client import get_prediction

st.title("AI Disease Prediction System")

data = get_user_input()

if st.button("Predict"):
    result = get_prediction(data)
    show_result(result)