import streamlit as st
import pandas as pd
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("The Pendulum Experiment!")
st.write("Here is where you can imput your data from the pendulum experiment")
st.markdown(" ### Changing Angle")
st.write("Here, input the length of your pendulum, the different angles of elevation you used, and the time it took to complete 5 oscillations.")
Alength = st.number_input("Length of pendulum [m]", value=None, placeholder="(meters)")
st.session_state["Alength"] = Alength
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
    "Trial 3 (s)": Atrial_3
})
st.markdown("#### Entered Data:")
columns1 = df_angles.columns[1:3]
df_angles["Average Time (s)"] = df_angles[columns1].mean(axis=1)
df_angles["Period (s)"] = df_angles["Average Time (s)"]/5
st.dataframe(df_angles)

if Alength:
    df_angles["Calculated 'g' (m/s^2)"] = (4 * math.pi**2 * Alength)/((df_angles["Period (s)"])**2)
    df_angles["Calculated uncertainty"] = ((((0.005*2*math.pi)/(df_angles["Period (s)"]))**2)+((0.08*Alength*(math.pi**2)/(df_angles["Period (s)"])**3)))**0.5
    avg_g_A = df_angles["Calculated 'g' (m/s^2)"].mean()
    avg_uncert_A = df_angles["Calculated uncertainty"].mean()
    st.write(f"Average g: {avg_g_A:0.2f} m/s^2")
    st.write(f"Average uncertainty: {avg_uncert_A:0.2f}")
    fig, ax = plt.subplots()
    ax.set_ylim(5,18)
    ax.errorbar(df_angles.index, df_angles["Calculated 'g' (m/s^2)"], yerr=df_angles["Calculated uncertainty"], fmt='o', capsize=5)
    ax.set_xlabel("Index")
    ax.set_ylabel("Calculated 'g' (m/s^2)")
    st.pyplot(fig)
    st.session_state["avg_g_A"] = avg_g_A
    st.session_state["avg_uncert_A"] = avg_uncert_A

st.session_state["df_angles"] = df_angles

st.markdown(" ### Changing Length")
st.write("Here, input the angle of elevation, the different lengths of the pendulum, and the time it took to complete 5 oscillations.")
Langle = st.number_input("Angle of Elevation (degrees)", value=None, placeholder="(degrees)")
st.session_state["Langle"] = Langle
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
columns2 = df_lengths.columns[1:3]
df_lengths["Average Time (s)"] = df_lengths[columns2].mean(axis=1)
df_lengths["Period (s)"] = df_lengths["Average Time (s)"]/5
st.dataframe(df_lengths)

if Langle:
    df_lengths["Calculated 'g' (m/s^2)"] = (4 * math.pi**2 *(df_lengths['Length (meters)']))/((df_lengths["Period (s)"])**2)
    df_lengths["Calculated uncertainty"] = ((((0.005*2*math.pi)/(df_lengths["Period (s)"]))**2)+((0.08*(df_lengths["Length (meters)"])*(math.pi**2)/(df_lengths["Period (s)"])**3)))**0.5
    avg_g_L = df_lengths["Calculated 'g' (m/s^2)"].mean()
    avg_uncert_L = df_lengths["Calculated uncertainty"].mean()
    st.write(f"Average g: {avg_g_L:0.2f} m/s^2")
    st.write(f"Average uncertainty: {avg_uncert_L:0.2f}")
    fig, ax = plt.subplots()
    ax.set_ylim(5,18)
    ax.errorbar(df_lengths.index, df_lengths["Calculated 'g' (m/s^2)"], yerr=df_lengths["Calculated uncertainty"], fmt='o', capsize=5)
    ax.set_xlabel("Index")
    ax.set_ylabel("Calculated 'g' (m/s^2)")
    st.pyplot(fig)
    st.session_state["avg_g_L"] = avg_g_L
    st.session_state["avg_uncert_L"] = avg_uncert_L

st.session_state["df_lengths"] = df_lengths