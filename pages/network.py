import streamlit as st
from st_pages import show_pages_from_config, add_page_title

import networkx
import pandas as pd
from bokeh.plotting import figure
from bokeh.models import Range1d, Circle, ColumnDataSource, MultiLine
from bokeh.plotting import from_networkx
import bokeh.palettes
from bokeh.palettes import Blues8, Reds8, Purples8, Oranges8, Viridis8, Spectral8

import altair as alt

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

## Metrics and Measures

degree_centrality = networkx.degree_centrality(G)


# Sort nodes by degree centrality in descending order
sorted_nodes_by_centrality = sorted(degree_centrality.items(), key=lambda item: item[1], reverse=True)

# Select the top ten nodes
top_ten_nodes = sorted_nodes_by_centrality[:10]

st.subheader("Degree Centrality: ")
# Print the top ten nodes along with their centrality values
st.write("Top ten nodes by degree centrality:")
for node, centrality in top_ten_nodes:
    st.write(f"{node}: {centrality}")


closeness_centrality = networkx.closeness_centrality(G)
sorted_nodes_by_closeness_centrality = sorted(closeness_centrality.items(), key=lambda item: item[1], reverse=True)
top_ten_nodes = sorted_nodes_by_closeness_centrality[:10]

st.subheader("Closeness Centrality: ")
st.write("Closeness centrality is a measure of how close a node is to all other nodes in a network. It's based on the average length of the shortest path from the node to all other nodes in the graph. The idea is to identify how easily a node can reach other nodes in the network.")
st.write("Top ten nodes by closeness centrality:")
for node, centrality in top_ten_nodes:
    st.write(f"{node}: {centrality}")

betweenness_centrality = networkx.betweenness_centrality(G)
sorted_nodes_by_betweenness_centrality = sorted(betweenness_centrality.items(), key=lambda item: item[1], reverse=True)
top_ten_nodes = sorted_nodes_by_betweenness_centrality[:10]

st.subheader("Betweenness Centrality: ")
st.write("Betweenness centrality is a measure of how often a node acts as a bridge along the shortest path between two other nodes in a network. It's based on the number of shortest paths that pass through the node.")
st.write("Top ten nodes by betweenness centrality:")
for node, centrality in top_ten_nodes:
    st.write(f"{node}: {centrality}")

eigenvector_centrality = networkx.eigenvector_centrality(G)
sorted_nodes_by_eigenvector_centrality = sorted(eigenvector_centrality.items(), key=lambda item: item[1], reverse=True)
top_ten_nodes = sorted_nodes_by_eigenvector_centrality[:10]
st.subheader("Eigenvector Centrality: ")
st.write("Eigenvector centrality is a measure of the influence of a node in a network. It's based on the idea that connections to high-scoring nodes contribute more to the score of the node in question.")
st.write("Top ten nodes by eigenvector centrality:")
for node, centrality in top_ten_nodes:
    st.write(f"{node}: {centrality}")

pagerank = networkx.pagerank(G)
sorted_nodes_by_pagerank = sorted(pagerank.items(), key=lambda item: item[1], reverse=True)
top_ten_nodes = sorted_nodes_by_pagerank[:10]
st.subheader("PageRank: ")
st.write("PageRank is a measure of the importance of a node in a network. It's based on the idea that connections to high-scoring nodes contribute more to the score of the node in question.")
st.write("Top ten nodes by PageRank:")
for node, centrality in top_ten_nodes:
    st.write(f"{node}: {centrality}")

clustering_coefficient = networkx.clustering(G)
sorted_nodes_by_clustering_coefficient = sorted(clustering_coefficient.items(), key=lambda item: item[1], reverse=True)
top_ten_nodes = sorted_nodes_by_clustering_coefficient[:10]
st.subheader("Clustering Coefficient: ")
st.write("Clustering coefficient is a measure of the degree to which nodes in a network tend to cluster together. It's based on the number of triangles in the network.")
st.write("Top ten nodes by clustering coefficient:")
for node, centrality in top_ten_nodes:
    st.write(f"{node}: {centrality}")

average_clustering = networkx.average_clustering(G)
st.subheader("Average Clustering: ")
st.write("Average clustering is a measure of the degree to which nodes in a network tend to cluster together. It's based on the number of triangles in the network.")
st.write(average_clustering)
st.write("This value suggests a moderate to high level of clustering within the network. It indicates that there's a significant tendency for nodes to form tightly knit groups characterized by relatively dense connections. In practical terms, nodes (or individuals, if this is a social network) tend to form close-knit communities or groups where each member is likely to be connected to many other members within the same group.")


diameter = networkx.diameter(G)
density = networkx.density(G)


st.write("Diameter: ", diameter)
st.write("The diameter of a network is the longest shortest path between any two nodes. A diameter of 4 in this context means that the furthest distance between any two nodes in the network is four edges. This relatively small diameter indicates that the network is quite compact; information or anything else flowing through the network can reach from one end to the other in a small number of steps. It suggests that despite any clustering, the network remains relatively efficient in terms of information dissemination or the spread of influence.")
st.write("Density: ", density)
st.write("Network density is the ratio of actual edges in the network to the total possible number of edges. The density value provided here indicates a low to moderate level of overall connectivity among the nodes in the network. This suggests that while there are some connections between nodes, the network is not overly saturated with links. There is room for more connections to be made, and not every node is directly connected to every other node, which is typical for larger or more complex networks.")

st.write("In summary, the network is characterized by a good level of local clustering, indicating the presence of community-like structures. Its compactness is highlighted by a small diameter, suggesting efficient pathways for communication or diffusion across the network. However, the network's relatively low density points to a selective pattern of connections, meaning that while there are focused areas of connectivity (e.g., within clusters), the network as a whole is not fully connected, maintaining a balance between cohesion and dispersion.")



st.subheader("Analysing network communities")
from networkx.algorithms import community
communities = community.greedy_modularity_communities(G)

modularity = community.modularity(G, communities)
coverage, performance = community.partition_quality(G, communities)

st.write("Modularity: ", modularity)
st.write("Modularity is a measure of the structure of networks or graphs which measures the strength of division of a network into modules (also called groups, clusters or communities). Networks with high modularity have dense connections between the nodes within modules but sparse connections between nodes in different modules.")
st.write(f"A modularity score of {modularity} indicates that the partitioning of the graph into communities is somewhat significant. Modularity measures the strength of division of a network into modules (or communities). A modularity score closer to 1 indicates a strong community structure, while a score close to 0 suggests a random structure.")

st.write("Coverage: ", coverage)
st.write("The coverage of a partition is the ratio of the number of intra-community edges to the total number of edges in the graph.")
st.write(f"A coverage score of {coverage} indicates that approximately {coverage} of the edges in the graph are within communities. A higher coverage suggests that there are relatively more edges within communities compared to between communities. This aligns with the notion of strong community structures within the graph.")

st.write("Performance: ", performance)
st.write("The performance of a partition is the number of intra-community edges plus inter-community non-edges divided by the total number of potential edges.")
st.write(f"A performance score of {performance} suggests that a significant portion of potential edges in the graph are realized either as intra-community edges or as inter-community non-edges. Higher performance values indicate better partitioning quality in terms of capturing both within-community cohesion and between-community separation.")

st.subheader("Analysing network measures by communities")

subgraphs = []
for i in range(len(communities)):
    nodes = (
        node
        for node, data
        in G.nodes(data=True)
        if data.get("modularity_class") == i
    )
    subgraphs.append(G.subgraph(nodes))

for i in range(len(subgraphs)):
    st.subheader(f"Community {i}")
    st.write("Average Clustering: ", networkx.average_clustering(subgraphs[i]))
    st.write("Diameter: ", networkx.diameter(subgraphs[i]))
    st.write("Density: ", networkx.density(subgraphs[i]))



source = pd.DataFrame({
    'Community label': [f"{i}" for i in range(len(subgraphs))],
    'Average Clustering': [networkx.average_clustering(subgraph) for subgraph in subgraphs]
})
base = alt.Chart(source)
chart = base.mark_bar().encode(
    x='Community label',
    y='Average Clustering'
).properties(
        title='Average Clustering by Community',
        width=600,
        height=400
    )
rule = base.mark_rule(color='red').encode(
    y=alt.Y(datum=networkx.average_clustering(G))
)
label = rule.mark_text(
    align="right",
    baseline="bottom",
    text="Average Clustering for the whole network",
    color='red'
)
st.altair_chart(chart+rule+label)


source = pd.DataFrame({
    'Community label': [f"{i}" for i in range(len(subgraphs))],
    'Diameter': [networkx.diameter(subgraph) for subgraph in subgraphs]
})

base = alt.Chart(source)
chart = base.mark_bar().encode(
    x='Community label',
    y='Diameter'
).properties(
        title='Diameter by Community',
        width=600,
        height=400
    )
rule = base.mark_rule(color='red').encode(
    y=alt.Y(datum=diameter)
)

label = rule.mark_text(
    align="right",
    baseline="bottom",
    text="Diameter for the whole network",
    color='red'
)

st.altair_chart(chart+rule+label)


source = pd.DataFrame({
    'Community label': [f"{i}" for i in range(len(subgraphs))],
    'Density': [networkx.density(subgraph) for subgraph in subgraphs]
})

base = alt.Chart(source)
chart = base.mark_bar().encode(
    x='Community label',
    y='Density'
).properties(
        title='Density by Community',
        width=600,
        height=400
    )
rule = base.mark_rule(color='red').encode(
    y=alt.Y(datum=density)
)

label = rule.mark_text(
    align="right",
    baseline="bottom",
    text="Density for the whole network",
    color='red'
)

st.altair_chart(chart+rule+label)