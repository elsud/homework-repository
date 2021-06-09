from homework11.enum import SimplifiedEnum


def test_simplifiedenum_sets_attributes_from_keys():
    class ColorsEnum(metaclass=SimplifiedEnum):
        __keys = ("RED", "BLUE", "ORANGE", "BLACK")

    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.ORANGE == "ORANGE"
