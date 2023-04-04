from pandasgwas import get_child_efo


def test_get_child_efo():
    assert len(get_child_efo('EFO_0004884')) == 1
    assert len(get_child_efo('EFO_0004343')) == 1
    assert len(get_child_efo('EFO_0005299')) == 0
    assert len(get_child_efo('EFO_0009640')) == 4
    assert len(get_child_efo('xxxx')) == 0
