from more_itertools import pairwise, windowed
from itertools import combinations
from collections import deque

def triplets(seq):
    return windowed(seq, 3)

def get_triplet_type(node_triplet, graph):
    assert len(node_triplet) == 3, node_triplet
    kinds = {(True, True): "chain",
             (True, False): "collider",
             (False, True): "fork",
             (False, False): "chain"}
            
    directions = tuple((f, t) in graph.edges for f, t in pairwise(node_triplet))
    return kinds[directions]
    
def is_blocked(path, Z, G):
    crit_1 = any(get_triplet_type(triplet, G) in ("chain", "fork") and triplet[1] in Z
                 for triplet in triplets(path))
    colliders = (triplet[1] for triplet in triplets(path) if get_triplet_type(triplet, G) == "collider")
    crit_2 = any(b in Z or any(z in G.successors(b) for z in Z)
                 for b in colliders)
    return crit_1 or crit_2

def is_d_separated(X, Y, Z, G):
    paths = nx.all_simple_paths(G.to_undirected(), X, Y)
    return all(is_blocked(path, Z, G) for path in paths)

def is_opened(node, Z, G):
    successors = set(G.successors(node))
    return bool(Z & successors)

def opened_checker(Z, G):
    memo = {}
    def f(node):
        if node in memo:
            return memo[node]
        value = any(f(n) for n in G.neighbors(node))
        memo[node] = value
        return value
    return f

def _check_colliders(colliders, Z, G):
    stack = colliders.copy()
    while stack:
        node = stack.pop()
        if node in Z:
            return False
        stack |= set(G.neighbors(node))
    print("#", colliders, Z)
    return True


def all_closed(path_starts, Y, Z, G):
    uG = G.to_undirected()
    stack = path_starts
    is_opened = opened_checker(Z, G)
    while stack:
        triplet, colliders, visited = stack.pop()
        t = get_triplet_type(triplet, G)
        if t in ("chain", "fork") and triplet[1] in Z:
            continue
        if t == "collider" and triplet[1] not in Z:
            colliders = colliders+[triplet[1]]
        if triplet[2] == Y:
            if all(is_opened(collider) for collider in colliders):
                return False
            continue

        stack.extend(((triplet[1], triplet[2], n), colliders, visited | {triplet[2]})
                     for n in uG.neighbors(triplet[2]) if n not in visited)
    return True

def is_d_separated_fast(X, Y, Z, G):
    uG = G.to_undirected()
    visited = {X}
    stack = [((X, n, nn), [], visited | {n}) for n in uG.neighbors(X)
             for nn in uG.neighbors(n) if n != Y and nn not in visited]
    all_colliders = set()
    return all_closed(stack, Y, Z, G)
# _check_colliders(all_colliders, Z, G)

def brute_force_find_separation(X, Y, G, nodes=None):
    if nodes is None:
        nodes = set(G.nodes)-{X, Y}
    subsets = (set(comb) for i in range(len(nodes)+1) for comb in combinations(nodes, i))
    separators = (Z for Z in subsets if is_d_separated_fast(X, Y, Z, G))
    return separators

