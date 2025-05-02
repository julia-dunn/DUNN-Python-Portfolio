import streamlit as st
import pandas as pd

df_angles = st.session_state["df_angles"]
df_lengths = st.session_state["df_lengths"]
df_stopwatch = st.session_state["df_stopwatch"]
df_photogate = st.session_state["df_stopwatch"]
df_machine = st.session_state["df_machine"]
df_incline = st.session_state["df_incline"]

st.dataframe(df_angles)