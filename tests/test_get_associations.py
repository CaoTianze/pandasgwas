from pandasgwas.get_associations import *


def test_get_associations_by_study_id():
    df = get_associations_by_study_id('GCST000854')
    assert df.associations.size == 19 * 4
    assert df.loci.size == 6 * 4
    assert df.strongest_risk_alleles.size == 6 * 4
    assert df.author_reported_genes.size == 6 * 6
    assert df.entrez_gene_ids.size == 4 * 5
    assert df.ensembl_gene_ids.size == 4 * 5


def test_get_associations_by_association_id():
    df = get_associations_by_association_id('16603')
    assert df.associations.size == 19 * 1
    assert df.loci.size == 6 * 1
    assert df.strongest_risk_alleles.size == 6 * 1
    assert df.author_reported_genes.size == 6 * 1
    assert df.entrez_gene_ids.size == 4 * 0
    assert df.ensembl_gene_ids.size == 4 * 0


def test_get_associations_by_variant_id():
    df = get_associations_by_variant_id('rs6538678')
    assert df.associations.size == 19 * 1
    assert df.loci.size == 6 * 1
    assert df.strongest_risk_alleles.size == 6 * 1
    assert df.author_reported_genes.size == 6 * 2
    assert df.entrez_gene_ids.size == 4 * 1
    assert df.ensembl_gene_ids.size == 4 * 1


def test_get_associations_by_efo_id():
    df = get_associations_by_efo_id('EFO_0001065')
    assert df.associations.size == 19 * 390


def test_get_associations_by_pubmed_id():
    df = get_associations_by_pubmed_id('21041247')
    assert df.associations.size == 19 * 4


def test_get_associations_by_efo_trait():
    df = get_associations_by_efo_trait('MHPG measurement')
    assert df.associations.size == 19 * 56


def test_get_associations_all():
    assert True


def test_get_associations():
    df = get_associations(study_id='GCST000854', association_id='16603')
    assert df.associations.size == 19 * 5
    df = get_associations(study_id='GCST000854', association_id='16603',set_operation='bind')
    assert df.associations.size == 19 * 5
    df = get_associations(study_id='GCST000854', association_id='16603', set_operation='intersection')
    assert df.associations.size == 19 * 1
    df = get_associations(variant_id='rs6538678')
    assert df.associations.size == 19 * 1
    df = get_associations(efo_id='EFO_0001065', set_operation='bind')
    assert df.associations.size == 19 * 390
    df = get_associations(pubmed_id='21041247', set_operation='intersection')
    assert df.associations.size == 19 * 4
    df = get_associations(efo_trait='MHPG measurement')
    assert df.associations.size == 19 * 56
