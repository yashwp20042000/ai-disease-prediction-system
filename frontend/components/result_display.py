import streamlit as st

def show_result(result):
    if result["prediction"] == 1:
        st.error("High risk of Diabetes")
    else:
        st.success("Low risk of Diabetes")