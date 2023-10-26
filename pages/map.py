import os
import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import folium
from folium.plugins import MarkerCluster

access_token = st.secrets['access_token']

st.write("# Mapping the Saint-Petersburg's Literary Space")
st.write("DB username:", st.secrets["access_token"])

m = folium.Map(
    location=[59.946288, 30.349214],
    zoom_start=12,
    tiles="https://tiles.stadiamaps.com/tiles/stamen_toner/{z}/{x}/{y}.jpg?access_token={access_token}",
    attr="Mapbox attribution",
)

marker_cluster = MarkerCluster().add_to(m)

data = st.cache_data(pd.read_csv)("data/addresses.csv")

for n, adress in data.iterrows():
    text = adress['event__place__name']
    folium.Marker(
        location=(adress['lat'], adress['lon']),
        popup=folium.Popup(text),
        icon=folium.Icon(color='green')
    ).add_to(marker_cluster)

st_data = st_folium(m, width=1200)