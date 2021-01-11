import networkx as nx
from itertools import combinations
from .path import all_closed

def is_backdoor(X, Y, Z, G):
    uG = G.to_undirected()
    if Z & set(G.successors(X)):
        return False
    visited = {X}
    into_x = [n for n in uG.neighbors(X) if X in G.neighbors(n) if n != Y]
    stack = [((X, n, nn), [], visited | {n}) for n in into_x for nn in uG.neighbors(n)
             if nn not in visited]

    return all_closed(stack, Y, Z, G)

def brute_force_find_backdoor(X, Y, G, nodes=None):
    if nodes is None:
        nodes = set(G.nodes)-{X, Y}
    subsets = (set(comb) for i in range(len(nodes)+1) for comb in combinations(nodes, i))
    separators = (Z for Z in subsets if is_backdoor(X, Y, Z, G))
    return separators
