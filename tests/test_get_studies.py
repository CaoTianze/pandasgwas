from pandasgwas.get_studies import *


def test_get_studies_by_study_id():
    df = get_studies_by_study_id("GCST000854", interactive=False)
    assert df.studies.size == 22
    assert df.platforms.size == 2
    assert df.genotyping_technologies.size == 2
    assert df.ancestries.size == 7 * 3
    assert df.ancestral_groups.size == 3 * 3
    assert df.country_of_origin.size == 5 * 0
    assert df.country_of_recruitment.size == 5 * 2


def test_get_studies_by_association_id():
    df = get_studies_by_association_id("16510553", interactive=False)
    assert df.studies.size == 22 * 1
    assert df.platforms.size == 2 * 1
    assert df.genotyping_technologies.size == 2 * 1
    assert df.ancestries.size == 7 * 2
    assert df.ancestral_groups.size == 3 * 2
    assert df.country_of_origin.size == 5 * 2
    assert df.country_of_recruitment.size == 5 * 2


def test_get_studies_by_variant_id():
    df = get_studies_by_variant_id("rs7329174", interactive=False)
    assert df.studies.size == 22 * 5
    assert df.platforms.size == 2 * 4
    assert df.genotyping_technologies.size == 2 * 5
    assert df.ancestries.size == 7 * 13
    assert df.ancestral_groups.size == 3 * 13
    assert df.country_of_origin.size == 5 * 5
    assert df.country_of_recruitment.size == 5 * 15


def test_get_studies_by_efo_id():
    df = get_studies_by_efo_id('EFO_0005133', interactive=False)
    assert df.studies.size == 22 * 3
    assert df.platforms.size == 2 * 3
    assert df.genotyping_technologies.size == 2 * 3
    assert df.ancestries.size == 7 * 3
    assert df.ancestral_groups.size == 3 * 3
    assert df.country_of_origin.size == 5 * 18
    assert df.country_of_recruitment.size == 5 * 3


def test_get_studies_by_pubmed_id():
    df = get_studies_by_pubmed_id('21041247', interactive=False)
    assert df.studies.size == 22
    assert df.platforms.size == 2
    assert df.genotyping_technologies.size == 2
    assert df.ancestries.size == 21
    assert df.ancestral_groups.size == 3 * 3
    assert df.country_of_origin.size == 0
    assert df.country_of_recruitment.size == 5 * 2


def test_get_studies_by_user_requested():
    df = get_studies_by_user_requested(True, interactive=False)
    assert df.studies.size == 22 * 365


def test_get_studies_by_full_pvalue_set():
    df = get_studies_by_full_pvalue_set(False, interactive=False)
    assert df.studies.size == 22 * 13092


def test_get_studies_by_efo_uri():
    df = get_studies_by_efo_uri('http://www.ebi.ac.uk/efo/EFO_0005133', interactive=False)
    assert df.studies.size == 22 * 3


def test_get_studies_by_efo_trait():
    df = get_studies_by_efo_trait('MHPG measurement', interactive=False)
    assert df.studies.size == 22 * 3


def test_get_studies_by_reported_trait():
    df = get_studies_by_reported_trait('Vitamin D levels', interactive=False)
    assert df.studies.size == 22 * 13


def test_get_studies_all(interactive=False):
    assert True


def test_get_studies():
    df = get_studies(study_id='GCST000854', association_id='16510553')
    assert df.studies.size == 22 * 2
    df = get_studies(variant_id='rs7329174', efo_id='EFO_0005133', set_operation='intersection')
    assert df.studies.size == 0
    df = get_studies(pubmed_id='21041247')
    assert df.studies.size == 22 * 1
    df = get_studies(user_requested=True, set_operation='bind')
    assert df.studies.size == 22 * 365
    df = get_studies(full_pvalue_set=False, set_operation='intersection', interactive=False)
    assert df.studies.size == 22 * 13092
    df = get_studies(efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133', efo_trait='MHPG measurement')
    assert df.studies.size == 22 * 6
    df = get_studies(reported_trait='Vitamin D levels')
    assert df.studies.size == 22 * 13
