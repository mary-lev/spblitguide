import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
from st_pages import show_pages_from_config, add_page_title

add_page_title()

show_pages_from_config()

st.write("""
        # Mapping the Saint-Petersburg's Literary Space
        ## Visual Representation of Event Frequency at Various Locations in Saint-Petersburg
        This interactive map offers a three-dimensional view of the frequency of literary events held at various locations across Saint-Petersburg. Each column represents a unique location, and the height of the column corresponds to the number of events that took place at that location. The color intensity of the columns also corresponds to the event frequency, providing a dual-visual cue to easily identify areas with higher concentrations of literary activities. The tooltip feature provides the exact name of the location and the number of events when hovered over each column, giving more detailed information. The map employs a pitch perspective to provide a three-dimensional view, making it easier to interpret the spatial distribution and frequency of events. Through this visualization, users can quickly grasp the hubs of literary activity across the city and identify notable venues by their event frequency.
        """
)

chart_data = pd.read_csv("data/amount.csv")

tooltip = {
    "html": "<b>{event__place__name}</b>: {event_count} events",
    "style": {"background": "grey", "color": "white", "font-family": '"Helvetica Neue", Arial', "z-index": "10000"},
}

st.pydeck_chart(pdk.Deck(
    map_style=None,
    tooltip=tooltip,
    initial_view_state=pdk.ViewState(
        latitude=59.94,
        longitude=30.35,
        zoom=12,
        pitch=50,
    ),
    layers=[
        pdk.Layer(
    "ColumnLayer",
    data=chart_data,
    get_position=["lon", "lat"],
    get_elevation="event_count",
    elevation_scale=1,
    radius=50,
    get_fill_color=["event_count * 10", "event_count", "event_count * 10", 140],
    pickable=True,
    auto_highlight=True,
)
    ],
))
