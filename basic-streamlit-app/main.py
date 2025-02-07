import streamlit as st
import pandas as pd

st.title("Who Are Palmer's Penguins?")
st.write("Use this app to learn more about Palmer's Penguins: who they are and where they came from. Penguins are one of the most interesting animals and as you interact with this platform, I hope you are intruiged by how the statistical information demonstrates their demographic.")

df = pd.read_csv("data/penguins.csv")

penguin_appretiation = st.select_slider("How much do you like penguins?",["I hate them!","I know literally nothing about penguins", "God's greatest gift to Earth"])
if penguin_appretiation == "I hate them!":
    st.write("What! How could you not like penguins?")
    st.text_input("Please explain your hatred")
elif penguin_appretiation == "I know literally nothing about penguins":
    st.write("No worries! We can give you lots of information")
    st.radio("Which of these do you want to learn about first?", ["Species", "Island", "Physical Features"])
else:
    st.write("I totally agree!")
    st.number_input("How many penguins have you adopted through World Wildlife?", min_value=0, step=1)
