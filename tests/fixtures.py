import pytest
import networkx as nx

@pytest.fixture
def figure_2_9():
    G = nx.DiGraph()
    G.add_nodes_from(["Z_1", "Z_2", "Z_3",
                      "X", "W", "Y"])
    G.add_edges_from([("Z_1", "Z_3"),
                      ("Z_2", "Z_3"),
                      ("Z_1", "X"),
                      ("Z_2", "Y"),
                      ("Z_3", "X"),
                      ("Z_3", "Y"),
                      ("X", "W"),
                      ("W", "Y")])
    return G
                      
    
@pytest.fixture
def figure_3_8():
    G = nx.DiGraph()
    G.add_nodes_from(list("ABCDXYZW"))
    G.add_edges_from([("B", "A"),
                      ("B", "Z"),
                      ("C", "D"),
                      ("C", "Z"),
                      ("A", "X"),
                      ("D", "Y"),
                      ("Z", "X"),
                      ("Z", "Y"),
                      ("X", "W"),
                      ("W", "Y")])
    return G 
    
                     
