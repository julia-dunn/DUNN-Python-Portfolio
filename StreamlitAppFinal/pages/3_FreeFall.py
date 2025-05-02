import streamlit as st
import pandas as pd
st.title("The Freefall Experiment")
st.write("Here is where you can input your data for the free fall experiment, both when using a stopwatch and with photogates.")
st.markdown(" ### Stopwatch:")
n = st.number_input("Number of heights you dropped the ball from:", value=1)
Fheights = []
Strial_1 = []
Strial_2 = []
Strial_3 = []
Strial_4 = []
Strial_5 = []

for i in range(n):
    st.markdown(f" #### Configuration {i+1}")
    Fh = st.number_input(f"Height {i+1}", value=None, placeholder="(meters)", key=f"Fh_{i}")
    c1, c2, c3, c4, c5 = st.columns(5)
    St1 = c1.number_input(f"Trial 1", value=None, placeholder="time(s)", key=f"St1_{i}")
    St2 = c2.number_input(f"Trial 2", value=None, placeholder="time(s)", key=f"St2_{i}")
    St3 = c3.number_input(f"Trial 3", value=None, placeholder="time(s)", key=f"St3_{i}")
    St4 = c4.number_input(f"Trial 4", value=None, placeholder="time(s)", key=f"St4_{i}")
    St5 = c5.number_input(f"Trial 5", value=None, placeholder="time(s)", key=f"St5_{i}")

    Fheights.append(Fh)
    Strial_1.append(St1)
    Strial_2.append(St2)
    Strial_3.append(St3)
    Strial_4.append(St4)
    Strial_5.append(St5)

df_stopwatch = ({
    "Height (m)": Fheights,
    "Trial 1 (s)": Strial_1,
    "Trial 2 (s)": Strial_2,
    "Trial 3 (s)": Strial_3,
    "Trial 4 (s)": Strial_4,
    "Trial 5 (s)": Strial_5
})
st.markdown("#### Entered Data")
st.dataframe(df_stopwatch)

st.session_state["df_stopwatch"] = df_stopwatch

st.markdown(" ### Photogates:")
m = st.number_input("Number of distances between photogates:", value=1)
Fdistances = []
Ptrial_1 = []
Ptrial_2 = []
Ptrial_3 = []
Ptrial_4 = []
Ptrial_5 = []

for i in range(m):
    st.markdown(f" #### Configuration {i+1}")
    Fd = st.number_input(f"Distance {i+1}", value=None, placeholder="(meters)", key=f"Fd_{i}")
    c1, c2, c3, c4, c5 = st.columns(5)
    Pt1 = c1.number_input(f"Trial 1", value=None, placeholder="time(s)", key=f"Pt1_{i}")
    Pt2 = c2.number_input(f"Trial 2", value=None, placeholder="time(s)", key=f"Pt2_{i}")
    Pt3 = c3.number_input(f"Trial 3", value=None, placeholder="time(s)", key=f"Pt3_{i}")
    Pt4 = c4.number_input(f"Trial 4", value=None, placeholder="time(s)", key=f"Pt4_{i}")
    Pt5 = c5.number_input(f"Trial 5", value=None, placeholder="time(s)", key=f"Pt5_{i}")

    Fdistances.append(Fd)
    Ptrial_1.append(Pt1)
    Ptrial_2.append(Pt2)
    Ptrial_3.append(Pt3)
    Ptrial_4.append(Pt4)
    Ptrial_5.append(Pt5)

df_photogate = ({
    "Distance (m)": Fdistances,
    "Trial 1 (s)": Ptrial_1,
    "Trial 2 (s)": Ptrial_2,
    "Trial 3 (s)": Ptrial_3,
    "Trial 4 (s)": Ptrial_4,
    "Trial 5 (s)": Ptrial_5
})

st.markdown("#### Entered Data:")
st.dataframe(df_photogate)

st.session_state["df_photogate"] = df_photogate