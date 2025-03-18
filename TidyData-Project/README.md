# ReadMe for Tidy Data Project: Federal Research and Development Budgets

## Project Overview

I created this Jupiter Notebook to develop my skills in tidying data such that is can be analyzed and understood logically. This is a cumulation not only of data tidying principles and methods, but also of how to analyze and visualize neat data represeted as dataframes. The goal of this project was to organize an external dataset, which contained information regarding federal research and development spending across government agencies. 

According to the Tidy Data Pricples, neat data is such that:
- Every variable forms a column
- Every observation forms a row
- Each value is a cell

Prior to my development of this project, the data was jumbled such that one column contained multiple variables, and each row also represented a *variable*. 

Demonstration of melting data to follow tidy data principles:

```
df_fedrd_melted = pd.melt(df_fedrd,
                          id_vars = 'department',
                          value_vars = df_fedrd.columns[1:],
                          var_name = 'Year_GDP",
                          value_name = 'Research and Development Budget')
```

After tidying the data, I then created tables which represented average values for a neater, numerical analysis. 

Demonstration of creating pivot tables:

```
pivot_table_department = pd.pivot_table(df_fedrd_melted_tidy,
                         values = ['Research and Development Budget', 'GDP'],
                         index = 'department',
                         aggfunc = 'mean)
```

Finally, I was able to use my neat data to create visualizations that could be easily understood. This not only was helpful in understanding the context of the dataset, but also created insightful visualizations which allowed me to make inferences. 

Visualization comparing Budget with respect to Federal GDP:

[![Screenshot-2025-03-17-at-9-40-19-PM.png](https://i.postimg.cc/Mp1bq6GN/Screenshot-2025-03-17-at-9-40-19-PM.png)](https://postimg.cc/9DFqBjZY)

## Instructions

To run this notebook, you must install and import several dictionaries which are later referred to. These include pandas, seaborn, matplotlib, squarify, and numpy.

To install: 

```
!pip install pandas
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

Once the above have been run, the notebook will be accessible and legible such that the visualizations and analysis are understood. 

## Dataset Description

This dataset came from the GitHub account rfordatascience under the repository tidytuesday. It is an adjusted csv ile from a NY times article regarding the federal spending and budget allocation for the research and development agencies within the federal government. As disccussed by the source, "jonthegeek," this data comes directly from the American Association for the Advacement of Science Historical Trends page.

The dataset I used, more specifically, did not consider the outlays but instead focused on budget allocation and gdp of the different departments throughout time. The data came from a csv which I then converted into a dataframe and manipulated throughout the project. It is important to consider that because the source of the data is the association for advancement of science, it is possible certain years or departments were selected to illicit specific trends and demonstrate a need for a focus on scientific research. 

## References 
- https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf 
- https://vita.had.co.nz/papers/tidy-data.pdf 
- https://stackoverflow.com/questions/15891038/change-column-type-in-pandas 
- https://stackoverflow.com/questions/51004029/create-a-new-dataframe-based-on-rows-with-a-certain-value 
- https://stackoverflow.com/questions/20461165/how-to-convert-index-of-a-pandas-dataframe-into-a-column
- https://stackoverflow.com/questions/20490274/how-to-reset-index-in-a-pandas-dataframe
- https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
- https://stackoverflow.com/questions/41400136/how-to-do-waffle-charts-in-python-square-piechart
- https://github.com/rfordatascience/tidytuesday/tree/main/data/2019/2019-02-12 