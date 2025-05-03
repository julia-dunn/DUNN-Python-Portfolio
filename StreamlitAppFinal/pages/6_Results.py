import streamlit as st
import pandas as pd
import math
import numpy as np

st.title("Results!")
st.write("Here is where you can access the analysis of your data! ")

st.markdown("## Pendulum Experiment")
st.markdown("### Changing Angles")
if "df_angles" in st.session_state and "Alength" in st.session_state:
    df_angles = st.session_state["df_angles"]
    Alength = st.session_state["Alength"]
    if Alength:
        columns1 = df_angles.columns[1:3]
        df_angles["Average Time (s)"] = df_angles[columns1].mean(axis=1)
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
if "df_lengths" in st.session_state and "Langle" in st.session_state:
    df_lengths = st.session_state["df_lengths"]
    Langle = st.session_state["Langle"]
    if Langle:
        columns2 = df_lengths.columns[1:3]
        df_lengths["Average Time (s)"] = df_lengths[columns2].mean(axis=1)
        df_lengths["Period (s)"] = df_lengths["Average Time (s)"]/5
        df_lengths["Calculated 'g' (m/s^2)"] = (4 * math.pi**2 *(df_lengths['Length (meters)']))/((df_lengths["Period (s)"])**2)
        df_lengths["Calculated uncertainty"] = ((((0.005*2*math.pi)/(df_lengths["Period (s)"]))**2)+((0.08*(df_lengths["Length (meters)"])*(math.pi**2)/(df_angles["Period (s)"])**3)))**0.5
        avg_g_L = df_lengths["Calculated 'g' (m/s^2)"].mean()
        avg_uncert_L = df_lengths["Calculated uncertainty"].mean()
        st.dataframe(df_lengths)
        st.write(f"Average g: {avg_g_L:0.2f} m/s^2")
        st.write(f"Average uncertainty: {avg_uncert_L:0.2f}")
    else:
        st.warning("Pendulum angle not given")
else:
    st.warning("Pendulum dataframe not given")

st.markdown("## Freefall Experiment")
st.markdown("### Stopwatch")
if "df_stopwatch" in st.session_state:
    df_stopwatch = st.session_state["df_stopwatch"]
    columns3 = df_stopwatch.columns[1:5]
    df_stopwatch["Average Time (s)"] = df_stopwatch[columns3].mean(axis=1)
    df_stopwatch["Calculated 'g' (m/s^2)"] = 2 * df_stopwatch["Height (m)"]/df_stopwatch["Average Time (s)"]
    df_stopwatch["Calculated uncertainty"] = (((-2 * 0.0005 * df_stopwatch["Height (m)"]/df_stopwatch["Average Time (s)"]**3)**2)+(0.02/df_stopwatch["Average Time (s)"]**2)**2)**0.5
    avg_g_S = df_stopwatch["Calculated 'g' (m/s^2)"].mean()
    avg_uncert_S = df_stopwatch["Calculated uncertainty"].mean()
    st.dataframe(df_stopwatch)
    st.write(f"Average g: {avg_g_S:0.2f} (m/s^2)")
    st.write(f"Average uncertainty: {avg_uncert_S:0.2f}")
else: 
    st.warning("Freefall with stopwatch dataframe not given")

st.markdown("### Photogates")
if "df_photogate" in st.session_state:
    df_photogate = st.session_state["df_photogate"]
    columns4 = df_photogate.columns[1:5]
    df_photogate["Average Time (s)"] = df_photogate[columns4].mean(axis=1)
    df_photogate["Calculated 'g' (m/s^2)"] = 2 * (df_photogate["Distance (m)"])/(df_photogate['Average Time (s)']**2)
    df_photogate['Calculated uncertainty'] = (((-2 * 0.0005 * df_photogate["Distance (m)"]/(df_photogate["Average Time (s)"])**3)**2)+(0.02/(df_photogate["Average Time (s)"])**2)**2)**0.5
    avg_g_P = df_photogate["Calculated 'g' (m/s^2)"].mean()
    avg_uncert_P = df_photogate["Calculated uncertainty"].mean()
    st.dataframe(df_photogate)
    st.write(f"Average 'g': {avg_g_P:0.2f} (m/s^2)")
    st.write(f"Average uncertainty: {avg_uncert_P:0.2f}")
else: 
    st.warning("Freefall with photogates dataframe not given")

st.markdown("## Atwood Machine")
if "df_machine" in st.session_state and "distance" in st.session_state:
    df_machine = st.session_state["df_machine"]
    dist = st.session_state["distance"]
    if dist:
        columns5 = df_machine.columns[1:5]
        df_machine["Average Time (s)"] = df_machine[columns5].mean(axis=1)
        df_machine["Calculated 'g' (m/s^2)"] = 2 * dist * (df_machine["Mass 1 (kg)"] + df_machine["Mass 2 (kg)"])/(df_machine["Average Time (s)"]**2 * (df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"]))
        df_machine["Calculated uncertainty"] = (((0.0004*(df_machine["Mass 1 (kg)"] + df_machine["Mass 2 (kg)"]))/(df_machine["Average Time (s)"]**2 * (df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"])))**2 + ((0.001*(df_machine["Mass 1 (kg)"] + df_machine["Mass 2 (kg)"]))/(df_machine["Average Time (s)"]**2) * (df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"]))**2 + 2*((0.000774 * df_machine["Average Time (s)"]**2 * ((df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"]) - (df_machine["Mass 1 (kg)"] + df_machine["Mass 2 (kg)"])))/((df_machine["Average Time (s)"]**2 * (df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"]))**2))**2)**0.5
        avg_g_M = df_machine["Calculated 'g' (m/s^2)"].mean()
        avg_uncert_M = df_machine["Calculated uncertainty"].mean()
        st.dataframe(df_machine)
        st.write(f"Average 'g': {avg_g_M:0.2f} (m/s^2)")
        st.write(f"Average uncertainty: {avg_uncert_M:0.2f}")
    else:
        st.warning("Distance not given")
else:
    st.warning("Atwood Machine dataframe not given")

st.markdown("## Incline Experiment")
if "df_incline" in st.session_state and "Ilength" in st.session_state:
    df_incline = st.session_state["df_incline"]
    Ilength = st.session_state["Ilength"]
    if Ilength:
        columns6 = df_incline.columns[1:5]
        df_incline["Average Time (s)"] = df_incline[columns6].mean(axis=1)
        df_incline["Angle (radians)"] = np.arcsin(df_incline["Height (m)"]/Ilength)
        df_incline["Calculated 'g' (m/s^2)"] = 14 * df_incline["Distance x (m)"]/(5 * df_incline["Average Time (s)"]**2 * np.sin(df_incline["Angle (radians)"]))
        df_incline["Calculated uncertainty"] = ((14 * 0.0005 / (5 * df_incline["Average Time (s)"]**2 * np.sin(df_incline["Angle (radians)"])))**2 + ((0.28 * df_incline["Distance x (m)"])/(5 * df_incline["Average Time (s)"]**2 * np.sin(df_incline["Angle (radians)"])))**2 + ((14 * df_incline["Distance x (m)"] * np.cos(df_incline["Angle (radians)"]) * (1/np.sin(df_incline["Angle (radians)"])) * (2*(0.0005/(1 + (df_incline["Height (m)"]/Ilength)**2))**2))/(5 * (df_incline["Average Time (s)"]**2)))**2)**0.5
        avg_g_I = df_incline["Calculated 'g' (m/s^2)"].mean()
        avg_uncert_I = df_incline["Calculated uncertainty"].mean()
        st.dataframe(df_incline)
        st.write(f"Average g: {avg_g_I:0.2f} (m/s^2)")
        st.write(f"Average uncertainty: {avg_uncert_I:0.2f}")
    else:
        st.warning("Length not given")
else:
    st.warning("Incline dataframe not given")