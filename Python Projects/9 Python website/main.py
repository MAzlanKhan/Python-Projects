import requests
import json
from PIL import Image
import streamlit as st
from streamlit_lottie import st_lottie

    
# Header
st.set_page_config(page_title="Azlan Khan", page_icon="q-face.png", layout="wide")

def load_lottie_file(filepath: str):
    with open(filepath, "r", encoding="utf-8") as f:
        return json.load(f) 

# # Annimation 
Lottie_coding = load_lottie_file("animation.json")
img_rute1 = Image.open("me.jpg")
img_rute2 = Image.open("bmi.png")

st.subheader("Hey! My name is Azlan Khan")
st.title("Future AI Angineer")
st.write("I'm a Student of PIAIC and currently doing Agentic Ai from there")

# Body 
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I Do?")
        st.write("##")
        st.write("""I am Azlan Khan, an 18-year-old website developer and CEO. I specialize in WordPress website development, creating responsive business, e-commerce, and blog websites. I am currently pursuing Robotics & AI Engineering from PIAIC and Intermediate (ICS) from Punjab Group of Colleges.
I have expertise in HTML, CSS, Bootstrap, C, and Python, and I am expanding my skills in AI and Full Stack Development. I have completed an AI beginners course from HP Life and am currently learning Python and AI concepts. My mega project, "Jarvis", is in development.
I am also interested in freelancing and starting my own agency to provide website development and AI solutions.""")
        st.write("[Linkedin:] https://www.linkedin.com/in/azlan-khan-00173b340/")

    with right_column:
        st_lottie(Lottie_coding)
        # st.image(img_rute ,width=600)
    
    # My Projects 
with st.container():
    st.write("---")
    st.subheader("My Projects")
    left_column, right_column = st.columns(2)
    with left_column:
        st.image(img_rute2)
    with right_column:
        st.title("BMI Calculator")
        st.write("This BMI (Body Mass Index) Calculator is a simple web application built using Streamlit. It allows users to input their weight (kg) and height (m or cm) to calculate their BMI score and determine their health category.")

    # Contact Us 
st.write("---")
st.subheader("Fill the Registration Form to Join Us!")
name = st.text_input("Your Name")
contact = st.text_input("Your Contact Number")
qualification = st.text_input("Your Qualification")
city = st.selectbox("Select a city:", ["Lahore", "Karachi", "Islamabad"])
resume = st.file_uploader("Upload your Resume/CV")
textArea = st.text_area("Enter the Message")
if st.form("Submit"):
    st.balloons()
    st.success("Form is Submitted Successfuly!")






