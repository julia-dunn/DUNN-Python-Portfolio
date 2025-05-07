# imports required dictionaries for all pages
import streamlit as st
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

# uses st. to apply markdown syntax to streamlit platform
st.title("The Pendulum Experiment!")
st.write("Here is where you can imput your data from the pendulum experiment")
st.markdown(" ### Changing Angle")
st.write("Here, input the length of your pendulum, the different angles of elevation you used, and the time it took to complete 5 oscillations.")
Alength = st.number_input("Length of pendulum [m]", value=None, placeholder="(meters)") # defines variable using number input on page, originally no value, when empty reads "(meters)"
st.session_state["Alength"] = Alength # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function
n = st.number_input("Number of Angles:", value=1) # defines variable using number input 

# creates empty lists that are appended in for loop with number_inputs, for input into dataframe
angles = []
Atrial_1 = []
Atrial_2 = []
Atrial_3 = []
c1, c2, c3, c4 = st.columns(4) # defines columns for streamlit to format input placement

# for loop so that there are only the number of entries for the number inputted with "n"
for i in range(n):
    angle = c1.number_input(f"Angle of Elevation {i+1}", value=None, placeholder="(degrees)", key=f"A_{i}") # defines variable with number input in first column, uses unique key to clarify between each iteration
    At1 = c2.number_input(f"Trial 1", value=None, placeholder="Time (s)", key=f"At1_{i}") # defines variable with number input in second column, uses unique key to clarify between each iteration
    At2 = c3.number_input(f"Trial 2", value=None, placeholder="Time (s)", key=f"At2_{i}") # defines variable with number input in third column, uses unique key to clarify between each iteration
    At3 = c4.number_input(f"Trial 3", value=None, placeholder="Time (s)", key=f"At3_{i}") # defines variable with number input in fourth column, uses unique key to clarify between each iteration

    # appends each of the above inputs to empty lists, inside for loop 
    angles.append(angle)
    Atrial_1.append(At1)
    Atrial_2.append(At2)
    Atrial_3.append(At3)

df_angles = pd.DataFrame({ # creates pandas dataframe from lists
    "Angle (degrees)": angles,
    "Trial 1 (s)": Atrial_1,
    "Trial 2 (s)": Atrial_2,
    "Trial 3 (s)": Atrial_3
})

st.markdown("#### Entered Data:")
columns1 = df_angles.columns[1:3] # defines columns to calculate average
df_angles["Average Time (s)"] = df_angles[columns1].mean(axis=1) # calculates mean of specific columns in dataframe and appends to dataframe new column
df_angles["Period (s)"] = df_angles["Average Time (s)"]/5 # calculates period by dividing average time by 5, appends to dataframe into new columm
st.dataframe(df_angles) # returns dataframe in streamlit platform for user readability

if Alength: # need if then because before Alength is inputted the following calculations would return an error 
    df_angles["Calculated 'g' (m/s^2)"] = (4 * math.pi**2 * Alength)/((df_angles["Period (s)"])**2) # appends calculated g value to dataframe
    df_angles["Calculated uncertainty"] = ((((0.005*2*math.pi)/(df_angles["Period (s)"]))**2)+((0.08*Alength*(math.pi**2)/(df_angles["Period (s)"])**3)))**0.5 # appends calculated uncertainty value to dataframe
    avg_g_A = df_angles["Calculated 'g' (m/s^2)"].mean() # defines avg g value for future returns
    avg_uncert_A = df_angles["Calculated uncertainty"].mean() # defines avg uncertainty for future returns
    st.write(f"Average g: {avg_g_A:0.2f} m/s^2") # uses f' to return average g, :0.2f indicates only 2 decimal places
    st.write(f"Average uncertainty: {avg_uncert_A:0.2f}") # uses f' to return average uncertainty, :0.2f indicates only 2 decimal places
    fig, ax = plt.subplots() # creates empty fig, ax for matplotlib visualization
    ax.set_ylim(5,18) # sets reasonable limits for calculated g (for this experiment)
    ax.errorbar(df_angles.index, df_angles["Calculated 'g' (m/s^2)"], yerr=df_angles["Calculated uncertainty"], fmt='o', capsize=5) # uses .errorbar function to visualize calculated g on y axis, index on x axis, and error bars of specific size
    ax.set_xlabel("Index") 
    ax.set_ylabel("Calculated 'g' (m/s^2)")
    st.pyplot(fig) # returns visualization on streamlit for user to read
    st.session_state["avg_g_A"] = avg_g_A # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function
    st.session_state["avg_uncert_A"] = avg_uncert_A # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function

st.session_state["df_angles"] = df_angles # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function

# second part of experiment, essentially repeated code from above
st.markdown(" ### Changing Length")
st.write("Here, input the angle of elevation, the different lengths of the pendulum, and the time it took to complete 5 oscillations.")
Langle = st.number_input("Angle of Elevation (degrees)", value=None, placeholder="(degrees)") # defines variable using number input on page, originally no value, when empty reads "(meters)"
st.session_state["Langle"] = Langle # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function
m = st.number_input("Number of Lengths:", value=1) # defines variable using number input 

# creates empty lists that are appended in for loop with number_inputs, for input into dataframe
lengths = []
Ltrial_1 = []
Ltrial_2 = []
Ltrial_3 = []
c1, c2, c3, c4 = st.columns(4) # defines columns for streamlit to format input placement

# for loop so that there are only the number of entries for the number inputted with "m"
for i in range(m):
    length = c1.number_input(f"Length {i+1}", value=None, placeholder="(meters)", key=f"L_{i}") # defines variable with number input in first column, uses unique key to clarify between each iteration
    Lt1 = c2.number_input(f"Trial 1", value=None, placeholder="Time (s)", key=f"Lt1_{i}") # defines variable with number input in second column, uses unique key to clarify between each iteration
    Lt2 = c3.number_input(f"Trial 2", value=None, placeholder="Time (s)", key=f"Lt2_{i}") # defines variable with number input in third column, uses unique key to clarify between each iteration
    Lt3 = c4.number_input(f"Trial 3", value=None, placeholder="Time (s)", key=f"Lt3_{i}") # defines variable with number input in fourth column, uses unique key to clarify between each iteration

    # appends each of the above inputs to empty lists, inside for loop 
    lengths.append(length)
    Ltrial_1.append(Lt1)
    Ltrial_2.append(Lt2)
    Ltrial_3.append(Lt3)

df_lengths = pd.DataFrame({ # creates pandas dataframe from lists
    "Length (meters)": lengths,
    "Trial 1 (s)": Ltrial_1,
    "Trial 2 (s)": Ltrial_2,
    "Trial 3 (s)": Ltrial_3
})
st.markdown("#### Entered Data:")
columns2 = df_lengths.columns[1:3] # defines column to calculate the average
df_lengths["Average Time (s)"] = df_lengths[columns2].mean(axis=1) # calculates mean of specific columns in dataframe and appends to dataframe new column
df_lengths["Period (s)"] = df_lengths["Average Time (s)"]/5 # calculates period by dividing average time by 5, appends to dataframe into new columm
st.dataframe(df_lengths) # returns dataframe in streamlit for user to read

if Langle: # need if then because before Langle is inputted the following calculations would return an error 
    df_lengths["Calculated 'g' (m/s^2)"] = (4 * math.pi**2 *(df_lengths['Length (meters)']))/((df_lengths["Period (s)"])**2) # appends calculated g value to dataframe
    df_lengths["Calculated uncertainty"] = ((((0.005*2*math.pi)/(df_lengths["Period (s)"]))**2)+((0.08*(df_lengths["Length (meters)"])*(math.pi**2)/(df_lengths["Period (s)"])**3)))**0.5 # appends calculated uncertainty value to dataframe
    avg_g_L = df_lengths["Calculated 'g' (m/s^2)"].mean() # defines avg g value for future returns
    avg_uncert_L = df_lengths["Calculated uncertainty"].mean() # defines avg uncertainty for future returns
    st.write(f"Average g: {avg_g_L:0.2f} m/s^2") # uses f' to return average g, :0.2f indicates only 2 decimal places
    st.write(f"Average uncertainty: {avg_uncert_L:0.2f}") # uses f' to return average uncertainty, :0.2f indicates only 2 decimal places
    fig, ax = plt.subplots() #creates empty fig, ax for matplotlib plot
    ax.set_ylim(5,18) # sets reasonable limits for calculated g (for this experiment)
    ax.errorbar(df_lengths.index, df_lengths["Calculated 'g' (m/s^2)"], yerr=df_lengths["Calculated uncertainty"], fmt='o', capsize=5) # uses .errorbar function to visualize calculated g on y axis, index on x axis, and error bars of specific size
    ax.set_xlabel("Index")
    ax.set_ylabel("Calculated 'g' (m/s^2)")
    st.pyplot(fig) # returns visualization on streamlit
    st.session_state["avg_g_L"] = avg_g_L # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function
    st.session_state["avg_uncert_L"] = avg_uncert_L # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function

st.session_state["df_lengths"] = df_lengths # saves entered value for the given session (will reset if reload page or change pages and return), value can be accessed on different pages with this function