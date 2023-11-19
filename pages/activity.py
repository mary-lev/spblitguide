import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from st_pages import show_pages_from_config, add_page_title

add_page_title()

show_pages_from_config()

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


st.write("""
    ### Weekday Event Distribution Analysis:
         """)
import seaborn as sns
import matplotlib.pyplot as plt

df['weekday'] = df['date'].dt.day_name()

# Map weekdays to the order you want them to appear in the chart
weekday_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
df['week_day_name'] = pd.Categorical(df['weekday'], categories=weekday_order, ordered=True)

df['year'] = df['date'].dt.year

# Group by 'year' and 'week_day_name', then count the number of events
event_counts = df.groupby(['year', 'week_day_name'], observed=True).size().reset_index(name='event_count')

# Create a box plot of event counts for each weekday across different years
plt.figure(figsize=(10, 6))
sns.boxplot(x='week_day_name', y='event_count', hue="week_day_name", data=event_counts, palette="Set2")
plt.title('Event Frequency by Weekday Across Years')
plt.xlabel('Day of the Week')
plt.ylabel('Number of Events')
plt.xticks(rotation=45)


# Display the plot
st.pyplot(plt)

st.write("""
    - The box plot shows the spread and central tendency of event counts across different weekdays.
    - Look for outliers to identify unusually busy or quiet days.
    - The median line in each box indicates the typical number of events for each weekday.
    - Variability in the box size and whisker length can reveal consistency in event scheduling.
    """
)
