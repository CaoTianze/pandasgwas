from pandasgwas.get_studies import *


def test_study():
    df = get_studies_by_variant_id("rs7329174", interactive=False)
    assert len(df) == 5
    assert df[4].studies.size == 22 * 1
    assert df[4].platforms.size == 2 * 1
    assert df[4].genotyping_technologies.size == 2 * 1
    assert df[4].ancestries.size == 7 * 2
    assert df[4].ancestral_groups.size == 3 * 2
    assert df[4].country_of_origin.size == 5 * 0
    assert df[4].country_of_recruitment.size == 5 * 2
    assert df['GCST90020042'].studies.size == 22 * 1
    assert df['GCST90020042'].platforms.size == 2 * 1
    assert df['GCST90020042'].genotyping_technologies.size == 2 * 1
    assert df['GCST90020042'].ancestries.size == 7 * 1
    assert df['GCST90020042'].ancestral_groups.size == 3 * 1
    assert df['GCST90020042'].country_of_origin.size == 5 * 1
    assert df['GCST90020042'].country_of_recruitment.size == 5 * 1
    assert df[1:3].studies.size == 22 * 2
    assert df[[0, 1, 2]].studies.size == 22 * 3
    assert df['GCST90020042', 'GCST000858'].studies.size == 22*2


def test_study_set_operation():
    df1 = get_studies(study_id='GCST000854', variant_id='rs7329174')
    df2 = get_studies(association_id='16510553', variant_id='rs7329174')
    df3 = df1 + df2
    assert df3.studies.size == 22 * 12
    df4 = df1 - df2
    assert df4.studies.size == 22 * 1
    df4 = df2 - df1
    assert df4.studies.size == 22 * 1
    df4 = df1 & df2
    assert df4.studies.size == 22 * 5
    df4 = df1 | df2
    assert df4.studies.size == 22 * 7
    df4 = df1 ^ df2
    assert df4.studies.size == 22 * 2
    df1 = get_studies(variant_id='rs7329174')
    df2 = get_studies(variant_id='rs7329174')
    assert df1 == df2