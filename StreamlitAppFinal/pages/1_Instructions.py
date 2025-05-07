# imports required dictionaries for all pages
import streamlit as st
import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt

# explanation of the how to run each experiment, uses st. to apply markdown sytnax to streamlit platform
st.markdown(" ## Instructions!")
st.write("Just in case you're not sure what I am talking about, here is an overview of the different methods you might use to calculate 'g'.")

# first experiment: the pendulum
st.markdown(" ### First: The Pendulum")
st.write("When using a pendulum to solve 'g,' the setup is pretty simple. You will need a lightweight string with a small mass at its end, a stand, a protractor or another way to measure angle, a meter stick, and a stopwatch. Setup the pendulum vertically such that it is supported by the stand, with the protractor aligned at the axis of rotation. It should look like this!")
with st.columns(3)[1]:
    st.image("https://img.brainkart.com/imagebk37/dXiIK15.jpg") # returns image into streamlit platform 
st.write("With this setup, you will first raise the mass, hanging from a string of fixed length, to different angles of elevation, and measure the time it takes to complete 5 oscillations, such that the period is the time divided by five. You will then raise the mass to a constant angle of elevation, varying the length of the string, and once again measure the time such that you can calculate the period.")
st.write("You should see that the period of oscillation has no dependence on the angle of oscillation, while it does depend on the length of the pendulum. With the length of the string and the period of oscillatin, the acceleration due to gravity 'g' can be calculated with the following equation:")
 # uses latex syntax to return correctly formatted expression into streamlit app
st.latex(r'''
        g = \frac{4\pi^2 L}{T^2}
        ''')

# second experiment: free fall
st.markdown(" ### Second: Free fall")
st.write("For the method with a mass in freefall, the setup is once again pretty simple. You will need a marble/mass, a way to tell time, pictured is a photogate, a meter stick, and a stand. Align the photogates a measured distance apart by attaching them to the stand as pictured below.")
with st.columns(3)[1]:
    st.image("https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22screenshot_freefall.png%22%2C%22type%22%3A%22image%2Fpng%22%2C%22signedurl_expire%22%3A%222028-05-06T21%3A54%3A12.270Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2Ffb3dcd76fc104e5c%2Fscreenshot_freefall.png%3FExpires%3D1841262852%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DZqXv~7pPMmOJJcKg9KbhoMk0Vfs5onhWFHphGL7mKQV8E5brbEOWzDoN8FKfrw1izxjmS037tKFHA55f5jAzB2oqs3ffck2tuS005jvTB-jda0SGjG~spjdO-V17SKnB1Ks9~pzjJGwK0WEzvQW8fwR3InHKnDj67cYHBPF~HiyclCMJJsXNu~QPHUnn~0vqnjTTpO0FQgZzIRD7bvJTRzdHQCZPT4GUicik-SLH9i3sONxr6-L2mBkxbAtkqYWk2jqicy~vGVWlzf6MHghXMKuvQ1piviIIXK5X4dVPP4uKvnkxeWUcfqNL-ICiW-7YSOdGeWJN3pduTJjYG5Whdg__%22%7D") # returns image in streamlit platform
st.write("You will drop the object of a known mass from varying heights and measure the time it takes the mass to fall.")
st.write("You should see that the time it takes to fall depends clearly on the height. With both measurements, the acceleration due to gravity 'g' can be calculated with the following equation:")
 # uses latex syntax to return currectly formatted expression into streamlit app
st.latex(r'''
        g = \frac{2 \Delta y}{t^2}
        ''')

# third experiment: the atwood machine
st.markdown(" ### Third: The Atwood Machine")
st.write("An atwood machine is a mechanism which uses a light strong to attach two masses on either side of a pulley. For this method, you will need a stand, a lightweight pulley, a lightweight string, a set of multiple masses, a meter stick, and something to measure time, whether that is a stopwatch or a photogate. Setup as depicted below:")
with st.columns(3)[1]:
    st.image("https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22screenshot_atwoodmachine.png%22%2C%22type%22%3A%22image%2Fpng%22%2C%22signedurl_expire%22%3A%222028-05-06T21%3A54%3A31.436Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F4134f2876e934d17%2Fscreenshot_atwoodmachine.png%3FExpires%3D1841262871%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3DH0ecZ8IXarnH7ZfyqG4pgEnBBR76vpCELHdjWa-rbliGICtpJScla2meSPC7DXPPwa1crtWslfL4am9tk0IoY-i174rkoXHuMHZ6PrWqjNfIoYcpbJzGMzX1~ekkqTZ7Zwx9rs-HljDr2XT3ktqE2KsqoMSyW8FhIfcVIKCZY8~zRdRZxpEUqw0EOt51XeKV05k6EeNZVjXC9vo67hXP7T4Xf641fLVUJQi3nW7SZEpoI-k9RgYOaptMfKhM3JaOOJkZGD4V-B0NytfZfqDGEgimMlq42UcR4cHHDjMGpT6GpExmKvWLBMFRkmFVNiNBCIT8pQcJ-0B-cmq4WzIfTw__%22%7D") # returns image in streamlit platform
st.write("You will set up two objects of different masses on either side of the pulley and allow them to accelerate a fixed distance. Measure the amount of time it takes for the masses to travel the given distance.")
st.write("You will see that the time it takes depends on the distance, as well as each of the masses. The acceleration due to gravity 'g' can be calculated with the following equation:")
 # uses latex syntax to return correctly formatted expression into streamlit app
st.latex(r'''
         g = \frac{2 \Delta y \left( m_1 + m_2 \right)}{t^2 \left( m_1 - m_2 \right)})
         ''')

# fourth experiment: incline
st.markdown(" ### Fourth: Incline")
st.write("The final method you could use to calculate the acceleration due to gravity is a mass sliding down a cart. For this experiment, you will need an incline, a marble or cart, a meter stick, and a stopwatch or a photogate. Setup the materials such that you can change the angle of the incline and measure the distance the mass travels, as demonstrated below.")
with st.columns(3)[1]:
    st.image("https://imagekit.io/tools/asset-public-link?detail=%7B%22name%22%3A%22screenshot_incline.png%22%2C%22type%22%3A%22image%2Fpng%22%2C%22signedurl_expire%22%3A%222028-05-06T21%3A54%3A33.363Z%22%2C%22signedUrl%22%3A%22https%3A%2F%2Fmedia-hosting.imagekit.io%2F4e92b5845a0144a5%2Fscreenshot_incline.png%3FExpires%3D1841262873%26Key-Pair-Id%3DK2ZIVPTIP2VGHC%26Signature%3Db7JFpfFSOh8URKAARoEt2dyvJmHZx9HFS2-laHwHlnm4AMVe8fCYp-ovp5BZAXIMauIZyD2brAOls-20K3gcZsvlwIFLnQC49R77pHW6ribIBVXO~V0bYfyZuTByPyI12gbuy16sjzy5cWY1l-CVIz45cNgI8p2KFbHir~tUootb2pMRTnI0rUNcCAuvpfR-OPfbgAwgMRSFAuFT0YXy4Ba0rWL99BQ27KvRp~iT9NS9-b2JZgeUW48pYe9j7YMc-4wOUi5g~cDHgLMO7Xza5jU2XPv9uG-sfTYw2ndMKQX0XX0RixomBX5-UJ5N4ux-mtNWoqge0lADXFT3pv86hg__%22%7D") # returns image in streamlit platform
st.write("You will drop the marble such that it rolls different distances down the incline and measure the time it takes. In addition, you will measure the time it takes the ball to travel a fixed distance with changing angles of incline.")
st.write("You will see that the time it takes for the marble to fall depends both on the distance it travels and the angle of incline. The acceleration due to gravity 'g' can be calculated with the following equation:")
 # uses latex syntax to return correctly formatted expression into streamlit app
st.latex(r'''
         g = \frac{2x}{t^2 \sin \theta}
         ''')