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
    c1.number_input(f"Angle of Elevation {i+1}", value=None, placeholder="(degrees)", key=f"A_{i}")
    c2.number_input(f"Trial 1", value=None, placeholder="Time (s)", key=f"At1_{i}")
    c3.number_input(f"Trial 2", value=None, placeholder="Time (s)", key=f"At2_{i}")
    c4.number_input(f"Trial 3", value=None, placeholder="Time (s)", key=f"At3_{i}")
st.markdown(" ### Changing Length")
st.write("Here, input the angle of elevation, the different lengths of the pendulum, and the time it took to complete 5 oscillations.")
st.number_input("Angle of Elevation (degrees)", value=None, placeholder="(degrees)")
m = st.number_input("Number of Lengths:", value=1)
c1, c2, c3, c4 = st.columns(4)
for i in range(m):
    c1.number_input(f"Length {i+1}", value=None, placeholder="(meters)", key=f"L_{i}")
    c2.number_input(f"Trial 1", value=None, placeholder="Time (s)", key=f"Lt1_{i}")
    c3.number_input(f"Trial 2", value=None, placeholder="Time (s)", key=f"Lt2_{i}")
    c4.number_input(f"Trial 3", value=None, placeholder="Time (s)", key=f"Lt3_{i}")