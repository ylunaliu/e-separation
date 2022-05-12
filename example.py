from platform import node
import networkx as nx
import numpy as np
import itertools
import matplotlib.pyplot as plt

graph_1 = nx.DiGraph()
graph_1.add_edges_from([("A", "D"), ("A", "C"),("C", "D"), ("B", "C")])
graph_1_hidden = list(["A"])
graph_1.remove_node("C")

graph_2 = nx.DiGraph()              
graph_2.add_edges_from([("B", "E"), ("A", "E"), ("A", "D"), ("C", "D")])
graph_2_hidden = list(["A"])
graph_2.remove_node("E")
graph_3 = nx.Graph()
graph_3.add_edges_from(graph_1.edges)


# nx.draw(graph_c)
# plt.show()
print(graph_2.nodes)

nx.draw(graph_3,with_labels=True)
plt.show()