import streamlit as st
import pandas as pd
from scipy.spatial import distance
import folium
from streamlit_folium import folium_static


# Load data
df = pd.read_csv('C:/Users/suman/OneDrive/Desktop/Data Science Internship/near_pub/resources/data/cleaned_pub.csv')

# Set up map
m = folium.Map(location=[df.latitude.mean(), df.longitude.mean()], zoom_start=12)

# Get user input
user_lat = st.number_input("Enter your latitude:")
user_lon = st.number_input("Enter your longitude:")

# Calculate Euclidean distances
df["distance"] = df[["latitude", "longitude"]].apply(lambda row: distance.euclidean(row, (user_lat, user_lon)), axis=1)

# Sort by distance and get nearest 5 pubs
nearest_pubs = df.sort_values("distance").head(5)

# Add markers for nearest pubs to map
for i, row in nearest_pubs.iterrows():
    folium.Marker(
        location=[row["latitude"], row["longitude"]],
        popup=row["name"]
    ).add_to(m)

# Display map with markers for nearest pubs
st.write("Nearest Pubs:")
folium_static(m)

# Display table of nearest pubs
st.write(nearest_pubs[["name", "distance"]])
