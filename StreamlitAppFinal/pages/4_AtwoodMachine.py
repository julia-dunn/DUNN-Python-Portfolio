# imports required dictionaries for all pages
import streamlit as st
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

# uses st. to apply markdown syntax to streamlit platform
st.title("The Atwood Machine Experiment")
st.write("Here is where you can input your data for the atwood machine experiment. How many mass configurations did you use?")
n = st.number_input("Number of mass configurations:", value=1) # defines variable using number_input
dist = st.number_input("Distance masses were allowed to fall:", value=None, placeholder="(meters)") # defines variable using number input on page, originally no value, when empty reads "(meters)"
st.session_state["distance"] = dist  # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function

# creates empty lists that are appended in for loop with number_inputs
mass1 = []
mass2 = []
Mtrial_1 = []
Mtrial_2 = []
Mtrial_3 = []
Mtrial_4 = []
Mtrial_5 = []

# for loop so that there are only the number of entries for the number inputted with "n"
for i in range(n):
    st.markdown(f" #### Configuration {i+1}:")
    c1, c2 = st.columns(2) # defines columns for streamlit to format input placement
    m1 = c1.number_input(f"Mass 1", value=None, placeholder="(kg)", key=f"m1_{i}") # defines variable with number input in first column, uses unique key to clarify between each iteration
    m2 = c2.number_input(f"Mass 2", value=None, placeholder="(kg)", key=f"m2_{i}") # defines variable with number input in second column, uses unique key to clarify between each iteration
    c1, c2, c3, c4, c5 = st.columns(5) # defines new columns for streamlit to format input placement
    Mt1 = c1.number_input(f"Trial 1", value=None, placeholder="time(s)", key=f"Mt1_{i}") # defines variable with number input in first column, uses unique key to clarify between each iteration
    Mt2 = c2.number_input(f"Trial 2", value=None, placeholder="time(s)", key=f"Mt2_{i}") # defines variable with number input in second column, uses unique key to clarify between each iteration
    Mt3 = c3.number_input(f"Trial 3", value=None, placeholder="time(s)", key=f"Mt3_{i}") # defines variable with number input in third column, uses unique key to clarify between each iteration
    Mt4 = c4.number_input(f"Trial 4", value=None, placeholder="time(s)", key=f"Mt4,{i}") # defines variable with number input in fourth column, uses unique key to clarify between each iteration
    Mt5 = c5.number_input(f"Trial 5", value=None, placeholder="time(s)", key=f"Mt5_{i}") # defines variable with number input in fifth column, uses unique key to clarify between each iteration

    # appends each of the above inpputs to empty lists, inside for loop
    mass1.append(m1)
    mass2.append(m2)
    Mtrial_1.append(Mt1)
    Mtrial_2.append(Mt2)
    Mtrial_3.append(Mt3)
    Mtrial_4.append(Mt4)
    Mtrial_5.append(Mt5)

df_machine = pd.DataFrame({ # creates pandas dataframe from lists
    "Mass 1 (kg)": mass1,
    "Mass 2 (kg)": mass2,
    "Trial 1 (s)": Mtrial_1,
    "Trial 2 (s)": Mtrial_2,
    "Trial 3 (s)": Mtrial_3,
    "Trial 4 (s)": Mtrial_4,
    "Trial 5 (s)": Mtrial_5
})

st.markdown("#### Data Entered:")
columns5 = df_machine.columns[1:5] # defines columns to calculate average
df_machine["Average Time (s)"] = df_machine[columns5].mean(axis=1) # calculates mean and appends to DF as new column
st.dataframe(df_machine) # returns dataframe in streamlit

if dist: # need if then because before dist is inputted the following calculations would return an error 
    df_machine["Calculated 'g' (m/s^2)"] = 2 * dist * (df_machine["Mass 1 (kg)"] + df_machine["Mass 2 (kg)"])/(df_machine["Average Time (s)"]**2 * (df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"])) # appends calculated g value to dataframe
    df_machine["Calculated uncertainty"] = (((0.0004*(df_machine["Mass 1 (kg)"] + df_machine["Mass 2 (kg)"]))/(df_machine["Average Time (s)"]**2 * (df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"])))**2 + ((0.001*(df_machine["Mass 1 (kg)"] + df_machine["Mass 2 (kg)"]))/(df_machine["Average Time (s)"]**2) * (df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"]))**2 + 2*((0.000774 * df_machine["Average Time (s)"]**2 * ((df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"]) - (df_machine["Mass 1 (kg)"] + df_machine["Mass 2 (kg)"])))/((df_machine["Average Time (s)"]**2 * (df_machine["Mass 1 (kg)"] - df_machine["Mass 2 (kg)"]))**2))**2)**0.5  # appends calculated uncertainty value to dataframe
    avg_g_M = df_machine["Calculated 'g' (m/s^2)"].mean() # defines avg g value for future returns, 
    avg_uncert_M = df_machine["Calculated uncertainty"].mean() # defines avg uncertainty for future returns
    st.write(f"Average 'g': {avg_g_M:0.2f} (m/s^2)") # uses f' to return average 'g', :0.2f indicates only 2 decimal places
    st.write(f"Average uncertainty: {avg_uncert_M:0.2f}") # uses f' to return average uncertainty, :0.2f indicates only 2 decimal places
    fig, ax = plt.subplots() # creates empty plot for matplotlib plot
    ax.set_ylim(8,25) # sets reasonable limits for calculated g (for this experiment)
    ax.errorbar(df_machine.index, df_machine["Calculated 'g' (m/s^2)"], yerr=df_machine["Calculated uncertainty"], fmt='o', capsize=5) # uses .errorbar function to visualize calculated g on y axis, index on x axis, and error bars of specific size
    ax.set_xlabel("Index")
    ax.set_ylabel("Calculated 'g' (m/s^2)")
    st.pyplot(fig) # returns visualization on streamlit for user
    st.session_state["avg_g_M"] = avg_g_M # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function
    st.session_state["avg_uncert_M"] = avg_uncert_M # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function

st.session_state["df_machine"] = df_machine # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function