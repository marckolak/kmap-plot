import pytest
from kmapplot.boolfunc import BooleanFunction


def test_value():
    ones = set([0, 1, 2])
    dont_cares = set([3, 4, 5])
    func = BooleanFunction(
        variable_names=["a", "b", "c"], ones=ones, dont_cares=dont_cares
    )

    for m in ones:
        assert func.value(m) == 1

    for m in ones:
        assert func.value(m) == 1

    for m in set(range(8)) - ones - dont_cares:
        assert func.value(m) == 0


def test_validate_repetitions():
    with pytest.raises(ValueError):
        ones = set([0, 1, 3])
        dont_cares = set([3, 4, 5])
        func = BooleanFunction(
            variable_names=["a", "b", "c"], ones=ones, dont_cares=dont_cares
        )


def test_validate_invalid_minterms():
    with pytest.raises(ValueError):
        ones = set([0, 1, 3])
        dont_cares = set([8, 9])
        func = BooleanFunction(
            variable_names=["a", "b", "c"], ones=ones, dont_cares=dont_cares
        )

    ones = set([0, 1, 2])
    dont_cares = set([3, 4, 5])
    func = BooleanFunction(
        variable_names=["a", "b", "c"], ones=ones, dont_cares=dont_cares
    )

    with pytest.raises(ValueError):
        func.value(10)
    with pytest.raises(ValueError):
        func.value_from_bits("1000")
