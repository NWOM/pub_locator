import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv('resources/data/cleaned_pub.csv')

# Display some basic information and statistics about the dataset
st.write("# Welcome to the Dataset Viewer")
st.write(f"Number of rows: {df.shape[0]}")
st.write(f"Number of columns: {df.shape[1]}")
st.write("Preview of the dataset:")
st.write(df.head())

# Display some descriptive statistics
st.write("Descriptive Statistics:")
st.write(df.describe())

# Display a histogram of the 'latitude' column
st.write("Histogram of Latitude:")
plt.hist(df["latitude"], bins=30)
st.pyplot()

# Display a scatter plot of 'longitude' vs. 'latitude' 
st.write("Scatter Plot of Longitude vs. Latitude:")
plt.scatter(df["longitude"], df["latitude"])
st.pyplot()
