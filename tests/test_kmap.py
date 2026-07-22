from kmapplot.kmap import Kmap
def test_kmap_val_mapping():
    kmap = Kmap(variables_n=2)
    print(kmap)
    assert True

def test_kmap_shapes():
    kmap = Kmap(variables_n=2)
    print(kmap)
    assert(len(kmap) == 2 and len(kmap[0]) == 2)


def test_undefined_variable_names():
    assert Kmap(variables_n=2).variable_names == ['a', 'b']
    assert Kmap(variables_n=1).variable_names == ['a']
    assert Kmap(variables_n=3).variable_names == ['a', 'b', 'c']
    assert Kmap(variables_n=6).variable_names == ['a', 'b', 'c', 'd', 'e', 'f']


def test_init_kmap_with_list():
    kmap_list_AND = [[0, 0], [0, 1]]
    kmap = Kmap(kmap=kmap_list_AND)

    assert len(kmap) == 2 and len(kmap[0]) == 2
    assert kmap == kmap_list_AND
    assert kmap.col_vars_n == 1
    assert kmap.row_vars_n == 1

