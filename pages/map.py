import streamlit as st
from streamlit_folium import st_folium
import pandas as pd
import folium
from folium.plugins import MarkerCluster

from st_pages import show_pages_from_config, add_page_title

#add_page_title()

show_pages_from_config()

st.write("""
        # Mapping the Saint-Petersburg's Literary Space
        ## Geographical Distribution of Literary Events in Saint-Petersburg (1999-2019)
        This map provides a visual representation of the various locations in Saint-Petersburg where literary events were held between the years 1999 and 2019. Each marker on the map denotes a unique location where one or more of these events took place. By clustering the markers, it offers a clear view of areas with higher concentrations of literary activities. Clicking on a marker reveals the name of the venue at that particular location. The underlying data is sourced from a curated database, offering insights into the spatial distribution of literary culture in Saint-Petersburg over two decades. The map is rendered using Folium, with the Stamen Toner tile layer providing a high-contrast, black and white basemap that accentuates the markers and clusters, making it easy to identify areas of notable literary activity.
        """
)

m = folium.Map(
    location=[59.946288, 30.349214],
    zoom_start=12,
    tiles="https://tiles.stadiamaps.com/tiles/stamen_toner/{z}/{x}/{y}.jpg?access_token={st.secrets.access_token}",
    attr="Mapbox attribution",
)

marker_cluster = MarkerCluster().add_to(m)

data = st.cache_data(pd.read_csv)("data/addresses.csv")

for n, adress in data.iterrows():
    text = adress['Place Name']
    folium.Marker(
        location=(adress['Latitude'], adress['Longitude']),
        popup=folium.Popup(text),
        icon=folium.Icon(color='green')
    ).add_to(marker_cluster)

st_data = st_folium(m, width=1200)