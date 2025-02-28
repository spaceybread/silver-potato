import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Read the edge list from the provided file
file_path = "graph_n4.md"
with open(file_path, "r") as f:
    edges = [line.strip().split() for line in f.readlines()]

# Create a directed graph
G = nx.DiGraph()

# Add edges with weights
for edge in edges:
    node1, node2, weight = edge
    G.add_edge(node1, node2, weight=int(weight))
    G.add_edge(node2, node1, weight=int(weight))
# Define a lattice layout manually (e.g., based on Hamming distance or ordering)
nodes = sorted(G.nodes())
positions = {}
n = int(np.ceil(np.sqrt(len(nodes))))  # Approximate square layout
for i, node in enumerate(nodes):
    positions[node] = (i % n, -i // n)  # Arrange in a grid

# Define edge colors based on weight
edge_colors = {2: 'blue', 3: 'green', 4: 'red'}
edge_styles = {2: 'solid', 3: 'dashed', 4: 'dotted'}

# Draw the graph
plt.figure(figsize=(10, 10))
ax = plt.gca()
for edge in G.edges(data=True):
    weight = edge[2]['weight']
    nx.draw_networkx_edges(G, positions, edgelist=[(edge[0], edge[1])], 
                           edge_color=edge_colors.get(weight, 'black'), 
                           style=edge_styles.get(weight, 'solid'), ax=ax)

nx.draw_networkx_nodes(G, positions, node_color='lightgray', node_size=500)
nx.draw_networkx_labels(G, positions, font_size=8)
plt.title("Lattice Representation of Graph")
plt.show()
