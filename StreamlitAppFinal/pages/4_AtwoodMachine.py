import streamlit as st
import pandas as pd
st.title("The Atwood Machine Experiment")
st.write("Here is where you can input your data for the atwood machine experiment. How many mass configurations did you use?")
n = st.number_input("Number of mass configurations:", value=1)
dist = st.number_input("Distance masses were allowed to fall:", value=None, placeholder="(meters)")
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
    m1 = c1.number_input(f"Mass 1", value=None, placeholder="(grams)", key=f"m1_{i}")
    m2 = c2.number_input(f"Mass 2", value=None, placeholder="(grams)", key=f"m2_{i}")
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

df_machine = ({
    "Mass 1 (grams)": mass1,
    "Mass 2 (grams)": mass2,
    "Trial 1 (s)": Mtrial_1,
    "Trial 2 (s)": Mtrial_2,
    "Trial 3 (s)": Mtrial_3,
    "Trial 4 (s)": Mtrial_4,
    "Trial 5 (s)": Mtrial_5
})

st.markdown("#### Data Entered:")
st.dataframe(df_machine)