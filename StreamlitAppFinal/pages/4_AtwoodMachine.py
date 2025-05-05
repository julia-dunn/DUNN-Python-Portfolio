import streamlit as st
import pandas as pd
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("The Atwood Machine Experiment")
st.write("Here is where you can input your data for the atwood machine experiment. How many mass configurations did you use?")
n = st.number_input("Number of mass configurations:", value=1)
dist = st.number_input("Distance masses were allowed to fall:", value=None, placeholder="(meters)")
st.session_state["distance"] = dist
mass1 = []
mass2 = []
Mtrial_1 = []
Mtrial_2 = []
Mtrial_3 = []
Mtrial_4 = []
Mtrial_5 = []
for i in range(n):
    st.markdown(f" #### Configuration {i+1}:")
    c1, c2 = st.columns(2)
    m1 = c1.number_input(f"Mass 1", value=None, placeholder="(kg)", key=f"m1_{i}")
    m2 = c2.number_input(f"Mass 2", value=None, placeholder="(kg)", key=f"m2_{i}")
    c1, c2, c3, c4, c5 = st.columns(5)
    Mt1 = c1.number_input(f"Trial 1", value=None, placeholder="time(s)", key=f"Mt1_{i}")
    Mt2 = c2.number_input(f"Trial 2", value=None, placeholder="time(s)", key=f"Mt2_{i}")
    Mt3 = c3.number_input(f"Trial 3", value=None, placeholder="time(s)", key=f"Mt3_{i}")
    Mt4 = c4.number_input(f"Trial 4", value=None, placeholder="time(s)", key=f"Mt4,{i}")
    Mt5 = c5.number_input(f"Trial 5", value=None, placeholder="time(s)", key=f"Mt5_{i}")

    mass1.append(m1)
    mass2.append(m2)
    Mtrial_1.append(Mt1)
    Mtrial_2.append(Mt2)
    Mtrial_3.append(Mt3)
    Mtrial_4.append(Mt4)
    Mtrial_5.append(Mt5)

df_machine = pd.DataFrame({
    "Mass 1 (kg)": mass1,
    "Mass 2 (kg)": mass2,
    "Trial 1 (s)": Mtrial_1,
    "Trial 2 (s)": Mtrial_2,
    "Trial 3 (s)": Mtrial_3,
    "Trial 4 (s)": Mtrial_4,
    "Trial 5 (s)": Mtrial_5
})

st.markdown("#### Data Entered:")
columns5 = df_machine.columns[1:5]
df_machine["Average Time (s)"] = df_machine[columns5].mean(axis=1)
st.dataframe(df_machine)

if dist: 
    df_machine["Calculated 'g' (m/s^2)"] = 2 * dist * (df_machine["Mass 1 (kg)"] + df_machine["Mass 2 (kg)"])/(df_machine["Average Time (s)"]**2 * (df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"]))
    df_machine["Calculated uncertainty"] = (((0.0004*(df_machine["Mass 1 (kg)"] + df_machine["Mass 2 (kg)"]))/(df_machine["Average Time (s)"]**2 * (df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"])))**2 + ((0.001*(df_machine["Mass 1 (kg)"] + df_machine["Mass 2 (kg)"]))/(df_machine["Average Time (s)"]**2) * (df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"]))**2 + 2*((0.000774 * df_machine["Average Time (s)"]**2 * ((df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"]) - (df_machine["Mass 1 (kg)"] + df_machine["Mass 2 (kg)"])))/((df_machine["Average Time (s)"]**2 * (df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"]))**2))**2)**0.5
    avg_g_M = df_machine["Calculated 'g' (m/s^2)"].mean()
    avg_uncert_M = df_machine["Calculated uncertainty"].mean()
    st.write(f"Average 'g': {avg_g_M:0.2f} (m/s^2)")
    st.write(f"Average uncertainty: {avg_uncert_M:0.2f}")
    fig, ax = plt.subplots()
    ax.set_ylim(8,25)
    ax.errorbar(df_machine.index, df_machine["Calculated 'g' (m/s^2)"], yerr=df_machine["Calculated uncertainty"], fmt='o', capsize=5)
    ax.set_xlabel("Index")
    ax.set_ylabel("Calculated 'g' (m/s^2)")
    st.pyplot(fig)
    st.session_state["avg_g_M"] = avg_g_M
    st.session_state["avg_uncert_M"] = avg_uncert_M

st.session_state["df_machine"] = df_machine