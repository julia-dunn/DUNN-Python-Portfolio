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
st.write("For the method with a mass in freefall, the setup is once again pretty simple. You will need a marble/mass, a way to tell time, pictured is a photogate, a meter stick, and a stand. Align the photogates a measured distance apart by attaching them to the stand as pictured below.")
with st.columns(3)[1]:
    st.image("Screenshot 2025-05-01 at 3.51.19 PM.png")
st.write("You will drop the object of a known mass from varying heights and measure the time it takes the mass to fall.")
st.write("You should see that the time it takes to fall depends clearly on the height. With both measurements, the acceleration due to gravity 'g' can be calculated with the following equation:")
st.latex(r'''
        g = \frac{2 \Delta y}{t^2}
        ''')
st.markdown(" ### Third: The Atwood Machine")
st.write("An atwood machine is a mechanism which uses a light strong to attach two masses on either side of a pulley. For this method, you will need a stand, a lightweight pulley, a lightweight string, a set of multiple masses, a meter stick, and something to measure time, whether that is a stopwatch or a photogate. Setup as depicted below:")
with st.columns(3)[1]:
    st.image("Screenshot 2025-05-01 at 4.08.50 PM.png")
st.write("You will set up two objects of different masses on either side of the pulley and allow them to accelerate a fixed distance. Measure the amount of time it takes for the masses to travel the given distance.")
st.write("You will see that the time it takes depends on the distance, as well as each of the masses. The acceleration due to gravity 'g' can be calculated with the following equation:")
st.latex(r'''
         g = \frac{2 \Delta y \left( m_1 + m_2 \right)}{t^2 \left( m_1 - m_2 \right)})
         ''')
st.markdown(" ### Fourth: Incline")
st.latex(r'''
         g = \frac{2x}{t^2 \sin \theta}
         ''')