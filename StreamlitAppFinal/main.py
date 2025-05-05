import streamlit as st
import pandas as pd
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Physics Right of Passage: Calculating 'g'")
st.write("Welcome to the best new app for university physics students. This app is built to help you with your introductory physics lab. Many students, myself included, spend the first semester in lab calculating the acceleration due to gravity in 4 different ways: with a pendulum, in free fall, with an Atwood machine, or on an incline. But which is the most accurate?")
st.markdown(" ### The Experiments!")
st.write("When calculating 'g,' there are four different methods typically used in a basic Physics 1 course. To learn more about the setup, click below to navigate to the 'Instructions' page.")
st.page_link("pages/1_Instructions.py", label="Instructions", icon="📝")
st.write("These are the four classical methods! To input your data and analyze the results, click the method you used!")
st.page_link("pages/2_Pendulum.py", label="Pendulum", icon="📍")
st.page_link("pages/3_FreeFall.py", label="Free Fall", icon="📍")
st.page_link("pages/4_AtwoodMachine.py", label="Atwood Machine", icon="📍")
st.page_link("pages/5_Incline.py", label="Incline", icon="📍")
st.markdown(" ### Results!")
st.write("Once you have inputted your data, click below to see the results! This platform will calculate the uncertainties for each experiment and compare their precision/accuracy. Uncertainty calculations are essential for the scientific method because they demonstrate the uncertainty of an experiment without human error, that is if done perfectly. Does your uncertainty account for the accuracy of your results? Or, is it possible the experiment could be improved?")
st.page_link("pages/6_Results.py", label="Results!", icon="🔎")
st.write("But what is uncertainty? And how is it calculated?")
