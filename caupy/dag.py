import networkx as nx
G  = nx.DiGraph()
G.add_nodes_from(["X", "Y", "Z"])
G.add_edges_from([("X", "Y"), ("X", "Z")])
print(G.nodes)
