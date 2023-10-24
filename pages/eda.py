import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Exploratory Data Analysis",
    page_icon="👋",
)

st.write("# Exploratory! Data Analysis 👋")

df = pd.read_csv("data/event_frequency.csv")

yearly_events = df.resample('Y').size()

# Convert to DataFrame
yearly_events_df = yearly_events.reset_index(name='event_count')

st.line_chart(yearly_events_df)