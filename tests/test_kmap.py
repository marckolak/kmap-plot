from kmapplot.kmap import Kmap
from kmapplot.boolfunc import BooleanFunction

def test_kmap_shapes():
    kmap = Kmap(function=BooleanFunction(variable_names=[c for c in 'abcd']))
    assert(len(kmap) == 4 and len(kmap[0]) == 4)

    kmap = Kmap(function=BooleanFunction(variable_names=[c for c in 'abcd']), rows_n=3)
    assert(len(kmap) == 8 and len(kmap[0]) == 2)

    kmap = Kmap(function=BooleanFunction(variable_names=[c for c in 'abcd']), rows_n=1)
    assert(len(kmap) == 2 and len(kmap[0]) == 8)
