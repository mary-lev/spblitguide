import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk

st.write("# Mapping the Saint-Petersburg's Literary Space")

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
