import folium
from folium.plugins import HeatMap
from streamlit_folium import st_folium
import streamlit as st
import pandas as pd

from st_pages import show_pages_from_config

show_pages_from_config()

# Load data
chart_data = pd.read_csv("data/amount_year.csv")

# Setup Streamlit session state for year
if 'year' not in st.session_state:
    st.session_state.year = 1999

# Button to update the year
if st.button('Next Year'):
    if st.session_state.year < 2019:
        st.session_state.year += 1
    else:
        st.session_state.year = 1999

# Select the year
selected_year = st.session_state.year
st.write(f"Displaying Heatmap for the year: {selected_year}")

# Filter data for the selected year
yearly_data = chart_data[chart_data['year'] == selected_year]

# Create a Folium map
m = folium.Map(location=[59.94, 30.35], zoom_start=12)

# Create a heatmap with the yearly data
heatmap = HeatMap(yearly_data[['lat', 'lon', 'event_count']].values, radius=10, blur=5, max_zoom=13)
heatmap.add_to(m)

# Display the map in Streamlit
st_folium(m, width=1200)
