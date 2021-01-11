from .fixtures import figure_2_9
from itertools import combinations
from caupy.path import brute_force_find_separation

def test_2_4_1_1(figure_2_9):
    pairs = [(a, b) for a, b in combinations(figure_2_9.nodes, 2)]
    non_adjacent = ((a, b) for a, b in pairs if a not in figure_2_9.neighbors(b) and b not in figure_2_9.neighbors(a))
    print({(a, b): next(brute_force_find_separation(a, b, figure_2_9), None)
           for a, b in non_adjacent})

def test_2_4_1_2(figure_2_9):
    measurable_nodes = {"Z_3", "W", "X", "Z_1"}
    pairs = [(a, b) for a, b in combinations(figure_2_9.nodes, 2)]
    non_adjacent = ((a, b) for a, b in pairs if a not in figure_2_9.neighbors(b) and b not in figure_2_9.neighbors(a))
    print({(a, b): next(brute_force_find_separation(a, b, figure_2_9, measurable_nodes), None)
           for a, b in non_adjacent})
    
    
