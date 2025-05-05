import streamlit as st
import pandas as pd
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("The Freefall Experiment")
st.write("Here is where you can input your data for the free fall experiment, both when using a stopwatch and with photogates.")
st.markdown(" ### Stopwatch:")
n = st.number_input("Number of heights you dropped the ball from:", value=1)
Fheights = []
Strial_1 = []
Strial_2 = []
Strial_3 = []
Strial_4 = []
Strial_5 = []

for i in range(n):
    st.markdown(f" #### Configuration {i+1}")
    Fh = st.number_input(f"Height {i+1}", value=None, placeholder="(meters)", key=f"Fh_{i}")
    c1, c2, c3, c4, c5 = st.columns(5)
    St1 = c1.number_input(f"Trial 1", value=None, placeholder="time(s)", key=f"St1_{i}")
    St2 = c2.number_input(f"Trial 2", value=None, placeholder="time(s)", key=f"St2_{i}")
    St3 = c3.number_input(f"Trial 3", value=None, placeholder="time(s)", key=f"St3_{i}")
    St4 = c4.number_input(f"Trial 4", value=None, placeholder="time(s)", key=f"St4_{i}")
    St5 = c5.number_input(f"Trial 5", value=None, placeholder="time(s)", key=f"St5_{i}")

    Fheights.append(Fh)
    Strial_1.append(St1)
    Strial_2.append(St2)
    Strial_3.append(St3)
    Strial_4.append(St4)
    Strial_5.append(St5)

df_stopwatch = pd.DataFrame({
    "Height (m)": Fheights,
    "Trial 1 (s)": Strial_1,
    "Trial 2 (s)": Strial_2,
    "Trial 3 (s)": Strial_3,
    "Trial 4 (s)": Strial_4,
    "Trial 5 (s)": Strial_5
})
st.markdown("#### Entered Data")
columns3 = df_stopwatch.columns[1:5]
df_stopwatch["Average Time (s)"] = df_stopwatch[columns3].mean(axis=1)
df_stopwatch["Calculated 'g' (m/s^2)"] = 2 * df_stopwatch["Height (m)"]/(df_stopwatch["Average Time (s)"]**2)
df_stopwatch["Calculated uncertainty"] = (((-2 * 0.0005 * df_stopwatch["Height (m)"]/df_stopwatch["Average Time (s)"]**3)**2)+(0.02/df_stopwatch["Average Time (s)"]**2)**2)**0.5
avg_g_S = df_stopwatch["Calculated 'g' (m/s^2)"].mean()
avg_uncert_S = df_stopwatch["Calculated uncertainty"].mean()
st.dataframe(df_stopwatch)
st.write(f"Average g: {avg_g_S:0.2f} (m/s^2)")
st.write(f"Average uncertainty: {avg_uncert_S:0.2f}")
fig, ax = plt.subplots()
ax.set_ylim(1,15)
ax.errorbar(df_stopwatch.index, df_stopwatch["Calculated 'g' (m/s^2)"], yerr=df_stopwatch["Calculated uncertainty"], fmt='o', capsize=5)
ax.set_xlabel("Index")
ax.set_ylabel("Calculated 'g' (m/s^2)")
st.pyplot(fig)

st.session_state["df_stopwatch"] = df_stopwatch
st.session_state["avg_g_S"] = avg_g_S
st.session_state["avg_uncert_S"] = avg_uncert_S

st.markdown(" ### Photogates:")
m = st.number_input("Number of distances between photogates:", value=1)
Fdistances = []
Ptrial_1 = []
Ptrial_2 = []
Ptrial_3 = []
Ptrial_4 = []
Ptrial_5 = []

for i in range(m):
    st.markdown(f" #### Configuration {i+1}")
    Fd = st.number_input(f"Distance {i+1}", value=None, placeholder="(meters)", key=f"Fd_{i}")
    c1, c2, c3, c4, c5 = st.columns(5)
    Pt1 = c1.number_input(f"Trial 1", value=None, placeholder="time(s)", key=f"Pt1_{i}")
    Pt2 = c2.number_input(f"Trial 2", value=None, placeholder="time(s)", key=f"Pt2_{i}")
    Pt3 = c3.number_input(f"Trial 3", value=None, placeholder="time(s)", key=f"Pt3_{i}")
    Pt4 = c4.number_input(f"Trial 4", value=None, placeholder="time(s)", key=f"Pt4_{i}")
    Pt5 = c5.number_input(f"Trial 5", value=None, placeholder="time(s)", key=f"Pt5_{i}")

    Fdistances.append(Fd)
    Ptrial_1.append(Pt1)
    Ptrial_2.append(Pt2)
    Ptrial_3.append(Pt3)
    Ptrial_4.append(Pt4)
    Ptrial_5.append(Pt5)

df_photogate = pd.DataFrame({
    "Distance (m)": Fdistances,
    "Trial 1 (s)": Ptrial_1,
    "Trial 2 (s)": Ptrial_2,
    "Trial 3 (s)": Ptrial_3,
    "Trial 4 (s)": Ptrial_4,
    "Trial 5 (s)": Ptrial_5
})

st.markdown("#### Entered Data:")
columns4 = df_photogate.columns[1:5]
df_photogate["Average Time (s)"] = df_photogate[columns4].mean(axis=1)
df_photogate["Calculated 'g' (m/s^2)"] = 2 * (df_photogate["Distance (m)"])/(df_photogate['Average Time (s)']**2)
df_photogate['Calculated uncertainty'] = (((-2 * 0.0005 * df_photogate["Distance (m)"]/(df_photogate["Average Time (s)"])**3)**2)+(0.02/(df_photogate["Average Time (s)"])**2)**2)**0.5
st.dataframe(df_photogate)
avg_g_P = df_photogate["Calculated 'g' (m/s^2)"].mean()
avg_uncert_P = df_photogate["Calculated uncertainty"].mean()
st.write(f"Average 'g': {avg_g_P:0.2f} (m/s^2)")
st.write(f"Average uncertainty: {avg_uncert_P:0.2f}")

fig, ax = plt.subplots()
ax.set_ylim(9,20)
ax.errorbar(df_photogate.index, df_photogate["Calculated 'g' (m/s^2)"], yerr=df_photogate["Calculated uncertainty"], fmt='o', capsize=5)
ax.set_xlabel("Index")
ax.set_ylabel("Calculated 'g' (m/s^2)")
st.pyplot(fig)

st.session_state["df_photogate"] = df_photogate
st.session_state["avg_g_P"] = avg_g_P
st.session_state["avg_uncert_P"] = avg_uncert_P