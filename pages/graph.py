import json
from pyvis.network import Network
import streamlit as st
import streamlit.components.v1 as components
from st_pages import show_pages_from_config, add_page_title

add_page_title()

show_pages_from_config()

st.title('Literary Network')

HtmlFile = open(f'data/events2014.html', 'r', encoding='utf-8')

# Load HTML file in HTML component for display on Streamlit page
components.html(HtmlFile.read(), height=700)
