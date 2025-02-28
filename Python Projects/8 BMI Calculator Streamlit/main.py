import streamlit as st
import pandas as pd

st.title("BMI Calculator")
height = st.slider("Enter the Height in Inches: ", 20, 250, 60)
weight = st.slider("Enter the Weight in kg: ", 20, 250, 75)

cm_height = height * 2.54
bmi = weight / ((cm_height/100) ** 2)
st.write(f"Your BMI is {bmi:.2f}")

st.write("### BMI Categories ###")

st.write("- Underweight: Less than 18.5.")
st.write("- Healthy Weight: 18.5 to less than 25.")
st.write("- Overweight: 25 to less than 30.")
st.write("- Obesity: 30 or greater.")