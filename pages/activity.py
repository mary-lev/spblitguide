import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Particiation",
    page_icon="👋",
)

st.write("# Events' Frequency")

df = pd.read_csv("data/event_frequency.csv")

# Assuming 'date' column is of string type, convert it to datetime
df['date'] = pd.to_datetime(df['date'])

# Now set 'date' as the index
df.set_index('date', inplace=True)

yearly_events = df.resample('Y').size()

# Convert to DataFrame
yearly_events_df = yearly_events.reset_index(name='event_count')

# Set 'date' as the index again
yearly_events_df.set_index('date', inplace=True)

st.line_chart(yearly_events_df)