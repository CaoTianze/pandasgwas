from pandasgwas.get_traits import *
from pandasgwas.set_operation import *


def test_bind():
    df1 = get_traits(study_id='GCST000854', efo_id='EFO_0001065')
    df2 = get_traits(study_id='GCST000854', efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133')
    df3 = bind(df1, df2)
    assert df3.efo_traits.size == 3 * 6


def test_intersect():
    df1 = get_traits(study_id='GCST000854', efo_id='EFO_0001065')
    df2 = get_traits(study_id='GCST000854', efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133')
    df3 = intersect(df1, df2)
    assert df3.efo_traits.size == 3 * 2


def test_set_diff():
    df1 = get_traits(study_id='GCST000854', efo_id='EFO_0001065')
    df2 = get_traits(study_id='GCST000854', efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133')
    df3 = set_diff(df1, df2)
    assert df3.efo_traits.size == 3 * 1


def test_set_xor():
    df1 = get_traits(study_id='GCST000854', efo_id='EFO_0001065')
    df2 = get_traits(study_id='GCST000854', efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133')
    df3 = set_xor(df1, df2)
    assert df3.efo_traits.size == 3 * 2


def test_union():
    df1 = get_traits(study_id='GCST000854', efo_id='EFO_0001065')
    df2 = get_traits(study_id='GCST000854', efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133')
    df3 = union(df1, df2)
    assert df3.efo_traits.size == 3 * 4


def test_set_equal():
    df1 = get_traits(study_id='GCST000854')
    df2 = get_traits(study_id='GCST000854')
    assert set_equal(df1, df2)