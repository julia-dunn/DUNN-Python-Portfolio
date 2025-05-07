# imports required dictionaries for all pages
import streamlit as st
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

# uses st. to apply markdown sytnax to streamlit platform
st.title("Results!")
st.write("Here is where you can access the analysis of your data! ")

st.markdown("## Pendulum Experiment")
st.markdown("### Changing Angles")
if "df_angles" and "Alength"  and "avg_g_A" and "avg_uncert_A" in st.session_state: # can only run following calculations if values have been entered on other page, if then loop avoids error
    df_angles = st.session_state["df_angles"] # defnes variable from session_state
    Alength = st.session_state["Alength"] # defines variable from session_state
    avg_g_A = st.session_state["avg_g_A"] # defines variable from session_state
    avg_uncert_A = st.session_state["avg_uncert_A"] # defines variable from session_state
    if Alength: # need variable to have been entered, if not entered if then loop avoids error
        st.write(f"Average g: {avg_g_A:0.2f} m/s^2") # return average g value for pendulum 1
        st.write(f"Average uncertainty: {avg_uncert_A:0.2f}") # returns average uncertainty for pendulum 1
        fig, ax = plt.subplots() # generates graph of g values from each trial with uncertainty, same code as page 2_pendulum
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
if "df_lengths" and "Langle" and "avg_g_L" and "avg_uncert_L" in st.session_state:  # can only run following calculations if values have been entered on other page, if then loop avoids error
    df_lengths = st.session_state["df_lengths"] # defnes variable from session_state
    Langle = st.session_state["Langle"] # defnes variable from session_state
    avg_g_L = st.session_state["avg_g_L"] # defnes variable from session_state
    avg_uncert_L = st.session_state["avg_uncert_L"] # defnes variable from session_state
    if Langle: # need variable to have been entered, if not entered if then loop avoids error
        st.write(f"Average g: {avg_g_L:0.2f} m/s^2") # returns average g value for pendulum 2
        st.write(f"Average uncertainty: {avg_uncert_L:0.2f}") # average uncertainty for pendulum 2
        fig, ax = plt.subplots() # generates graph of g values form each trial with uncertainty, same code as page 2_pendulum
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
if "df_stopwatch" and "avg_g_S" and "avg_uncert_S" in st.session_state: # can only run following calculations if values have been entered on other page, if then loop avoids error
    df_stopwatch = st.session_state["df_stopwatch"] # defnes variable from session_state
    avg_g_S = st.session_state["avg_g_S"] # defnes variable from session_state
    avg_uncert_S = st.session_state["avg_uncert_S"] # defnes variable from session_state
    st.write(f"Average g: {avg_g_S:0.2f} (m/s^2)") # returns average g for freefall 1
    st.write(f"Average uncertainty: {avg_uncert_S:0.2f}") # returns average uncertainty for freefall 1
    fig, ax = plt.subplots() # generates graph of g values form each trial with uncertainty, same code as page 3_freefall
    ax.set_ylim(2,13)
    ax.errorbar(df_stopwatch.index, df_stopwatch["Calculated 'g' (m/s^2)"], yerr=df_stopwatch["Calculated uncertainty"], fmt='o', capsize=5)
    ax.set_xlabel("Index")
    ax.set_ylabel("Calculated 'g' (m/s^2)")
    st.pyplot(fig)
else: 
    st.warning("Freefall with stopwatch dataframe not given")

st.markdown("### Photogates") 
if "df_photogate" and "avg_g_P" and "avg_uncert_P" in st.session_state:  # can only run following calculations if values have been entered on other page, if then loop avoids error
    df_photogate = st.session_state["df_photogate"]  # defnes variable from session_state
    avg_g_P = st.session_state["avg_g_P"]  # defnes variable from session_state
    avg_uncert_P = st.session_state["avg_uncert_P"]  # defnes variable from session_state
    st.write(f"Average 'g': {avg_g_P:0.2f} (m/s^2)") # returns average g for freefall 2
    st.write(f"Average uncertainty: {avg_uncert_P:0.2f}") # returns average uncertainty for freefall 2
    fig, ax = plt.subplots() # generates graph of g values form each trial with uncertainty, same code as page 3_freefall
    ax.set_ylim(9,20)
    ax.errorbar(df_photogate.index, df_photogate["Calculated 'g' (m/s^2)"], yerr=df_photogate["Calculated uncertainty"], fmt='o', capsize=5)
    ax.set_xlabel("Index")
    ax.set_ylabel("Calculated 'g' (m/s^2)")
    st.pyplot(fig)
else: 
    st.warning("Freefall with photogates dataframe not given")

st.markdown("## Atwood Machine")
if "df_machine" and "distance" and "avg_g_M" and "avg_uncert_M" in st.session_state: # can only run following calculations if values have been entered on other page, if then loop avoids error
    df_machine = st.session_state["df_machine"] # defnes variable from session_state
    dist = st.session_state["distance"] # defnes variable from session_state
    avg_g_M = st.session_state["avg_g_M"] # defnes variable from session_state
    avg_uncert_M = st.session_state["avg_uncert_M"] # defnes variable from session_state
    if dist: # need variable to have been entered, if not entered if then loop avoids error
        st.write(f"Average 'g': {avg_g_M:0.2f} (m/s^2)") # returns average g for atwood machine
        st.write(f"Average uncertainty: {avg_uncert_M:0.2f}") # returns average uncertainty for atwood machine
        fig, ax = plt.subplots() # generates graph of g values form each trial with uncertainty, same code as page 4_AtwoodMachine
        ax.set_ylim(7,24)
        ax.errorbar(df_machine.index, df_machine["Calculated 'g' (m/s^2)"], yerr=df_machine["Calculated uncertainty"], fmt='o', capsize=5)
        ax.set_xlabel("Index")
        ax.set_ylabel("Calculated 'g' (m/s^2)")
        st.pyplot(fig)
    else:
        st.warning("Distance not given")
else:
    st.warning("Atwood Machine dataframe not given")

st.markdown("## Incline Experiment")
if "df_incline" and "Ilength" and "avg_g_I" and "avg_uncert_I" in st.session_state: # can only run following calculations if values have been entered on other page, if then loop avoids error
    df_incline = st.session_state["df_incline"] # defnes variable from session_state
    Ilength = st.session_state["Ilength"] # defnes variable from session_state
    avg_g_I = st.session_state["avg_g_I"] # defnes variable from session_state
    avg_uncert_I = st.session_state["avg_uncert_I"] # defnes variable from session_state
    if Ilength:  # need variable to have been entered, if not entered if then loop avoids error
        st.write(f"Average g: {avg_g_I:0.2f} (m/s^2)") # returns average g for incline
        st.write(f"Average uncertainty: {avg_uncert_I:0.2f}") # returns average uncertainty for incline
        fig, ax = plt.subplots() # generates graph of g values form each trial with uncertainty, same code as page 5_Incline
        ax.set_ylim(8,16)
        ax.errorbar(df_incline.index, df_incline["Calculated 'g' (m/s^2)"], yerr=df_incline["Calculated uncertainty"], fmt='o', capsize=5)
        ax.set_xlabel("Index")
        ax.set_ylabel("Calculated 'g' (m/s^2)")
        st.pyplot(fig)
    else:
        st.warning("Length not given")
else:
    st.warning("Incline dataframe not given")

st.markdown("## Final Comparison")
if "df_angles" and "Alength"  and "avg_g_A" and "avg_uncert_A" and "df_lengths" and "Langle" and "avg_g_L" and "avg_uncert_L" and "df_stopwatch" and "avg_g_S" and "avg_uncert_S" and "df_photogate" and "avg_g_P" and "avg_uncert_P" and "df_machine" and "distance" and "avg_g_M" and "avg_uncert_M" and "df_incline" and "Ilength" and "avg_g_I" and "avg_uncert_I" in st.session_state:  # can only run following calculations if values have been entered on other page, if then loop avoids error
    df_all = pd.DataFrame({ # generates dataframe from average values of all experiments
        "Experiment": ["Pendulum - Angles", "Pendulum - Lengths", "Freefall - Stopwatch", "Freefall - Photogate", "Atwood Machine", "Incline"],
        "Average 'g' (m/s^2)": [avg_g_A, avg_g_L, avg_g_S, avg_g_P, avg_g_M, avg_g_I],
        "Average Uncertainty": [avg_uncert_A,avg_uncert_L,avg_uncert_S, avg_uncert_P,avg_uncert_M,avg_uncert_I]
    })
    fig, ax = plt.subplots() # creates empty plot for matplotlib plot
    ax.set_ylim(5,17) # sets reasonable limits for average g of all experiments
    ax.errorbar(np.arange(len(df_all)), df_all["Average 'g' (m/s^2)"], yerr=df_all["Average Uncertainty"], fmt='o', capsize=5)  # uses .errorbar function to visualize calculated g on y axis, index on x axis, and error bars of specific size
    ax.set_xticks(np.arange(len(df_all))) # creates ticks on x axis
    ax.set_xticklabels(df_all["Experiment"], rotation=45,ha='right') # labels ticks on x axis with each experiment name
    ax.set_xlabel("Experiment")
    ax.set_ylabel("Average calculated 'g' value (m/s^2)")
    ax.set_title("Comparison of Experimental 'g' values")
    st.pyplot(fig) # returns visualization in streamlit
    best_uncert_indx = df_all["Average Uncertainty"].idxmin() # determines index of minimum avg uncertainty
    best_uncert_exp = df_all.loc[best_uncert_indx, "Experiment"] # determines experiment name of minimum avg uncertainty 
    st.write(f"Experiment with smallest uncertainty: {best_uncert_exp}") # returns experiment with minimum avg uncertainty
    df_all["Inaccuracy"] = abs(df_all["Average 'g' (m/s^2)"].values - 9.8) # defines inaccuracy as difference between avg and 9.8
    best_accuracy_idx = df_all["Inaccuracy"].idxmin() # determines index with minimum inaccuracy
    best_accuracy_exp = df_all.loc[best_accuracy_idx, "Experiment"] # determines experiment name with minimum inacuraccy
    st.write(f"Experiment closest to real 'g': {best_accuracy_exp}") # returns experiment with minimum inaccuracy
else:
    st.warning("Not all data has been entered.")