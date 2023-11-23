import streamlit as st
import pandas as pd

from st_pages import show_pages_from_config, add_page_title

add_page_title()

show_pages_from_config()

def update():
    st.session_state.df = st.session_state.edited_df.copy()
    st.session_state.df.to_csv("data/example.csv", index=False)


df = pd.read_csv("data/example.csv")


# Initialize session state with dataframes
# Include initialization of "edited" slots by copying originals
if 'df' not in st.session_state:
    st.session_state.df = pd.read_csv("data/example.csv")

st.session_state.edited_df = st.data_editor(
    df,
    use_container_width=True,
    disabled=("place_name", "date", "id"),
    column_config={
        "address_latitude": None,
        "address_longitude": None,
        "address": None,
        "description": st.column_config.Column(
            "description",
            help="help",
            required=True,
        ),
    },
    hide_index=True,
)

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True


st.button('Save changes', on_click=click_button)

if st.session_state.clicked:
    update()
    # The message and nested widget will remain on the page
    st.write('Saved!')

