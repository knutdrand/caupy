import networkx as nx
from itertools import combinations
from .path import all_closed


def find_backdoor_path(X, Z, G):
    into_x = [n for n in uG.neighbors(X) if X in G.neighbors(n) if n != Y]
    stack = [((X, n, nn), visited | {n}) for n in into_x for nn in uG.neighbors(n)
             if nn not in visited]
    while stack:
        triplet, visited = stack.pop()
        t = get_triplet_type(triplet, G)
        if t == "collider":
            continue
        if triplet[-1] in Z:
            return True
        stack.extend(((triplet[1], triplet[2], n) for n in G.neighbors
    return False

def is_frontdoor(X, Y, Z, G):
    directed_paths = nx.all_simple_paths(G, X, Y)
    if not all(Z & set(path) for path in directed_paths):
        return False

def brute_force_find_backdoor(X, Y, G, nodes=None):
    if nodes is None:
        nodes = set(G.nodes)-{X, Y}
    subsets = (set(comb) for i in range(len(nodes)+1) for comb in combinations(nodes, i))
    separators = (Z for Z in subsets if is_backdoor(X, Y, Z, G))
    return separators
