# Final Streamlit App README
## Physics Right of Passage: Calculating 'g'

### Project Overview 

Welcome to the home page README for my final project, a streamlit app related to the field that interests me. I chose to create an app that is incredibly useful for introductory phsycis and scientific exploration. In most university Physics 1 courses, there is a lab component in which students use many experimental methods to calculate the accelerationd ue to gravity on Earth. They have to use the scientific method to create in depth lab reports that are, at times, tedious considering the content is not the most "earth-shattering." 

One aspect of these reports that is incredibly important is uncertainty. Uncertainty of a value depends on the uncertainty of measurements that make up the calculation. Fundamentally, tools used to measure values have uncertainty because they can only be marked to a specific increment. Thus, when you calculate a value based on many measurements, those uncertainties must be propagated to understand the overall uncertainty of your calculations. These calculations can be challenging and time consuming, especially for those with a limited understanding of calculus. The purpose of this app is to provide introductory physics students with a platform where they can build these skills and test their own uncertainty calculations. In addition, the platform demonstrates, through visualizations, how uncertainty does not always account for inaccuracy. When this happens, which is often, there is likely either a systematic problem with the experimental method or substantial human error. 

The first method typically used a simple pendulum, for which the acceleration due to gravity can be calculated with the period of the pendulum and the length of the spring. Depicted below is what it may look like in a professional lab.

![The Simple Pendulum](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSP0Y3G6X2BoygDHwH9V-bfU4BR8-nEu65BdA&s)

The second method typically used is freefall. Everyone knows that when you drop something, it falls to the ground. In fact, regardless of the mass of an object (in a perfect, air-resistence-less world tha is), all objects fall with the same acceleration (g). By dropping small, smooth objects, like marbles, at different heights, you can once again calculate the acceleration due to gravity.

Third is the Atwood Machine, a much more complicated setup that demonstrates how different sized masses attached by a pulley accelerate in g. This, once again, gives students the opportunity to make more complicated calculations because of the number of measurements invlved. Depicted below is a typical atwood setup.

![Atwood Machine](https://cdn1.byjus.com/wp-content/uploads/2022/06/atwood-machine1.png)

Finally, an incline. Once again, most people are familiar with the idea that when you roll something, like a marble, down a hill, it will accelerate. It is more complicated, however, when you consider the rotational energy in addition to the translational kinetic energy the object gains. That factor, once again, makes calculations for g slightly more complicated than the typical free fall. 

### Setup and Run Instructions

There are a few required libraries for this app in order to run the necessary calculations. They are listed in the requirements file within the portfolio, and include:
- Streamlit 1.41.1
- Pandas 2.0
- Numpy 3.1
- Matplotlib 3.10.0

In order to install these libraries, run the following commands within your terminal:
```
{
    pip install streamlit
    pip install pandas
    pip install numpy
    pip install matplotlib
}
```

Then, to run the app locally, run this command in the integrated terminal:
```
{
    streamlit run main.py
}
```
In addition, you can access the platform via this link!

[🔎](https://physics-right-of-passage.streamlit.app/)

### App Features

#### Informative Pages

The purpose of this app is to provide a usable resource for introductory physics students. The landing page features links to each of the pages where the user can input data, as well as an instructions page to develop an understanding of the experiments. In addition, the homepage is where the user can learn more about what uncertainty is and why it is important for the scientific method.

#### Data Input

There are four pages of this app where users can input data from their experiments. Each page is specific for one experiment, the pendulum, freefall, the atwood machine, or the incline. Here, the user will import setup schematics and experimental measurements. Once the necessary data has been entered into the platform, a dataframe summarizing the entered data is returned. In addition, relevant average values, the calculated 'g' value, and the calculated uncertainty are added to the dataframe for each setup. In addition, once the user inputs data for an experimental procedure, a graph is generated with the calculated 'g' and uncertainty for each trial. On the final results page, each of these visualizations, as well as the average 'g' and average uncertainty values are cumulated and compared. It is then reported which method had the lowest uncertainty and which had the least inaccruacy, that is which value was the closest to the known 9.8 m/s^2.

##### Pendulum 

Data Required for Changing Angle:
- Length of pendulum (m)
- Number of angles measured 
- For each setup:
    - Angle (degrees)
    - Time for 3 trials (s)

Data Returned for Changing Angle:
- Average Time 
- Period 
- Average 'g'
- Average uncertainty

Data Required for Changing Length:
- Angle of elevation (degrees)
- Number of lengths measured 
- For each setup:
    - Length (m)
    - Time for 3 trials (s)

Data Returned for Changing Length:
- Average time
- Period
- Average 'g'
- Average uncertainty

##### The Freefall Experiment 

Data required for stopwatch:
- Number of heights 
- For each setup:
    - Time for 5 trials (s)

Data Returned for stopwatch: 
- Average Time 
- Calculated 'g'
- Calculated Uncertainty
- Average 'g'
- Average uncertainty

Data required for photogates:
- Distance between photogates
- Number of distances measured 
- For each setup:
    -Time for 5 trials (s)

Data Returned for photogates: 
- Average Time 
- Calculated 'g'
- Calculated Uncertainty
- Average 'g'
- Average uncertainty

##### The Atwood Machine

 Data Required:
- Number of mass configurations
- Distance masses were allowed to fall 
- For each setup:
    - Mass 1
    - Mass 2
    Time for 5 trials (s)

Data Returned:
- Average Time 
- Average 'g'
- Average uncertainty

##### Incline

Data Required:
- Length of track
- Number of heights measured
- For each setup:
    - Height of track
    - Distance traveled along track
    - Time for 5 trials (s)

Data returned:
- Average time 
- Average 'g'
- Average uncertainty 

### References and Resources
- [Latex Syntax](https://docs.streamlit.io/develop/api-reference/text/st.latex)
- [Pendulum Information](https://www.brainkart.com/article/Acceleration-Due-to-Gravity-Using-Simple-Pendulum_36366/)
- [Format Troubleshooting](https://stackoverflow.com/questions/70932538/how-to-center-the-title-and-an-image-in-streamlit)
- [Page Link](https://docs.streamlit.io/develop/api-reference/widgets/st.page_link)
- [Streamlit Cheat Sheet](https://docs.streamlit.io/develop/quick-reference/cheat-sheet)
- [Markdown Syntax Cheat Sheet](https://www.markdownguide.org/basic-syntax/#links)
- Simon-Robertson, Anna. Instruction for Physics A: Lab 1. Fall, 2023
- Simon-Robertson, Anna. Instruction for Physics A: Lab 2. Fall, 2023
- Simon-Robertson, Anna. Instruction for Physics A: Lab 3. Fall, 2023
- Simon-Robertson, Anna. Instruction for Physics A: Lab 4. Fall, 2023
- Serway, R. and Jewett, J. Physics for Scientists and Engineers. Cengage Learning, 2019.

### Visual Examples