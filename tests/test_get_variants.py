from pandasgwas.get_variants import *


def test_get_variants_by_study_id():
    df = get_variants_by_study_id('GCST000854')
    assert df.variants.size == 6 * 4
    assert df.locations.size == 4 * 4
    assert df.genomic_contexts.size == 15 * 22
    assert df.entrez_gene_ids.size == 3 * 22
    assert df.ensembl_gene_ids.size == 3 * 18


def test_get_variants_by_association_id():
    df = get_variants_by_association_id('16603')
    assert df.variants.size == 6 * 1
    assert df.locations.size == 4 * 1
    assert df.genomic_contexts.size == 15 * 4
    assert df.entrez_gene_ids.size == 3 * 4
    assert df.ensembl_gene_ids.size == 3 * 4


def test_get_variants_by_variant_id():
    df = get_variants_by_variant_id('rs7744020')
    assert df.variants.size == 6 * 1
    assert df.locations.size == 4 * 7
    assert df.genomic_contexts.size == 15 * 111
    assert df.entrez_gene_ids.size == 3 * 99
    assert df.ensembl_gene_ids.size == 3 * 526


def test_get_variants_by_efo_id():
    df = get_variants_by_efo_id('EFO_0001065')
    assert df.variants.size == 6 * 398


def test_get_variants_by_pubmed_id():
    df = get_variants_by_pubmed_id('21041247')
    assert df.variants.size == 6 * 4


def test_get_variants_by_genomic_range():
    df = get_variants_by_genomic_range('1', 2300001, 5300000)
    assert df.variants.size == 6 * 267


def test_get_variants_by_cytogenetic_band():
    df = get_variants_by_cytogenetic_band('1p36.32')
    assert df.variants.size == 6 * 267


def test_get_variants_by_gene_name():
    df = get_variants_by_gene_name('KIAA0319')
    assert df.variants.size == 6 * 120


def test_get_variants_by_efo_trait():
    df = get_variants_by_efo_trait('MHPG measurement')
    assert df.variants.size == 6 * 56


def test_get_variants_by_reported_trait():
    df = get_variants_by_reported_trait("Dupuytren's disease")
    assert df.variants.size == 6 * 41


def test_get_variants_all():
    assert True


def test_get_variants():
    df = get_variants(study_id='GCST000854', association_id='16603')
    assert df.variants.size == 6 * 5
    df = get_variants(study_id='GCST000854', association_id='16603', set_operation='intersection')
    assert df.variants.size == 6 * 1
    df = get_variants(variant_id='rs7744020', efo_id='EFO_0001065', set_operation='bind')
    assert df.variants.size == 6 * 399
    df = get_variants(variant_id='rs7744020', efo_id='EFO_0001065', set_operation='intersection')
    assert df.variants.size == 6 * 0
    df = get_variants(pubmed_id='21041247', set_operation='intersection')
    assert df.variants.size == 6 * 4
    df = get_variants(genomic_range=[6, 16000000, 25000000])
    assert df.variants.size == 6 * 776
    df = get_variants(gene_name='KIAA0319')
    assert df.variants.size == 6 * 120
    df = get_variants(efo_trait='MHPG measurement')
    assert df.variants.size == 6 * 56
    df = get_variants(reported_trait="Dupuytren's disease")
    assert df.variants.size == 6 * 41

