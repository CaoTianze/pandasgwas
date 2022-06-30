from pandasgwas.get_traits import *


def test_trait():
    df = get_traits_by_study_id('GCST000854')
    assert len(df) == 2
    assert df[0].efo_traits.size == 3 * 1
    assert df['EFO_0000677'].efo_traits.size == 3 * 1
    assert df[1:3].efo_traits.size == 3 * 1
    assert df[[0, 1]].efo_traits.size == 3 * 2
    assert df['EFO_0000677', 'EFO_0004321'].efo_traits.size == 3*2


def test_trait_set_operation():
    df1 = get_traits(study_id='GCST000854', efo_id='EFO_0001065')
    df2 = get_traits(study_id='GCST000854', efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133')
    df3 = df1 + df2
    assert df3.efo_traits.size == 3 * 6
    df4 = df1 - df2
    assert df4.efo_traits.size == 3 * 1
    df4 = df2 - df1
    assert df4.efo_traits.size == 3 * 1
    df4 = df1 & df2
    assert df4.efo_traits.size == 3 * 2
    df4 = df1 | df2
    assert df4.efo_traits.size == 3 * 4
    df4 = df1 ^ df2
    assert df4.efo_traits.size == 3 * 2
    df1 = get_traits(study_id='GCST000854')
    df2 = get_traits(study_id='GCST000854')
    assert df1 == df2
