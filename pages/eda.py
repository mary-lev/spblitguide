import streamlit as st
import pandas as pd

from st_pages import show_pages_from_config, add_page_title

add_page_title()

show_pages_from_config()

st.write("# Exploratory! Data Analysis 👋")

df = pd.read_csv("data/event_frequency.csv")

yearly_events = df.resample('Y').size()

# Convert to DataFrame
yearly_events_df = yearly_events.reset_index(name='event_count')

st.line_chart(yearly_events_df)