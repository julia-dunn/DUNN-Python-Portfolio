import streamlit as st
import pandas as pd
st.title("The Incline Experiment")
st.write("Here you can input your data for the incline experiment. First, input the standard dimensions for your setup.")
radius = st.number_input("Radius of marble:", value=None, placeholder="(meters)")
mass = st.number_input("Mass of marble:", value=None, placeholder="(grams)")
length = st.number_input("Length of track:", value=None, placeholder="(meters)")
st.write("You must also input the number of configurations you tested, that is the different heights you set the track to.")
n = st.number_input("Number of heights:", value=1)
Iheights = []
Idistances = []
Itrial_1 = []
Itrial_2 = []
Itrial_3 = []
Itrial_4 = []
Itrial_5 = []
for i in range(n):
    st.markdown(f" #### Configuration {i+1}")
    Ih = st.number_input(f"Height of track", value=None, placeholder="(meters)", key=f"Ih_{i}")
    x = st.number_input(f"Distance traveled along track", value=None, placeholder="(meters)", key=f"x_{i}")
    c1, c2, c3, c4, c5 = st.columns(5)
    It1 = c1.number_input(f"Trial 1", value=None, placeholder="time(s)", key=f"It1_{i}")
    It2 = c2.number_input(f"Trial 2", value=None, placeholder="time(s)", key=f"It2_{i}")
    It3 = c3.number_input(f"Trial 3", value=None, placeholder="time(s)", key=f"It3_{i}")
    It4 = c4.number_input(f"Trial 4", value=None, placeholder="time(s)", key=f"It4_{i}")
    It5 = c5.number_input(f"Trial 5", value=None, placeholder="time(s)", key=f"It5_{i}")

    Iheights.append(Ih)
    Idistances.append(x)
    Itrial_1.append(It1)
    Itrial_2.append(It2)
    Itrial_3.append(It3)
    Itrial_4.append(It4)
    Itrial_5.append(It5)

df_incline = ({
    "Height (m)": Iheights,
    "Distance x (m)": Idistances,
    "Trial 1 (s)": Itrial_1,
    "Trial 2 (s)": Itrial_2,
    "Trial 3 (s)": Itrial_3,
    "Trial 4 (s)": Itrial_4,
    "Trial 5 (s)": Itrial_5
})

st.markdown("#### Entered Data")
st.dataframe(df_incline)

st.session_state["df_incline"] = df_incline