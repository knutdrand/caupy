from .fixtures import * 
from caupy.backdoor import brute_force_find_backdoor

def test_3_3_1_1(figure_3_8):
    res = brute_force_find_backdoor("X", "Y", figure_3_8)
    print(list(res))
    assert False
