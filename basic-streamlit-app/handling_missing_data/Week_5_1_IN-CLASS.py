import pandas as pd            # Library for data manipulation
import seaborn as sns          # Library for statistical plotting
import matplotlib.pyplot as plt  # For creating custom plots
import streamlit as st         # Framework for building interactive web apps

# ================================================================================
#Missing Data & Data Quality Checks
#
# This lecture covers:
# - Data Validation: Checking data types, missing values, and ensuring consistency.
# - Missing Data Handling: Options to drop or impute missing data.
# - Visualization: Using heatmaps and histograms to explore data distribution.
# ================================================================================
st.title("Missing Data & Data Quality Checks")
st.markdown("""
This lecture covers:
- **Data Validation:** Checking data types, missing values, and basic consistency.
- **Missing Data Handling:** Options to drop or impute missing data.
- **Visualization:** Using heatmaps and histograms to understand data distribution.
""")

# ------------------------------------------------------------------------------
# Load the Dataset
# ------------------------------------------------------------------------------
# Read the Titanic dataset from a CSV file.
df = pd.read_csv("titanic.csv")

# ------------------------------------------------------------------------------
# Display Summary Statistics
# ------------------------------------------------------------------------------
# Show key statistical measures like mean, standard deviation, etc.
st.write("**Summary Statistics**")
st.write(df.shape) # age missing not at random, not keeping track of children (deleted in dataset, real titanic people did) MNAR
st.dataframe(df.describe()) # only describes numeric columns 

# ------------------------------------------------------------------------------
# Check for Missing Values
# ------------------------------------------------------------------------------
# Display the count of missing values for each column.
st.write("**Number of Missing Values by Column**")
# st.dataframe(df.isnull()) # checked values are null (true), unchecked values are not null (false)
st.dataframe(df.isnull().sum()) # use age for imputations on thursday
# ------------------------------------------------------------------------------
# Visualize Missing Data
# ------------------------------------------------------------------------------
# Create a heatmap to visually indicate where missing values occur.
st.subheader("Heatmap of Missing Values")
fig, ax = plt.subplots() #plt is matlibpy.plot, subplots method takes canvas and puts it in python environment, fig is figure (looking for visualization code), ax is customizable axis
sns.heatmap(df.isnull(),cmap = "viridis",cbar = False) # extra parameters for formatting, with just sns it does not go into the actual app itself
st.pyplot(fig) # reveals our visualization

# ================================================================================
# Interactive Missing Data Handling
#
# Users can select a numeric column and choose a method to address missing values.
# Options include:
# - Keeping the data unchanged
# - Dropping rows with missing values
# - Dropping columns if more than 50% of the values are missing
# - Imputing missing values with mean, median, or zero
# ================================================================================
st.subheader("Handle Missing Data")

column = st.selectbox("Choose a column to fill", 
             df.select_dtypes(include=["number"]).columns) # creates a list of column names where those columns are numeric data types

method = st.radio("Choose a method", 
                  ["Original DF", "Drop Rows", 
                   "Impute Mean", "Impute Median", "Impute Zero"])

# Work on a copy of the DataFrame so the original data remains unchanged.
# df is going to stay untouched\
# df_clean is a copy of df that will change with the custom filters
df_clean = df.copy()

if method == "Original DF":
    pass # leaves df_clean as df.copy(), makes no changes
elif method == "Drop Rows":
    df_clean = df_clean.dropna(subset=[column]) # clarifies to only drop if missing the data in specific column, without subset drops all rows with any missing data 
elif method == "Impute Mean":
    df_clean[column] = df_clean[column].fillna(df_clean[column].mean())
elif method == "Impute Median":
    df_clean[column] = df_clean[column].fillna(df_clean[column].median())
elif method == "Impute Zero":
    df_clean[column] = df_clean[column].fillna(0)

# Apply the selected method to handle missing data.

# ------------------------------------------------------------------------------
# Compare Data Distributions: Original vs. Cleaned
#
# Display side-by-side histograms and statistical summaries for the selected column.
# ------------------------------------------------------------------------------
st.subheader("Cleaned Data Distribution")
fig, ax = plt.subplots()
sns.histplot(df_clean[column], kde=True) #kde=True creates line of distrubution
st.pyplot(fig)