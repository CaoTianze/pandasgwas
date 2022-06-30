from pandasgwas.get_traits import *


def test_get_traits_by_study_id():
    df = get_traits_by_study_id('GCST000854')
    assert df.efo_traits.size == 3 * 2


def test_get_traits_by_association_id():
    df = get_traits_by_association_id('16603')
    assert df.efo_traits.size == 3 * 2


def test_get_traits_by_efo_id():
    df = get_traits_by_efo_id('EFO_0001065')
    assert df.efo_traits.size == 3 * 1


def test_get_traits_by_pubmed_id():
    df = get_traits_by_pubmed_id('21041247')
    assert df.efo_traits.size == 3 * 2


def test_get_traits_by_efo_uri():
    df = get_traits_by_efo_uri('http://www.ebi.ac.uk/efo/EFO_0005133')
    assert df.efo_traits.size == 3 * 1


def test_get_traits_by_efo_trait():
    df = get_traits_by_efo_trait('MHPG measurement')
    assert df.efo_traits.size == 3 * 1


def test_get_traits_all():
    df = get_traits_all(interactive=False)
    assert df.efo_traits.size == 3 * 5753


def test_get_traits():
    df = get_traits(study_id='GCST000854', association_id='16603')
    assert df.efo_traits.size == 3 * 4
    df = get_traits(efo_id='EFO_0001065', pubmed_id='21041247',set_operation='bind')
    assert df.efo_traits.size == 3 * 3
    df = get_traits(efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133', efo_trait='MHPG measurement')
    assert df.efo_traits.size == 3 * 2

    df = get_traits(study_id='GCST000854', association_id='16603', set_operation='intersection')
    assert df.efo_traits.size == 3 * 2
    df = get_traits(efo_id='EFO_0001065', pubmed_id='21041247', set_operation='intersection')
    assert df.efo_traits.size == 0
    df = get_traits(efo_id='EFO_0001065')
    assert df.efo_traits.size == 3 * 1
    df = get_traits(pubmed_id='21041247', set_operation='intersection')
    assert df.efo_traits.size == 3 * 2
    df = get_traits(efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133', efo_trait='MHPG measurement',
                    set_operation='intersection')
    assert df.efo_traits.size == 3 * 1
