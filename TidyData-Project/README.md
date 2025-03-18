# ReadMe for Tidy Data Project: Federal Research and Development Budgets

## Project Overview

I created this Jupiter Notebook to develop my skills in tidying data such that is can be analyzed and understood logically. This is a cumulation not only of data tidying principles and methods, but also of how to analyze and visualize neat data represeted as dataframes. The goal of this project was to organize an external dataset, which contained information regarding federal research and development spending across government agencies. 

According to the Tidy Data Pricples, neat data is such that:
- Every variable forms a column
- Every observation forms a row
- Each value is a cell

Prior to my development of this project, the data was jumbled such that one column contained multiple variables, and each row also represented a *variable*. 

After tidying the data, I then created tables which represented average values for a neater, numerical analysis. 

Finally, I was able to use my neat data to create visualizations that could be easily understood. This not only was helpful in understanding the context of the dataset, but also created insightful visualizations which allowed me to make inferences. 

## Instructions

To run this notebook, you must install and import several dictionaries which are later referred to. These include pandas, seaborn, matplotlib, squarify, and numpy.

To install: 

```
pip install pandas
!pip install seaborn
!pip install matplotlib.pyplot
!pip install squarify
!pip install numpy
```

To import:

```
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import squarify
import numpy as np
```