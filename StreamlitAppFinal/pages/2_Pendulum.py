import streamlit as st
import pandas as pd
st.title("The Pendulum Experiment!")
st.write("Here is where you can imput your data from the pendulum experiment")
st.markdown(" ### Changing Angle")
st.write("Here, input the length of your pendulum, the different angles of elevation you used, and the time it took to complete 5 oscillations.")
st.number_input("Length of pendulum [m]", value=None, placeholder="(meters)")
n = st.number_input("Number of Angles:", value=1)
angles = []
Atrial_1 = []
Atrial_2 = []
Atrial_3 = []
c1, c2, c3, c4 = st.columns(4)
for i in range(n):
    angle = c1.number_input(f"Angle of Elevation {i+1}", value=None, placeholder="(degrees)", key=f"A_{i}")
    At1 = c2.number_input(f"Trial 1", value=None, placeholder="Time (s)", key=f"At1_{i}")
    At2 = c3.number_input(f"Trial 2", value=None, placeholder="Time (s)", key=f"At2_{i}")
    At3 = c4.number_input(f"Trial 3", value=None, placeholder="Time (s)", key=f"At3_{i}")

    angles.append(angle)
    Atrial_1.append(At1)
    Atrial_2.append(At2)
    Atrial_3.append(At3)

df_angles = pd.DataFrame({
    "Angle (degrees)": angles,
    "Trial 1 (s)": Atrial_1,
    "Trial 2 (s)": Atrial_2,
    "Trial_3 (s)": Atrial_3
})
st.markdown("#### Entered Data:")
st.dataframe(df_angles)

st.markdown(" ### Changing Length")
st.write("Here, input the angle of elevation, the different lengths of the pendulum, and the time it took to complete 5 oscillations.")
st.number_input("Angle of Elevation (degrees)", value=None, placeholder="(degrees)")
m = st.number_input("Number of Lengths:", value=1)
lengths = []
Ltrial_1 = []
Ltrial_2 = []
Ltrial_3 = []
c1, c2, c3, c4 = st.columns(4)
for i in range(m):
    length = c1.number_input(f"Length {i+1}", value=None, placeholder="(meters)", key=f"L_{i}")
    Lt1 = c2.number_input(f"Trial 1", value=None, placeholder="Time (s)", key=f"Lt1_{i}")
    Lt2 = c3.number_input(f"Trial 2", value=None, placeholder="Time (s)", key=f"Lt2_{i}")
    Lt3 = c4.number_input(f"Trial 3", value=None, placeholder="Time (s)", key=f"Lt3_{i}")

    lengths.append(length)
    Ltrial_1.append(Lt1)
    Ltrial_2.append(Lt2)
    Ltrial_3.append(Lt3)

df_lengths = pd.DataFrame({
    "Length (meters)": lengths,
    "Trial 1 (s)": Ltrial_1,
    "Trial 2 (s)": Ltrial_2,
    "Trial 3 (s)": Ltrial_3
})
st.markdown("#### Entered Data:")
st.dataframe(df_lengths)