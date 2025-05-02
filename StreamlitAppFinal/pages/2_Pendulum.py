import streamlit as st
import pandas as pd
st.title("The Pendulum Experiment!")
st.write("Here is where you can imput your data from the pendulum experiment")
st.markdown(" ### Changing Angle")
st.write("Here, input the length of your pendulum, the different angles of elevation you used, and the time it took to complete 5 oscillations.")
st.number_input("Length of pendulum [m]", value=None, placeholder="(meters)")
n = st.number_input("Number of Angles:", value=1)
c1, c2, c3, c4 = st.columns(4)
for i in range(n):
    c1.number_input(f"Angle of Elevation {i+1}", value=None, placeholder="(degrees)")
    c2.number_input(f"Angle {i+1} - trial 1", value=None, placeholder="Time (s)")
    c3.number_input(f"Angle {i+1} - trial 2", value=None, placeholder="Time (s)")
    c4.number_input(f"Angle {i+1} - trial 3", value=None, placeholder="Time (s)")
st.markdown(" ### Changing Length")
st.write("Here, input the angle of elevation, the different lengths of the pendulum, and the time it took to complete 5 oscillations.")
st.number_input("Angle of Elevation (degrees)", value=None, placeholder="(degrees)")
m = st.number_input("Number of Lengths:", value=1)
c1, c2, c3, c4 = st.columns(4)
for i in range(m):
    c1.number_input(f"Length {i+1}", value=None, placeholder="(meters)")
    c2.number_input(f"Length {i+1} - trial 1", value=None, placeholder="Time (s)")
    c3.number_input(f"Length {i+1} - trial 2", value=None, placeholder="Time (s)")
    c4.number_input(f"Length {i+1} - trial 3", value=None, placeholder="Time (s)")