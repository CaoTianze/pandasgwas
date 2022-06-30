from pandasgwas.get_associations import *


def test_association():
    df = get_associations_by_study_id('GCST000854')
    assert len(df) == 4
    assert df[3].associations.size == 19 * 1
    assert df[3].loci.size == 6 * 1
    assert df[3].strongest_risk_alleles.size == 6 * 1
    assert df[3].author_reported_genes.size == 6 * 1
    assert df[3].entrez_gene_ids.size == 4 * 1
    assert df[3].ensembl_gene_ids.size == 4 * 1
    assert df['16600'].associations.size == 19 * 1
    assert df['16600'].loci.size == 6 * 1
    assert df['16600'].strongest_risk_alleles.size == 6 * 1
    assert df['16600'].author_reported_genes.size == 6 * 2
    assert df['16600'].entrez_gene_ids.size == 4 * 2
    assert df['16600'].ensembl_gene_ids.size == 4 * 2
    assert df[1:3].associations.size == 19 * 2
    assert df[[0, 1, 2]].associations.size == 19 * 3
    assert df['16603', '16602'].associations.size == 19*2


def test_association_set_operation():
    df1 = get_associations(study_id='GCST000854', association_id='16603')
    df2 = get_associations(study_id='GCST000854', variant_id='rs6538678')
    df3 = df1 + df2
    assert df3.associations.size == 19 * 10
    df4 = df1 - df2
    assert df4.associations.size == 19 * 0
    df4 = df2 - df1
    assert df4.associations.size == 19 * 1
    df4 = df1 & df2
    assert df4.associations.size == 19 * 4
    df4 = df1 | df2
    assert df4.associations.size == 19 * 5
    df4 = df1 ^ df2
    assert df4.associations.size == 19 * 1
    df1 = get_associations(study_id='GCST000854')
    df2 = get_associations(study_id='GCST000854')
    assert df1 == df2