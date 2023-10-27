import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium

import streamlit as st
import pandas as pd
import pydeck as pdk
from st_pages import show_pages_from_config, add_page_title

#add_page_title()

show_pages_from_config()

st.write("""
        # Mapping the Saint-Petersburg's Literary Space
        ## Heat Map of Event Frequency at Various Locations in Saint-Petersburg
        The provided heatmap vividly showcases the frequency of literary events that transpired across various locations in Saint-Petersburg. Using color intensity to indicate the prevalence of events, the heatmap allows for a straightforward visual interpretation of areas with higher literary activity.
        """
)

chart_data = pd.read_csv("data/amount.csv")


m = folium.Map(
    location=[59.94, 30.35],
    zoom_start=12,
    tiles="https://tiles.stadiamaps.com/tiles/stamen_toner/{z}/{x}/{y}.jpg",
    attr="Mapbox attribution",
)

heatmap = HeatMap(
    data=chart_data[['lat', 'lon', 'event_count']].values,
    radius=10,
    blur=5,
    max_zoom=13,
)

heatmap.add_to(m)

st_data = st_folium(m, width=1200)

st.write("The darker areas on the map signify regions with a higher frequency of events, thus indicating hotspots of literary activity within the city. This visual representation aids in identifying zones of significant literary engagement, which could be invaluable for researchers and the general public interested in the literary landscape of Saint-Petersburg.")