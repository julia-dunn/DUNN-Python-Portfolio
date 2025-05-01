import streamlit as st
import pandas as pd 

st.markdown(" ## Instructions!")
st.write("Just in case you're not sure what I am talking about, here is an overview of the different methods you might use to calculate 'g'.")
st.markdown(" ### First: The Pendulum")
st.write("When using a pendulum to solve 'g,' the setup is pretty simple. You will need a lightweight string with a small mass at its end, a stand, a protractor or another way to measure angle, a meter stick, and a stopwatch. Setup the pendulum vertically such that it is supported by the stand, with the protractor aligned at the axis of rotation. It should look like this!")
with st.columns(3)[1]:
    st.image("https://img.brainkart.com/imagebk37/dXiIK15.jpg")
st.write("With this setup, you will first raise the mass, hanging from a string of fixed length, to different angles of elevation, and measure the time it takes to complete 5 oscillations, such that the period is the time divided by five. You will then raise the mass to a constant angle of elevation, varying the length of the string, and once again measure the time such that you can calculate the period.")
st.write("You should see that the period of oscillation has no dependence on the angle of oscillation, while it does depend on the length of the pendulum. With the length of the string and the period of oscillatin, the acceleration due to gravity 'g' can be calculated with the following equation:")
st.latex(r'''
        g = \frac{4\pi^2 L}{T^2}
        ''')
st.markdown(" ### Second: Free fall")