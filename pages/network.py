import streamlit as st
from st_pages import show_pages_from_config, add_page_title

import networkx
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine
from bokeh.plotting import from_networkx
import bokeh.palettes
from bokeh.palettes import Blues8, Reds8, Purples8, Oranges8, Viridis8, Spectral8

add_page_title()

show_pages_from_config()

st.write("This graph visualizes the co-participation of individuals in events and highlights identified communities within the literary network.")

df = pd.read_json("data/cooccurrence_list.json")
df.columns = ["Source", "Target", "Weight"]

G = networkx.from_pandas_edgelist(df, 'Source', 'Target', 'Weight')
degrees = dict(networkx.degree(G))
networkx.set_node_attributes(G, name='degree', values=degrees)
number_to_adjust_by = 5
adjusted_node_size = dict([(node, degree+number_to_adjust_by) for node, degree in networkx.degree(G)])
networkx.set_node_attributes(G, name='adjusted_node_size', values=adjusted_node_size)

from networkx.algorithms import community
communities = community.greedy_modularity_communities(G)

palette = bokeh.palettes.all_palettes['Category20'][20]
# Create empty dictionaries
modularity_class = {}
modularity_color = {}
#Loop through each community in the network
for community_number, community in enumerate(communities):
    #For each member of the community, add their community number and a distinct color
    for name in community: 
        modularity_class[name] = community_number
        modularity_color[name] = palette[community_number]

# Add modularity class and color as attributes from the network above
networkx.set_node_attributes(G, modularity_class, 'modularity_class')
networkx.set_node_attributes(G, modularity_color, 'modularity_color')

#Choose attributes from G network to size and color by — setting manual size (e.g. 10) or color (e.g. 'skyblue') also allowed
size_by_this_attribute = 'adjusted_node_size'
color_by_this_attribute = 'modularity_color'
#Pick a color palette — Blues8, Reds8, Purples8, Oranges8, Viridis8
color_palette = Viridis8
#Choose a title!
title = 'Literary Network'

#Establish which categories will appear when hovering over each node
HOVER_TOOLTIPS = [
       ("Character", "@index"),
        ("Degree", "@degree"),
         ("Modularity Class", "@modularity_class"),
        ("Modularity Color", "$color[swatch]:modularity_color"),
]

#Create a plot — set dimensions, toolbar, and title
plot = figure(tooltips = HOVER_TOOLTIPS,
              tools="pan,wheel_zoom,save,reset, tap", active_scroll='wheel_zoom',
            x_range=Range1d(-10.1, 10.1), y_range=Range1d(-10.1, 10.1), title=title)

#Create a network graph object
# https://networkx.github.io/documentation/networkx-1.9/reference/generated/networkx.drawing.layout.spring_layout.html
network_graph = from_networkx(G, networkx.fruchterman_reingold_layout, scale=20, center=(0, 0))

#Set node sizes and colors according to node degree (color as category from attribute)
network_graph.node_renderer.glyph = Circle(size=size_by_this_attribute, fill_color=color_by_this_attribute)

#Set edge opacity and width
network_graph.edge_renderer.glyph = MultiLine(line_alpha=0.5, line_width=1)

plot.renderers.append(network_graph)


st.bokeh_chart(plot, use_container_width=True)