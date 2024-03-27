import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
G.add_edge("A", "G", weight=5.0)
G.add_edge("A", "F", weight=3.0)
G.add_edge("A", "C", weight=1.0)
G.add_edge("C", "F", weight=5.0)
G.add_edge("C", "D", weight=1.0)
G.add_edge("D", "K", weight=5.0)
G.add_edge("K", "E", weight=5.0)
G.add_edge("K", "J", weight=7.0)
G.add_edge("J", "B", weight=3.0)
G.add_edge("B", "E", weight=5.0)
G.add_edge("B", "G", weight=11.0)
G.add_edge("F", "E", weight=3.0)

G.add_edge("G", "A", weight=5.0)
G.add_edge("F", "A", weight=3.0)
G.add_edge("C", "A", weight=1.0)
G.add_edge("F", "C", weight=5.0)
G.add_edge("D", "C", weight=1.0)
G.add_edge("K", "D", weight=5.0)
G.add_edge("E", "K", weight=5.0)
G.add_edge("J", "K", weight=7.0)
G.add_edge("B", "J", weight=3.0)
G.add_edge("E", "B", weight=5.0)
G.add_edge("G", "B", weight=11.0)
G.add_edge("E", "F", weight=3.0)

layout = nx.circular_layout(G)
labels2 = nx.get_edge_attributes(G,'weight')
nx.draw(G,layout,with_labels=True, node_color='#bb22bb', node_size=600)
nx.draw_networkx_edge_labels(G, layout, edge_labels=labels2)
plt.show()

rest = nx.dijkstra_path(G, source="A", target="J")

print(rest)


ruta = G.subgraph(['A','C','D','K','J'])
nx.draw(ruta,with_labels=True, node_size=600)

plt.show()