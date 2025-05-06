import streamlit as st
import pandas as pd
import math
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Physics Right of Passage: Calculating 'g'")
st.write("Welcome to the best new app for university physics students. This app is built to help you with your introductory physics lab. Many students, myself included, spend the first semester in lab calculating the acceleration due to gravity in 4 different ways: with a pendulum, in free fall, with an Atwood machine, or on an incline. But which is the most accurate?")
st.markdown(" ### The Experiments!")
st.write("When calculating 'g,' there are four different methods typically used in a basic Physics 1 course. To learn more about the setup, click below to navigate to the 'Instructions' page.")
st.page_link("pages/1_Instructions.py", label="Instructions", icon="📝")
st.write("These are the four classical methods! To input your data and analyze the results, click the method you used!")
st.page_link("pages/2_Pendulum.py", label="Pendulum", icon="📍")
st.page_link("pages/3_FreeFall.py", label="Free Fall", icon="📍")
st.page_link("pages/4_AtwoodMachine.py", label="Atwood Machine", icon="📍")
st.page_link("pages/5_Incline.py", label="Incline", icon="📍")
st.markdown(" ### Results!")
st.write("Once you have inputted your data, click below to see the results! This platform will calculate the uncertainties for each experiment and compare their precision/accuracy. Uncertainty calculations are essential for the scientific method because they demonstrate the uncertainty of an experiment without human error, that is if done perfectly. Does your uncertainty account for the accuracy of your results? Or, is it possible the experiment could be improved?")
st.page_link("pages/6_Results.py", label="Results!", icon="🔎")
st.markdown("#### Uncertainty:")
st.write("But what is uncertainty? And how is it calculated?")
st.write("The uncertainty of a value depends on the uncertainty of the measurements that make up the calculation. When completing an experiment, there is fundamental uncertainty due to the tools you use. For example, when you measure length with a typical ruler, the smallest increment marked is 1/16 of an inch. Because of this, there is an uncertainty in your measurement of about 1/32 of an inch. Then, when you calculate a value based on multiple measurements, the uncertainty of those measurements can be propagated into an overall uncertainty. The equation is as follows:")
st.latex(r'''
        \sigma_f = \sqrt{ \left( \frac{\delta_f}{\delta_x} \delta_x \right)^2 + \left( \frac{\delta_f}{\delta_y} \delta_y \right)^2 }
         ''')
st.write("This means that for every variable (x, y, etc.), you take the partial derivative with respect to that variable and multiply it by the uncertainty of the measurement. Then, you square this value for each variable, add them together, and take the square root.")
st.write("For our pendulum experiment, this is the uncertainty:")
st.latex(r'''
        \sigma_g = \sqrt{ \left( \left( \frac{0.005}{\frac{T}{2\pi}} \right)^2 + \left( \frac{0.08L\pi^2}{T^3} \right)^2 \right) }
        ''')
st.write("For the freefall experiment, this is the uncertainty:")
st.latex(r'''
        \sigma = \sqrt{ \left( \left( \frac{-2y}{t^3} \right)(0.0005) \right)^2 + \left( \left( \frac{2}{t^2} \right)(0.01) \right)^2 }
        ''')
st.write("For the Atwood Machine experiment, this is the uncertainty:")
st.latex(r'''
        \sigma_g = \sqrt{\left( \frac{-0.0004(m_1 + m_2)}{t^2(m_1 - m_2)} \right)^2 + \left( \frac{0.001(m_1 + m_2)}{t^2(m_1 - m_2)} \right)^2 + 2 \left( \frac{0.000774(t^2(m_1 - m_2)^2 - t^2[0.000774(m_1 + m_2)]^2)}{[t^2(m_1 - m_2)]^2} \right)^2}
        ''')
st.write("For the Incline experiment, this is the uncertainty:")
st.latex(r'''
        \sigma_g = \sqrt{ \left( \frac{14}{5t^{2} \sin(\theta)} \cdot 0.0005 \right)^2 + \left( \frac{-28x}{5t^{3} \sin(\theta)} \cdot 0.01 \right)^2 + \left( \frac{-14x \cos(\theta) \csc(\theta)}{5t^{2}} \cdot \sigma_{\theta} \right)^2}
        ''')
st.write("Where theta is defined as:")
st.latex(r'''
        \theta = \tan^{-1}(\frac{height~of~track}{length~of~track})
        ''')
st.write("And the uncertainty in theta is defined as:")
st.latex(r'''
        \sigma_{\theta} = \sqrt{ \left( \frac{0.0005}{1 + \left( \frac{H}{L} \right)^2} \right)^2 + \left( \frac{-0.0005}{1 + \left( \frac{H}{L} \right)^2} \right)^2}
        ''')