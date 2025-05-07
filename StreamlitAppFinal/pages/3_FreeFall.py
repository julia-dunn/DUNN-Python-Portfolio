# imports required dictionaries for all pages
import streamlit as st
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

# uses st. to apply markdown syntax to streamlit platform
st.title("The Freefall Experiment")
st.write("Here is where you can input your data for the free fall experiment, both when using a stopwatch and with photogates.")
st.markdown(" ### Stopwatch:")
n = st.number_input("Number of heights you dropped the ball from:", value=1) # defines variable using number input 

# creates empty lists that are appended in for loop with number_inputs, for input into dataframe
Fheights = []
Strial_1 = []
Strial_2 = []
Strial_3 = []
Strial_4 = []
Strial_5 = []

# for loop so that there are only number of entries for the number inputted with "n"
for i in range(n):
    st.markdown(f" #### Configuration {i+1}")
    Fh = st.number_input(f"Height {i+1}", value=None, placeholder="(meters)", key=f"Fh_{i}") # defines variable with number input, uses unique key to clarify between each iteration
    c1, c2, c3, c4, c5 = st.columns(5) # defines number of columns for streamlit to format number input placement
    St1 = c1.number_input(f"Trial 1", value=None, placeholder="time(s)", key=f"St1_{i}") # defines variable with number input in first column, uses unique key to clarify between each iteration
    St2 = c2.number_input(f"Trial 2", value=None, placeholder="time(s)", key=f"St2_{i}") # defines variable with number input in second column, uses unique key to clarify between each iteration
    St3 = c3.number_input(f"Trial 3", value=None, placeholder="time(s)", key=f"St3_{i}") # defines variable with number input in third column, uses unique key to clarify between each iteration
    St4 = c4.number_input(f"Trial 4", value=None, placeholder="time(s)", key=f"St4_{i}") # defines variable with number input in fourth column, uses unique key to clarify between each iteration
    St5 = c5.number_input(f"Trial 5", value=None, placeholder="time(s)", key=f"St5_{i}") # defines variable with number input in fifth column, uses unique key to clarify between each iteration

    # appends each of the above inputs to empty lists, inside for loop
    Fheights.append(Fh)
    Strial_1.append(St1)
    Strial_2.append(St2)
    Strial_3.append(St3)
    Strial_4.append(St4)
    Strial_5.append(St5)
 # creates pandas dataframe from lists
df_stopwatch = pd.DataFrame({
    "Height (m)": Fheights,
    "Trial 1 (s)": Strial_1,
    "Trial 2 (s)": Strial_2,
    "Trial 3 (s)": Strial_3,
    "Trial 4 (s)": Strial_4,
    "Trial 5 (s)": Strial_5
})
st.markdown("#### Entered Data")
columns3 = df_stopwatch.columns[1:5] # defines columns to calculate average
df_stopwatch["Average Time (s)"] = df_stopwatch[columns3].mean(axis=1) # calculates mean of specific columns in dataframe and appends to dataframe new column
df_stopwatch["Calculated 'g' (m/s^2)"] = 2 * df_stopwatch["Height (m)"]/(df_stopwatch["Average Time (s)"]**2) # appends calculated g value to dataframe
df_stopwatch["Calculated uncertainty"] = (((-2 * 0.0005 * df_stopwatch["Height (m)"]/df_stopwatch["Average Time (s)"]**3)**2)+(0.02/df_stopwatch["Average Time (s)"]**2)**2)**0.5 # appends calculated uncertainty value to dataframe
avg_g_S = df_stopwatch["Calculated 'g' (m/s^2)"].mean() # defines avg g value for future returns
avg_uncert_S = df_stopwatch["Calculated uncertainty"].mean() # defines avg uncertainty for future returns
st.dataframe(df_stopwatch) # returns dataframe in streamlit for user readibility
st.write(f"Average g: {avg_g_S:0.2f} (m/s^2)") # uses f' to return avg g, :0.2f indicates 2 decimal places
st.write(f"Average uncertainty: {avg_uncert_S:0.2f}") # uses f' to return avg uncetainty, :0.2f indicates 2 decimal places
fig, ax = plt.subplots() # creates empty fig, ax for matplotlib visualization
ax.set_ylim(1,15) # sets reasonable limits for calculated 'g' (for this experiment)
ax.errorbar(df_stopwatch.index, df_stopwatch["Calculated 'g' (m/s^2)"], yerr=df_stopwatch["Calculated uncertainty"], fmt='o', capsize=5) # uses .errorbar function to visualize calculated g on y axis, index on x axis, and error bars of specific size
ax.set_xlabel("Index") 
ax.set_ylabel("Calculated 'g' (m/s^2)")
st.pyplot(fig) # returns visualization on streamlit for users

st.session_state["df_stopwatch"] = df_stopwatch # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function
st.session_state["avg_g_S"] = avg_g_S # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function
st.session_state["avg_uncert_S"] = avg_uncert_S # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function

# second part of experiment, essentially repeated code from above
st.markdown(" ### Photogates:")
m = st.number_input("Number of distances between photogates:", value=1) # defines variable using number input 

# creates empty lists
Fdistances = []
Ptrial_1 = []
Ptrial_2 = []
Ptrial_3 = []
Ptrial_4 = []
Ptrial_5 = []

# for loop to have number of entries = m
for i in range(m):
    st.markdown(f" #### Configuration {i+1}")
    Fd = st.number_input(f"Distance {i+1}", value=None, placeholder="(meters)", key=f"Fd_{i}") # defines variable with number input, uses unique key to clarify between each iteration
    c1, c2, c3, c4, c5 = st.columns(5) # defines columns for streamlit to format input placement
    Pt1 = c1.number_input(f"Trial 1", value=None, placeholder="time(s)", key=f"Pt1_{i}") # defines variable with number input in first column, uses unique key to clarify between each iteration
    Pt2 = c2.number_input(f"Trial 2", value=None, placeholder="time(s)", key=f"Pt2_{i}") # defines variable with number input in second column, uses unique key to clarify between each iteration
    Pt3 = c3.number_input(f"Trial 3", value=None, placeholder="time(s)", key=f"Pt3_{i}") # defines variable with number input in third column, uses unique key to clarify between each iteration
    Pt4 = c4.number_input(f"Trial 4", value=None, placeholder="time(s)", key=f"Pt4_{i}") # defines variable with number input in fourth column, uses unique key to clarify between each iteration
    Pt5 = c5.number_input(f"Trial 5", value=None, placeholder="time(s)", key=f"Pt5_{i}") # defines variable with number input in fifth column, uses unique key to clarify between each iteration

    # appends each of the above inputs to empty lists, inside for loop
    Fdistances.append(Fd)
    Ptrial_1.append(Pt1)
    Ptrial_2.append(Pt2)
    Ptrial_3.append(Pt3)
    Ptrial_4.append(Pt4)
    Ptrial_5.append(Pt5)
 # creates pandas dataframe from lists
df_photogate = pd.DataFrame({
    "Distance (m)": Fdistances,
    "Trial 1 (s)": Ptrial_1,
    "Trial 2 (s)": Ptrial_2,
    "Trial 3 (s)": Ptrial_3,
    "Trial 4 (s)": Ptrial_4,
    "Trial 5 (s)": Ptrial_5
})

st.markdown("#### Entered Data:")
columns4 = df_photogate.columns[1:5] # defines columns to calculate the aberahe
df_photogate["Average Time (s)"] = df_photogate[columns4].mean(axis=1) #calculates mean of specific columnsin dataframe, appends to DF
df_photogate["Calculated 'g' (m/s^2)"] = 2 * (df_photogate["Distance (m)"])/(df_photogate['Average Time (s)']**2) # calculates avg g and appends to DF
df_photogate['Calculated uncertainty'] = (((-2 * 0.0005 * df_photogate["Distance (m)"]/(df_photogate["Average Time (s)"])**3)**2)+(0.02/(df_photogate["Average Time (s)"])**2)**2)**0.5 # calculates avg uncertainty and appends to DF
st.dataframe(df_photogate) # returns dataframe in streamlit 
avg_g_P = df_photogate["Calculated 'g' (m/s^2)"].mean() # defines avg g value for future returns
avg_uncert_P = df_photogate["Calculated uncertainty"].mean() # defines avg uncertainty value for future returns
st.write(f"Average 'g': {avg_g_P:0.2f} (m/s^2)")  # uses f' to return average g, :0.2f indicates only 2 decimal places
st.write(f"Average uncertainty: {avg_uncert_P:0.2f}")  # uses f' to return average uncertainty, :0.2f indicates only 2 decimal places

fig, ax = plt.subplots() # creates empty fig, ax for matplotlib plot
ax.set_ylim(9,20) # sets reasonable limits for calculated g, for this experiment
ax.errorbar(df_photogate.index, df_photogate["Calculated 'g' (m/s^2)"], yerr=df_photogate["Calculated uncertainty"], fmt='o', capsize=5) # uses .errorbar function to visualize calculated g on y axis, index on x axis, and error bars of specific size
ax.set_xlabel("Index")
ax.set_ylabel("Calculated 'g' (m/s^2)")
st.pyplot(fig) # returns visualization on streamlit

st.session_state["df_photogate"] = df_photogate # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function
st.session_state["avg_g_P"] = avg_g_P # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function
st.session_state["avg_uncert_P"] = avg_uncert_P # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function