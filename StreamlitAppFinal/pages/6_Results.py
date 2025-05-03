import streamlit as st
import pandas as pd
import math

df_angles = st.session_state["df_angles"]
df_lengths = st.session_state["df_lengths"]
df_stopwatch = st.session_state["df_stopwatch"]
df_photogate = st.session_state["df_stopwatch"]
df_machine = st.session_state["df_machine"]
df_incline = st.session_state["df_incline"]
Alength = st.session_state["Alength"]
Langle = st.session_state["Langle"]

st.title("Results!")
st.write("Here is where you can access the analysis of your data! ")

st.markdown("## Pendulum Experiment")
st.markdown("### Changing Angles")
if df_angles is not None:
    if Alength:
        df_angles["Average Time (s)"] = df_angles[["Trial 1 (s)", "Trial 2 (s)", "Trial 3 (s)"]].mean(axis=1)
        df_angles["Period (s)"] = df_angles["Average Time (s)"]/5
        df_angles["Calculated 'g' (m/s^2)"] = (4 * math.pi**2 * Alength)/((df_angles["Period (s)"])**2)
        df_angles["Calculated uncertainty"] = ((((0.005*2*math.pi)/(df_angles["Period (s)"]))**2)+((0.08*Alength*(math.pi**2)/(df_angles["Period (s)"])**3)))**0.5
        avg_g_A = df_angles["Calculated 'g' (m/s^2)"].mean()
        avg_uncert_A = df_angles["Calculated uncertainty"].mean()
        st.dataframe(df_angles)
        st.write(f"Average g: {avg_g_A:0.2f} m/s^2")
        st.write(f"Average uncertainty: {avg_uncert_A:0.2f}")
    else:
        st.warning("Pendulum length not given")
else:
    st.warning("Pendulum dataframe not defined")
st.markdown("### Changing Lengths")
if df_lengths is not None:
    if Langle:
        df_lengths["Average Time (s)"] = df_lengths[["Trial 1 (s)", "Trial 2 (s)", "Trial 3 (s)"]].mean(axis=1)
        df_lengths["Period (s)"] = df_lengths["Average Time (s)"]/5
        df_lengths["Calculated 'g' (m/s^2)"] = (4 * math.pi**2 *(df_lengths['Length (meters)']))/((df_lengths["Period (s)"])**2)
        df_lengths["Calculated uncertainty"] = ((((0.005*2*math.pi)/(df_lengths["Period (s)"]))**2)+((0.08*(df_lengths["Length (meters)"])*(math.pi**2)/(df_angles["Period (s)"])**3)))**0.5
        avg_g_L = df_lengths["Calculated 'g' (m/s^2)'"].mean()
        avg_uncert_L = df_lengths["Calculated uncertainty"].mean()
        st.dataframe(df_lengths)
        st.write(f"Average g: {avg_g_L:0.2f} m/s^2")
        st.write(f"Average uncertainty: {avg_uncert_L:0.2f}")
    else:
        st.warning("Pendulum angle not given")
else:
    st.warning("Pendulum dataframe not given")