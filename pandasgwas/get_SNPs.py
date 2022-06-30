from typing import List

from pandasgwas.SingleNucleotidePolymorphism import SingleNucleotidePolymorphism
from pandasgwas import client
from functools import reduce
from pandas import read_csv
import os


def get_variants_by_study_id(study_id: str, interactive: bool = True) -> SingleNucleotidePolymorphism:
    return SingleNucleotidePolymorphism(
        client.get_SNPs('https://www.ebi.ac.uk/gwas/rest/api/studies/%s/snps' % study_id, interactive=interactive))


def get_variants_by_association_id(association_id: str, interactive: bool = True) -> SingleNucleotidePolymorphism:
    return SingleNucleotidePolymorphism(
        client.get_SNPs('https://www.ebi.ac.uk/gwas/rest/api/associations/%s/snps' % association_id,
                        interactive=interactive))


def get_variants_by_variant_id(variant_id: str, interactive: bool = True) -> SingleNucleotidePolymorphism:
    return SingleNucleotidePolymorphism(
        client.get_SNPs('https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/%s' % variant_id,
                        interactive=interactive))


def get_variants_by_efo_id(efo_id: str, interactive: bool = True) -> SingleNucleotidePolymorphism:
    trait = client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/efoTraits/%s' % efo_id)[0].get('trait')
    return get_variants_by_efo_trait(trait, interactive)


def get_variants_by_pubmed_id(pubmed_id: str, interactive: bool = True) -> SingleNucleotidePolymorphism:
    return SingleNucleotidePolymorphism(
        client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByPubmedId?pubmedId=%s' % pubmed_id,
            interactive=interactive))


def get_variants_by_genomic_range(chromosome: str, start: int, end: int,
                                  interactive: bool = True) -> SingleNucleotidePolymorphism:
    return SingleNucleotidePolymorphism(
        client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByChromBpLocationRange'
            '?chrom=%s&bpStart=%d&bpEnd=%d' % (chromosome,
                                               start, end), interactive=interactive))


def get_variants_by_cytogenetic_band(cytogenetic_band: str, interactive: bool = True) -> SingleNucleotidePolymorphism:
    project_dir = os.path.split(os.path.realpath(__file__))[0]
    df = read_csv(project_dir + os.sep + 'cytogenetic_bands.csv', index_col='index', infer_datetime_format=True,
                  parse_dates=['last_download_date'])
    query_df = df[df['cytogenetic_band'] == cytogenetic_band]
    if query_df.size == 0:
        return SingleNucleotidePolymorphism()
    else:
        chromosome = query_df.loc[:, 'chromosome'].values[0]
        start = query_df.loc[:, 'start'].values[0]
        end = query_df.loc[:, 'end'].values[0]
    return get_variants_by_genomic_range(chromosome, start, end, interactive=interactive)


def get_variants_by_gene_name(gene_name: str, interactive: bool = True) -> SingleNucleotidePolymorphism:
    return SingleNucleotidePolymorphism(
        client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByGene?geneName=%s' % gene_name,
            interactive=interactive))


def get_variants_by_efo_trait(efo_trait: str, interactive: bool = True) -> SingleNucleotidePolymorphism:
    return SingleNucleotidePolymorphism(
        client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByEfoTrait?efoTrait=%s' % efo_trait,
            interactive=interactive))


def get_variants_by_reported_trait(reported_trait: str, interactive: bool = True) -> SingleNucleotidePolymorphism:
    return SingleNucleotidePolymorphism(
        client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByDiseaseTrait?diseaseTrait=%s' % reported_trait,
            interactive=interactive))


def get_variants_all(interactive: bool = True) -> SingleNucleotidePolymorphism:
    return SingleNucleotidePolymorphism(
        client.get_SNPs('https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms', interactive=interactive))


def get_variants(study_id: str = None, association_id: str = None, variant_id: str = None, efo_id: str = None,
                 pubmed_id: str = None, genomic_range: List[int] = None,
                 gene_name: str = None, efo_trait: str = None, reported_trait: str = None,
                 set_operation: str = 'bind',
                 interactive: bool = True) -> SingleNucleotidePolymorphism:
    if study_id is None and association_id is None and variant_id is None and efo_id is None and pubmed_id is None and genomic_range is None and gene_name is None and efo_trait is None and reported_trait is None:
        return SingleNucleotidePolymorphism(
            client.get_SNPs('https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms',
                            interactive=interactive))
    variants = {}
    if study_id is not None:
        variants['study_id'] = client.get_SNPs('https://www.ebi.ac.uk/gwas/rest/api/studies/%s/snps' % study_id,
                                               interactive=interactive)

    if association_id is not None:
        variants['association_id'] = client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/associations/%s/snps' % association_id,
            interactive=interactive)

    if variant_id is not None:
        variants['variant_id'] = client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/%s' % variant_id,
            interactive=interactive)

    if efo_id is not None:
        trait = client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/efoTraits/%s' % efo_id)[0].get('trait')
        variants['efo_id'] = client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByEfoTrait?efoTrait=%s' % trait,
            interactive=interactive)

    if pubmed_id is not None:
        variants['pubmed_id'] = client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByPubmedId?pubmedId=%s' % pubmed_id,
            interactive=interactive)

    if genomic_range is not None:
        variants['genomic_range'] = client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByChromBpLocationRange'
            '?chrom=%s&bpStart=%d&bpEnd=%d' % (str(genomic_range[0]), genomic_range[1], genomic_range[2]),
            interactive=interactive)

    if gene_name is not None:
        variants['gene_name'] = client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByGene?geneName=%s' % gene_name,
            interactive=interactive)

    if efo_trait is not None:
        variants['efo_trait'] = client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByEfoTrait?efoTrait=%s' % efo_trait,
            interactive=interactive)

    if reported_trait is not None:
        variants['reported_trait'] = client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByDiseaseTrait?diseaseTrait=%s' % reported_trait,
            interactive=interactive)
    if set_operation == 'bind':
        all_data = []
        for singe_get in variants.values():
            all_data.extend(singe_get)
        return SingleNucleotidePolymorphism(all_data)
    else:
        rsId_dict = {}
        rsId_sets = []
        for singe_get in variants.values():
            temp_set = set()
            for i in singe_get:
                rsId_dict[i.get('rsId')] = i
                temp_set.add(i.get('rsId'))
            rsId_sets.append(temp_set)
        intersection_rsId = reduce(lambda x, y: x.intersection(y), rsId_sets)
        intersection_result = []
        for k in intersection_rsId:
            intersection_result.append(rsId_dict.get(k))
        return SingleNucleotidePolymorphism(intersection_result)
