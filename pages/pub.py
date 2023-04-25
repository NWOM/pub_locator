import streamlit as st
import pandas as pd
import folium
from streamlit_folium import folium_static

df = pd.read_csv('C:/Users/suman/OneDrive/Desktop/Data Science Internship/near_pub/resources/data/open_pubs.csv')
df.columns=['fsa_id','name','adress','postcode','easting','northing','latitude','longitude','local_authority']
df['latitude']=df['latitude'].str.replace('\\','Na')
df['longitude']=df['longitude'].str.replace('\\','Na')
df['latitude']=df['latitude'].str.replace('NaN','nan').astype(float)
df['longitude']=df['longitude'].str.replace('NaN','nan').astype(float)
df.dropna(inplace=True)
postal_codes = df['postcode'].unique()
local_authorities = df['local_authority'].unique()

def_loc = [df['latitude'].mean(), df['longitude'].mean()]
def_zoom = 10


def filter(option):
    if option in postal_codes:
        return df[df['postcode'] == option]
    elif option in local_authorities:
        return df[df['local_authority'] == option]


def create_map(data):
    m = folium.Map(location=def_loc, zoom_start=def_zoom)
    for index, row in data.iterrows():
        folium.Marker(
            location=[row['latitude'], row['longitude']],
            popup=row['name'],
            icon=folium.Icon(color='blue')
        ).add_to(m)
    return m


st.title('Pub Locations')
option = st.selectbox('Postal Code or Local Authority', list(postal_codes) + list(local_authorities))
data = filter(option)
st.write('Number of pubs found:', len(data))
folium_static(create_map(data))
