import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import folium
from folium.plugins import MarkerCluster


st.write("# Mapping the Saint-Petersburg's Literary Space")

data = st.cache_data(pd.read_csv)("data/addresses.csv")

m = folium.Map(location=[59.946288, 30.349214], zoom_start=12, tiles='Stamen Toner')

marker_cluster = MarkerCluster().add_to(m)

for n, adress in data.iterrows():
    text = adress['event__place__name']
    folium.Marker(
        location=(adress['lat'], adress['lon']),
        popup=folium.Popup(text),
        icon=folium.Icon(color='green')
    ).add_to(marker_cluster)

st_data = st_folium(m, width=1200)