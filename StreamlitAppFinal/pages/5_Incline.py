import streamlit as st
import pandas as pd
st.title("The Incline Experiment")
st.write("Here you can input your data for the incline experiment. First, input the standard dimensions for your setup.")
st.number_input("Radius of marble:", value=None, placeholder="(meters)")
st.number_input("Mass of marble:", value=None, placeholder="(grams)")
st.number_input("Length of track:", value=None, placeholder="(meters)")
st.write("You must also input the number of configurations you tested, that is the different heights you set the track to.")
n = st.number_input("Number of heights:", value=1)
for i in range(n):
    st.markdown(f" #### Configuration {i+1}")
    st.number_input(f"Height of track ({i+1})", value=None, placeholder="(meters)")
    st.number_input(f"Distance traveled along track ({i+1})", value=None, placeholder="(meters)")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.number_input(f"Trial 1 ({i+1})", value=None, placeholder="time(s)")
    c2.number_input(f"Trial 2 ({i+1})", value=None, placeholder="time(s)")
    c3.number_input(f"Trial 3 ({i+1})", value=None, placeholder="time(s)")
    c4.number_input(f"Trial 4 ({i+1})", value=None, placeholder="time(s)")
    c5.number_input(f"Trial 5 ({i+1})", value=None, placeholder="time(s)")