from pandasgwas.get_variants import *


def test_single_nucleotide_polymorphism():
    df = get_variants_by_study_id('GCST000854')
    assert len(df) == 4
    assert df[3].variants.size == 6 * 1
    assert df[3].locations.size == 4 * 1
    assert df[3].genomic_contexts.size == 15 * 7
    assert df[3].entrez_gene_ids.size == 3 * 7
    assert df[3].ensembl_gene_ids.size == 3 * 4
    assert df['rs10854398'].variants.size == 6 * 1
    assert df['rs10854398'].locations.size == 4 * 1
    assert df['rs10854398'].genomic_contexts.size == 15 * 7
    assert df['rs10854398'].entrez_gene_ids.size == 3 * 7
    assert df['rs10854398'].ensembl_gene_ids.size == 3 * 6
    assert df[1:3].variants.size == 6 * 2
    assert df[[0, 1, 2]].variants.size == 6 * 3
    assert df['rs10854398', 'rs4918918'].variants.size == 6 * 2


def test_single_nucleotide_polymorphism_set_operation():
    df1 = get_variants(study_id='GCST000854', association_id='16603')
    df2 = get_variants(study_id='GCST000854', variant_id='rs7744020')
    df3 = df1 + df2
    assert df3.variants.size == 6 * 10
    df4 = df1 - df2
    assert df4.variants.size == 6 * 0
    df4 = df2 - df1
    assert df4.variants.size == 6 * 1
    df4 = df1 & df2
    assert df4.variants.size == 6 * 4
    df4 = df1 | df2
    assert df4.variants.size == 6 * 5
    df4 = df1 ^ df2
    assert df4.variants.size == 6 * 1
    df1 = get_variants(study_id='GCST000854')
    df2 = get_variants(study_id='GCST000854')
    assert df1 == df2
