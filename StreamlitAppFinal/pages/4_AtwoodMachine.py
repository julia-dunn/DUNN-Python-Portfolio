import streamlit as st
import pandas as pd
st.title("The Atwood Machine Experiment")
st.write("Here is where you can input your data for the atwood machine experiment. How many mass configurations did you use?")
n = st.number_input("Number of mass configurations:", value=1)
st.number_input("Distance masses were allowed to fall:", value=None, placeholder="(meters)")
for i in range(n):
    st.markdown(f" #### Configuration {i+1}:")
    c1, c2 = st.columns(2)
    c1.number_input(f"Mass 1 ({i+1})", value=None, placeholder="(grams)")
    c2.number_input(f"Mass 2 ({i+1})", value=None, placeholder="(grams)")
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.number_input(f"Trial 1 ({i+1})", value=None, placeholder="time(s)")
    c2.number_input(f"Trial 2 ({i+1})", value=None, placeholder="time(s)")
    c3.number_input(f"Trial 3 ({i+1})", value=None, placeholder="time(s)")
    c4.number_input(f"Trial 4 ({i+1})", value=None, placeholder="time(s)")
    c5.number_input(f"Trial 5 ({i+1})", value=None, placeholder="time(s)")
