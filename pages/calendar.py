import streamlit as st
from streamlit_calendar import calendar


year = st.selectbox(
    "Select a year:",
    (
        [year for year in range(1999, 2020)]
    ),
)

calendar_options = {
    "headerToolbar": {
        "left": "prev,next",
        "center": "title",
    },
    "slotMinTime": "09:00:00",
    "slotMaxTime": "23:00:00",
    "initialView": "dayGridMonth",
    "navLinks": True
    
}
calendar_events = [
    {
        "title": "Event 1",
        "start": "2023-07-31T08:30:00",
        "end": "2023-07-31T10:30:00",
    },
    {
        "title": "Event 2",
        "start": "2023-07-31T07:30:00",
        "end": "2023-07-31T10:30:00",
    },
    {
        "title": "Event 3",
        "start": "2023-07-31T10:40:00",
        "end": "2023-07-31T12:30:00",
    }
]
custom_css="""
    .fc-event-past {
        opacity: 0.8;
    }
    .fc-event-time {
        font-style: italic;
    }
    .fc-event-title {
        font-weight: 700;
    }
    .fc-toolbar-title {
        font-size: 2rem;
    }
"""

calendar = calendar(events=calendar_events, options=calendar_options, custom_css=custom_css)
st.write(calendar)