import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Participation",
    page_icon="👋",
)

st.write("# Exploratory Data Analysis: Events' Frequency")

df = pd.read_csv("data/event_frequency.csv")

# Assuming 'date' column is of string type, convert it to datetime
df['date'] = pd.to_datetime(df['date'])

# Create 'year' and 'month' columns from the 'date' column
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month

# Group by year and month, and count the number of events
monthly_counts = df.groupby(['year', 'month']).size().reset_index(name='event_count')

# Create a pivot table with years as columns, months as the index
pivot_table = monthly_counts.pivot(index='month', columns='year', values='event_count')

# Replace NaN values with 0 (assuming no events is equivalent to 0)
pivot_table.fillna(0, inplace=True)

# Map month numbers to month names
month_mapping = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 
                 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
pivot_table.index = pivot_table.index.map(month_mapping)

# Convert the index to a CategoricalIndex with the categories ordered by month number
pivot_table.index = pd.CategoricalIndex(pivot_table.index, categories=[month_mapping[i] for i in range(1, 13)], ordered=True)

# Now sort the index
pivot_table.sort_index(inplace=True)

st.bar_chart(pivot_table)

# People


import matplotlib.pyplot as plt

# Assume df is your DataFrame
df = pd.read_csv("data/person_activity.csv")

plt.figure(figsize=(10,6))
plt.hist(df['event_count'], bins=range(1, df['event_count'].max() + 1), color='skyblue', edgecolor='black')
plt.xlabel('Number of Events Participated')
plt.ylabel('Frequency')
plt.title('Distribution of Event Participation')
plt.grid(axis='y', linestyle='--', alpha=0.7)

st.pyplot(plt)

# Another one

summary = df['event_count'].describe()
st.write(summary)
plt.figure(figsize=(10,6))
plt.boxplot(df['event_count'])
plt.ylabel('Number of Events Participated')
plt.title('Box Plot of Event Participation')

st.pyplot(plt)