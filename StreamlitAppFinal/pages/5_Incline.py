# imports required dictionaries for all pages
import streamlit as st
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

# uses st. to apply markdown syntax to streamlit platform
st.title("The Incline Experiment")
st.write("Here you can input your data for the incline experiment. First, input the standard dimensions for your setup.")
Ilength = st.number_input("Length of track:", value=None, placeholder="(meters)") # defines variable using number_input
st.session_state["Ilength"] = Ilength # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function
st.write("You must also input the number of configurations you tested, that is the different heights you set the track to.")
n = st.number_input("Number of heights:", value=1) # defines variable using number_input

# creates empty lists that are appended in for loop with number_inputs
Iheights = []
Idistances = []
Itrial_1 = []
Itrial_2 = []
Itrial_3 = []
Itrial_4 = []
Itrial_5 = []

# for loop so that there are only the number of entries for the number inputed with "n"
for i in range(n):
    st.markdown(f" #### Configuration {i+1}")
    Ih = st.number_input(f"Height of track", value=None, placeholder="(meters)", key=f"Ih_{i}")  # defines variable with number input, uses unique key to clarify between each iteration
    x = st.number_input(f"Distance traveled along track", value=None, placeholder="(meters)", key=f"x_{i}")  # defines variable with number input, uses unique key to clarify between each iteration
    c1, c2, c3, c4, c5 = st.columns(5) # defines columns for streamlit to format input placement
    It1 = c1.number_input(f"Trial 1", value=None, placeholder="time(s)", key=f"It1_{i}")  # defines variable with number input in first column, uses unique key to clarify between each iteration
    It2 = c2.number_input(f"Trial 2", value=None, placeholder="time(s)", key=f"It2_{i}")  # defines variable with number input in second column, uses unique key to clarify between each iteration
    It3 = c3.number_input(f"Trial 3", value=None, placeholder="time(s)", key=f"It3_{i}")  # defines variable with number input in third column, uses unique key to clarify between each iteration
    It4 = c4.number_input(f"Trial 4", value=None, placeholder="time(s)", key=f"It4_{i}")  # defines variable with number input in fourth column, uses unique key to clarify between each iteration
    It5 = c5.number_input(f"Trial 5", value=None, placeholder="time(s)", key=f"It5_{i}")  # defines variable with number input in fifth column, uses unique key to clarify between each iteration

    # appends each of the above inpputs to empty lists, inside for loop
    Iheights.append(Ih)
    Idistances.append(x)
    Itrial_1.append(It1)
    Itrial_2.append(It2)
    Itrial_3.append(It3)
    Itrial_4.append(It4)
    Itrial_5.append(It5)
 # creates pandas dataframe from lists
df_incline = pd.DataFrame({
    "Height (m)": Iheights,
    "Distance x (m)": Idistances,
    "Trial 1 (s)": Itrial_1,
    "Trial 2 (s)": Itrial_2,
    "Trial 3 (s)": Itrial_3,
    "Trial 4 (s)": Itrial_4,
    "Trial 5 (s)": Itrial_5
})

st.markdown("#### Entered Data")
columns6 = df_incline.columns[1:5] # defines columns to calculate average
df_incline["Average Time (s)"] = df_incline[columns6].mean(axis=1)  # calculates mean and appends to DF as new column
st.dataframe(df_incline) # returns dataframe in streamlit

if Ilength: # need if then because before Ilength is inputted the following calculations would return an error 
    df_incline["Angle (radians)"] = np.arcsin(df_incline["Height (m)"]/Ilength) # appends angle value to dataframe from measuremets
    df_incline["Calculated 'g' (m/s^2)"] = 14 * df_incline["Distance x (m)"]/(5 * df_incline["Average Time (s)"]**2 * np.sin(df_incline["Angle (radians)"])) # appends calculated value of g to dataframe
    df_incline["Calculated uncertainty"] = ((14 * 0.0005 / (5 * df_incline["Average Time (s)"]**2 * np.sin(df_incline["Angle (radians)"])))**2 + ((0.28 * df_incline["Distance x (m)"])/(5 * df_incline["Average Time (s)"]**2 * np.sin(df_incline["Angle (radians)"])))**2 + ((14 * df_incline["Distance x (m)"] * np.cos(df_incline["Angle (radians)"]) * (1/np.sin(df_incline["Angle (radians)"])) * (2*(0.0005/(1 + (df_incline["Height (m)"]/Ilength)**2))**2))/(5 * (df_incline["Average Time (s)"]**2)))**2)**0.5 # appends calculated value of uncertainty to dataframe
    avg_g_I = df_incline["Calculated 'g' (m/s^2)"].mean() # defines avg g value for future returns
    avg_uncert_I = df_incline["Calculated uncertainty"].mean() # defines avg uncertainty for future returns
    st.write(f"Average g: {avg_g_I:0.2f} (m/s^2)") # uses f' to return average 'g', :0.2f indicates only 2 decimal places
    fig, ax = plt.subplots() # uses f' to return average 'uncertainty', :0.2f indicates only 2 decimal places
    ax.set_ylim(5,18) # sets reasonable limits for calculated g, for this experiment
    ax.errorbar(df_incline.index, df_incline["Calculated 'g' (m/s^2)"], yerr=df_incline["Calculated uncertainty"], fmt='o', capsize=5) # uses .errorbar function to visualize calculated g on y axis, index on x axis, and error bars of specific size
    ax.set_xlabel("Idex")
    ax.set_ylabel("Calculated 'g' (m/s^2)")
    st.pyplot(fig) # returns visualization on streamlit
    st.session_state["avg_g_I"] = avg_g_I # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function
    st.session_state["avg_uncert_I"] = avg_uncert_I # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function

st.session_state["df_incline"] = df_incline # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function