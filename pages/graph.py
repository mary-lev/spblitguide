import json
from pyvis.network import Network
import streamlit as st
import streamlit.components.v1 as components
from st_pages import show_pages_from_config, add_page_title

add_page_title()

show_pages_from_config()

st.write("""
    The network graph vividly captures the interactions and connections between literary actors in Saint-Petersburg, based on their joint participation in events during the year 2004. Each node represents a unique literary actor, while each edge signifies the presence of a collaborative event. The strength and frequency of collaborations are represented by the thickness of the edges, providing a clear visual cue for understanding the intensity of interactions between different actors.
    """
)

HtmlFile = open(f'data/events2014.html', 'r', encoding='utf-8')

# Load HTML file in HTML component for display on Streamlit page
components.html(HtmlFile.read(), height=700)

st.write("""
    This visualization adopts the Force Atlas 2 algorithm, which spatially distributes the nodes in a way that visually separates clusters of highly interconnected actors from less connected ones. As a result, clusters of literary actors who frequently collaborate in events are brought into focus, revealing the core networks of interaction within the broader literary community.
    Through this network graph, users can delve into the collaborative landscape of the literary scene, identifying key players, emergent clusters, and the overall structure of interactions. This visualization serves as an insightful tool for exploring the dynamics of literary collaborations and understanding the social fabric binding the literary community in Saint-Petersburg during 2004.
    Moreover, the interactive nature of the network graph allows users to hover over nodes and edges to obtain detailed information about the actors and their collaborative engagements, making this a rich and engaging resource for exploring the literary network.
    """
)
