import streamlit as st
import pandas as pd
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Results!")
st.write("Here is where you can access the analysis of your data! ")

st.markdown("## Pendulum Experiment")
st.markdown("### Changing Angles")
if "df_angles" and "Alength"  and "avg_g_A" and "avg_uncert_A" in st.session_state:
    df_angles = st.session_state["df_angles"]
    Alength = st.session_state["Alength"]
    avg_g_A = st.session_state["avg_g_A"]
    avg_uncert_A = st.session_state["avg_uncert_A"]
    if Alength:
        st.write(f"Average g: {avg_g_A:0.2f} m/s^2")
        st.write(f"Average uncertainty: {avg_uncert_A:0.2f}")
        fig, ax = plt.subplots()
        ax.set_ylim(6,14)
        ax.errorbar(df_angles.index, df_angles["Calculated 'g' (m/s^2)"], yerr=df_angles["Calculated uncertainty"], fmt='o', capsize=5)
        ax.set_xlabel("Index")
        ax.set_ylabel("Calculated 'g' (m/s^2)")
        st.pyplot(fig)
    else:
        st.warning("Pendulum length not given")
else:
    st.warning("Pendulum dataframe not defined")

st.markdown("### Changing Lengths")
if "df_lengths" and "Langle" and "avg_g_L" and "avg_uncert_L" in st.session_state:
    df_lengths = st.session_state["df_lengths"]
    Langle = st.session_state["Langle"]
    avg_g_L = st.session_state["avg_g_L"]
    avg_uncert_L = st.session_state["avg_uncert_L"]
    if Langle:
        st.write(f"Average g: {avg_g_L:0.2f} m/s^2")
        st.write(f"Average uncertainty: {avg_uncert_L:0.2f}")
        fig, ax = plt.subplots()
        ax.set_ylim(7,18)
        ax.errorbar(df_lengths.index, df_lengths["Calculated 'g' (m/s^2)"], yerr=df_lengths["Calculated uncertainty"], fmt='o', capsize=5)
        ax.set_xlabel("Index")
        ax.set_ylabel("Calculated 'g' (m/s^2)")
        st.pyplot(fig)
    else:
        st.warning("Pendulum angle not given")
else:
    st.warning("Pendulum dataframe not given")

st.markdown("## Freefall Experiment")
st.markdown("### Stopwatch")
if "df_stopwatch" and "avg_g_S" and "avg_uncert_S" in st.session_state:
    df_stopwatch = st.session_state["df_stopwatch"]
    avg_g_S = st.session_state["avg_g_S"]
    avg_uncert_S = st.session_state["avg_uncert_S"]
    st.write(f"Average g: {avg_g_S:0.2f} (m/s^2)")
    st.write(f"Average uncertainty: {avg_uncert_S:0.2f}")
    fig, ax = plt.subplots()
    ax.set_ylim(2,13)
    ax.errorbar(df_stopwatch.index, df_stopwatch["Calculated 'g' (m/s^2)"], yerr=df_stopwatch["Calculated uncertainty"], fmt='o', capsize=5)
    ax.set_xlabel("Index")
    ax.set_ylabel("Calculated 'g' (m/s^2)")
    st.pyplot(fig)
else: 
    st.warning("Freefall with stopwatch dataframe not given")

st.markdown("### Photogates")
if "df_photogate" and "avg_g_P" and "avg_uncert_P" in st.session_state:
    df_photogate = st.session_state["df_photogate"]
    avg_g_P = st.session_state["avg_g_P"]
    avg_uncert_P = st.session_state["avg_uncert_P"]
    st.write(f"Average 'g': {avg_g_P:0.2f} (m/s^2)")
    st.write(f"Average uncertainty: {avg_uncert_P:0.2f}")
    fig, ax = plt.subplots()
    ax.set_ylim(9,20)
    ax.errorbar(df_photogate.index, df_photogate["Calculated 'g' (m/s^2)"], yerr=df_photogate["Calculated uncertainty"], fmt='o', capsize=5)
    ax.set_xlabel("Index")
    ax.set_ylabel("Calculated 'g' (m/s^2)")
    st.pyplot(fig)
else: 
    st.warning("Freefall with photogates dataframe not given")

st.markdown("## Atwood Machine")
if "df_machine" and "distance" and "avg_g_M" and "avg_uncert_M" in st.session_state:
    df_machine = st.session_state["df_machine"]
    dist = st.session_state["distance"]
    avg_g_M = st.session_state["avg_g_M"]
    avg_uncert_M = st.session_state["avg_uncert_M"]
    if dist:
        st.write(f"Average 'g': {avg_g_M:0.2f} (m/s^2)")
        st.write(f"Average uncertainty: {avg_uncert_M:0.2f}")
        fig, ax = plt.subplots()
        ax.set_ylim(7,24)
        ax.errorbar(df_machine.index, df_machine["Calculated 'g' (m/s^2)"], yerr=df_machine["Calculated uncertainty"], fmt='o', capsize=5)
        ax.set_xlabel("Idex")
        ax.set_ylabel("Calculated 'g' (m/s^2)")
        st.pyplot(fig)
    else:
        st.warning("Distance not given")
else:
    st.warning("Atwood Machine dataframe not given")

st.markdown("## Incline Experiment")
if "df_incline" and "Ilength" and "avg_g_I" and "avg_uncert_I" in st.session_state:
    df_incline = st.session_state["df_incline"]
    Ilength = st.session_state["Ilength"]
    avg_g_I = st.session_state["avg_g_I"]
    avg_uncert_I = st.session_state["avg_uncert_I"]
    if Ilength:
        st.write(f"Average g: {avg_g_I:0.2f} (m/s^2)")
        st.write(f"Average uncertainty: {avg_uncert_I:0.2f}")
        fig, ax = plt.subplots()
        ax.set_ylim(8,16)
        ax.errorbar(df_incline.index, df_incline["Calculated 'g' (m/s^2)"], yerr=df_incline["Calculated uncertainty"], fmt='o', capsize=5)
        ax.set_xlabel("Idex")
        ax.set_ylabel("Calculated 'g' (m/s^2)")
        st.pyplot(fig)
    else:
        st.warning("Length not given")
else:
    st.warning("Incline dataframe not given")

st.markdown("## Final Comparison")
if "df_angles" and "Alength"  and "avg_g_A" and "avg_uncert_A" and "df_lengths" and "Langle" and "avg_g_L" and "avg_uncert_L" and "df_stopwatch" and "avg_g_S" and "avg_uncert_S" and "df_photogate" and "avg_g_P" and "avg_uncert_P" and "df_machine" and "distance" and "avg_g_M" and "avg_uncert_M" and "df_incline" and "Ilength" and "avg_g_I" and "avg_uncert_I" in st.session_state:
    df_all = pd.DataFrame({
        "Experiment": ["Pendulum - Angles", "Pendulum - Lengths", "Freefall - Stopwatch", "Freefall - Photogate", "Atwood Machine", "Incline"],
        "Average 'g' (m/s^2)": [avg_g_A, avg_g_L, avg_g_S, avg_g_P, avg_g_M, avg_g_I],
        "Average Uncertainty": [avg_uncert_A,avg_uncert_L,avg_uncert_S, avg_uncert_P,avg_uncert_M,avg_uncert_I]
    })
    fig, ax = plt.subplots()
    ax.set_ylim(5,17)
    ax.errorbar(np.arange(len(df_all)), df_all["Average 'g' (m/s^2)"], yerr=df_all["Average Uncertainty"], fmt='o', capsize=5)
    ax.set_xticks(np.arange(len(df_all)))
    ax.set_xticklabels(df_all["Experiment"], rotation=45,ha='right')
    ax.set_xlabel("Experiment")
    ax.set_ylabel("Average calculated 'g' value (m/s^2)")
    ax.set_title("Comparison of Experimental 'g' values")
    st.pyplot(fig)
    best_uncert_indx = df_all["Average Uncertainty"].idxmin()
    best_uncert_exp = df_all.loc[best_uncert_indx, "Experiment"]
    st.write(f"Experiment with smallest uncertainty: {best_uncert_exp}")
    df_all["Inaccuracy"] = abs(df_all["Average 'g' (m/s^2)"].values - 9.8)
    best_accuracy_idx = df_all["Inaccuracy"].idxmin()
    best_accuracy_exp = df_all.loc[best_accuracy_idx, "Experiment"]
    st.write(f"Experiment closest to real 'g': {best_accuracy_exp}")
else:
    st.warning("Not all data has been entered.")