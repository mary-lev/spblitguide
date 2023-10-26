import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Participation",
    page_icon="👋",
)

st.write("""
    # Exploratory Data Analysis
    ## Monthly Event Frequency Over the Years
    A comparative visualization of the monthly distribution of events over different years. 
    Each bar represents the count of events that occurred in a particular month of a specific year. 
    """
)

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
pivot_table.sort_index(axis=1, ascending=True, inplace=True)

st.bar_chart(pivot_table)

st.write("""
    ### Key Observations:
    - Seasonal Trends: The chart may reflect any seasonal trends in event frequencies. For instance, certain months may consistently show higher or lower event occurrences over the years.
    - Yearly Comparison: It allows for a quick comparison of event frequency between different years on a month-by-month basis.
    - Month-wise Distribution: The month-wise distribution of events is clearly depicted, allowing for an analysis of which months are most active with events.
    - Variation Across Years: Any significant variations in event frequency across years are visually evident. This could be due to various external factors affecting the occurrence of events.
    """
)



# Places participants
df = pd.read_csv("data/events_participation.csv")
grouped_data = df.groupby(['place_name', 'participant_count']).size().reset_index(name='occurrences')

# Find the most frequent participant count per place
idx = grouped_data.groupby(['place_name'])['occurrences'].idxmax()
most_frequent_data = grouped_data.loc[idx]

sns.set_style("whitegrid")
plt.figure(figsize=(10, 6))
sns.barplot(data=most_frequent_data, x='place_name', y='participant_count', hue='place_name', palette='viridis')
plt.xticks(rotation=90)  # Rotate x labels for better readability
plt.title('Most Frequent Participant Count per Place')
plt.xlabel('Place')
plt.ylabel('Participant Count')
plt.legend().remove() 
st.pyplot(plt)