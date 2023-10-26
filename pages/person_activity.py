import pandas as pd
import streamlit as st
import altair as alt
import numpy as np

from st_pages import show_pages_from_config, add_page_title

add_page_title()

show_pages_from_config()

# People activity
df = pd.read_csv("data/person_activity.csv")

st.write("""
    # Exploratory Data Analysis
    ## Distribution of Event Participation (Log Scale)
    This histogram illustrates the distribution of individuals based on the number of events they have participated in, on a logarithmic scale. The x-axis represents the number of events participated, ranging from 1 to the maximum event count observed in the dataset. The y-axis represents the frequency of individuals, in a logarithmic scale, who have participated in a particular number of events. Utilizing a log scale for the frequency helps in better visualizing the distribution, especially when dealing with a wide range of frequency values. Each bar represents the count of individuals who have participated in a particular number of events. This visualization provides an insight into the frequency of event participation among individuals, enabling a better understanding of participation patterns.
    """
)
# Log Scale:
count, bins = np.histogram(df['event_count'], bins=range(1, df['event_count'].max() + 1))
count[count == 0] = 1
log_count = np.log(count)

# Convert to DataFrame
hist_df = pd.DataFrame({
    'Number of Events Participated': bins[:-1],  # excluding the last bin edge
    'Log(Frequency)': log_count
})

# Remove entries where count is 0 to avoid log(0)
hist_df = hist_df[hist_df['Log(Frequency)'] > 0]

# Display the chart in Streamlit
st.bar_chart(hist_df.set_index('Number of Events Participated'))




st.write("""
    ## Distribution of Persons by Event Participation Bins
    This chart visualizes the distribution of individuals based on the number of events they have participated in. The data is grouped into bins of event counts: '2-5', '6-10', '11-20', '21-50', and '>50'. Each bar represents the count of individuals who fall within the respective event participation range. The x-axis denotes the event participation bins, while the y-axis represents the count of individuals. Through this visualization, it's apparent how many individuals are frequent participants (engaging in numerous events) versus those who participate less often. This chart provides insights into the level of engagement of individuals in events, which could be useful for understanding participant behavior.
    """
)

# Load your data
df_filtered = df[df['event_count'] > 1]

# Create bins
bins = [2, 5, 10, 20, 50, 300]  # The last bin will cover values greater than 50
labels = ['2-5', '6-10', '11-20', '21-50', '>50']
df_filtered['event_count_bin'] = pd.cut(df_filtered['event_count'], bins=bins, labels=labels, right=False)

# Now, to get the count of persons in each bin, you can use the groupby and count functions:
bin_counts = df_filtered.groupby('event_count_bin').size().reset_index(name='count')

# Now create the chart
chart = (
    alt.Chart(bin_counts)
    .mark_bar()
    .encode(
        x=alt.X('event_count_bin:O', title='Number of Events Participated (Bins)', sort=labels),  # Specify the sort order here
        y=alt.Y('count:Q', title='Number of Persons')
    )
    .properties(
        #title='Distribution of Persons by Event Participation Bins',
        width=600,
        height=400
    )
)

st.altair_chart(chart)