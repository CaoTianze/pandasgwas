from typing import List

from pandasgwas.Variant import Variant
from pandasgwas import client
from functools import reduce
from pandas import read_csv
import os


def get_variants_by_study_id(study_id: str, interactive: bool = True) -> Variant:
    """
    Get GWAS Catalog Single Nucleotide Polymorphisms by Study identifier

    ```Python
    from pandasgwas.get_variants import get_variants_by_study_id
    snps = get_variants_by_study_id('GCST000854')
    ```

    Args:
        study_id: Study identifier, accessionId in Study
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Variant object

    """
    return Variant(
        client.get_SNPs('https://www.ebi.ac.uk/gwas/rest/api/studies/%s/snps' % study_id, interactive=interactive))


def get_variants_by_association_id(association_id: str, interactive: bool = True) -> Variant:
    """
    Get GWAS Catalog Single Nucleotide Polymorphisms by by their Association identifier

    ```Python
    from pandasgwas.get_variants import get_variants_by_association_id
    snps = get_variants_by_association_id('16603')
    ```

    Args:
        association_id: Association identifier, associationId in Association
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Variant object

    """
    return Variant(
        client.get_SNPs('https://www.ebi.ac.uk/gwas/rest/api/associations/%s/snps' % association_id,
                        interactive=interactive))


def get_variants_by_variant_id(variant_id: str, interactive: bool = True) -> Variant:
    """
    Get GWAS Catalog Single Nucleotide Polymorphisms by Single Nucleotide Polymorphism identifier

    ```Python
    from pandasgwas.get_variants import get_variants_by_variant_id
    snps = get_variants_by_variant_id('rs7744020')
    ```

    Args:
        variant_id: Single Nucleotide Polymorphism identifier, rsId in Single Nucleotide Polymorphism
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Variant object

    """
    return Variant(
        client.get_SNPs('https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/%s' % variant_id,
                        interactive=interactive))


def get_variants_by_efo_id(efo_id: str, interactive: bool = True) -> Variant:
    """
    Get GWAS Catalog Single Nucleotide Polymorphisms by their EFO Trait identifier

    ```Python
    from pandasgwas.get_variants import get_variants_by_efo_id
    snps = get_variants_by_efo_id('EFO_0001065')
    ```

    Args:
        efo_id: EFO Trait identifier, shortForm in EFO Trait
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Variant object

    """
    trait = client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/efoTraits/%s' % efo_id)[0].get('trait')
    return get_variants_by_efo_trait(trait, interactive)


def get_variants_by_pubmed_id(pubmed_id: str, interactive: bool = True) -> Variant:
    """
    Get GWAS Catalog Single Nucleotide Polymorphisms by PubMed identifiers

    ```Python
    from pandasgwas.get_variants import get_variants_by_pubmed_id
    snps = get_variants_by_pubmed_id('21041247')
    ```

    Args:
        pubmed_id: PubMed identifier
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Variant object

    """
    return Variant(
        client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByPubmedId?pubmedId=%s' % pubmed_id,
            interactive=interactive))


def get_variants_by_genomic_range(chromosome: str, start: int, end: int,
                                  interactive: bool = True) -> Variant:
    """
    Get GWAS Catalog Single Nucleotide Polymorphisms by genomic range

    ```Python
    from pandasgwas.get_variants import get_variants_by_genomic_range
    snps = get_variants_by_genomic_range('1', 2300001, 5300000)
    ```

    Args:
        chromosome: Human chromosome names: autosomal and sexual chromosomes only, i.e., 1--22, X and Y
        start: Start position of range (starts at 1).
        end: End position of range (inclusive).
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Variant object

    """
    return Variant(
        client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByChromBpLocationRange'
            '?chrom=%s&bpStart=%d&bpEnd=%d' % (chromosome,
                                               start, end), interactive=interactive))


def get_variants_by_cytogenetic_band(cytogenetic_band: str, interactive: bool = True) -> Variant:
    """
    Get GWAS Catalog Single Nucleotide Polymorphisms by cytogenetic band.

    ```Python
    from pandasgwas.get_variants import get_variants_by_cytogenetic_band
    snps = get_variants_by_cytogenetic_band('1p36.32')
    ```

    Args:
        cytogenetic_band: Cytogenetic bands of the form '1p36.11'
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Variant object

    """
    project_dir = os.path.split(os.path.realpath(__file__))[0]
    df = read_csv(project_dir + os.sep + 'cytogenetic_bands.csv', index_col='index', infer_datetime_format=True,
                  parse_dates=['last_download_date'])
    query_df = df[df['cytogenetic_band'] == cytogenetic_band]
    if query_df.size == 0:
        return Variant()
    else:
        chromosome = query_df.loc[:, 'chromosome'].values[0]
        start = query_df.loc[:, 'start'].values[0]
        end = query_df.loc[:, 'end'].values[0]
    return get_variants_by_genomic_range(chromosome, start, end, interactive=interactive)


def get_variants_by_gene_name(gene_name: str, interactive: bool = True) -> Variant:
    """
    Get GWAS Catalog Single Nucleotide Polymorphisms gene name

    ```Python
    from pandasgwas.get_variants import get_variants_by_gene_name
    snps = get_variants_by_gene_name('KIAA0319')
    ```

    Args:
        gene_name: Gene names
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Variant object

    """
    return Variant(
        client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByGene?geneName=%s' % gene_name,
            interactive=interactive))


def get_variants_by_efo_trait(efo_trait: str, interactive: bool = True) -> Variant:
    """
    Get GWAS Catalog Single Nucleotide Polymorphisms that match trait description

    ```Python
    from pandasgwas.get_variants import get_variants_by_efo_trait
    snps = get_variants_by_efo_trait('MHPG measurement')
    ```

    Args:
        efo_trait: Trait description
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Variant object

    """
    return Variant(
        client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByEfoTrait?efoTrait=%s' % efo_trait,
            interactive=interactive))


def get_variants_by_reported_trait(reported_trait: str, interactive: bool = True) -> Variant:
    """
    Get GWAS Catalog Single Nucleotide Polymorphisms that match the reported traits, as reported by the original authors of the study.

    ```Python
    from pandasgwas.get_variants import get_variants_by_reported_trait
    snps = get_variants_by_reported_trait("Dupuytren's disease")
    ```

    Args:
        reported_trait: Trait are reported by the original authors of the study
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Variant object

    """
    return Variant(
        client.get_SNPs(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/search/findByDiseaseTrait?diseaseTrait=%s' % reported_trait,
            interactive=interactive))


def get_variants_all(interactive: bool = True) -> Variant:
    """
    Get all Single Nucleotide Polymorphisms

    ```Python
    from pandasgwas.get_variants import get_variants_all
    snps = get_variants_all()
    ```

    Args:
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Variant object

    """
    return Variant(
        client.get_SNPs('https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms', interactive=interactive))


def get_variants(study_id: str = None, association_id: str = None, variant_id: str = None, efo_id: str = None,
                 pubmed_id: str = None, genomic_range: List[int] = None,
                 gene_name: str = None, efo_trait: str = None, reported_trait: str = None,
                 set_operation: str = 'bind',
                 interactive: bool = True) -> Variant:
    """
    Retrieves Single Nucleotide Polymorphisms via the NHGRI-EBI GWAS Catalog REST API. The REST API is queried multiple times with the criteria passed as arguments. By default all Single Nucleotide Polymorphisms that match the criteria supplied in the arguments are retrieved: this corresponds to the default set_operation set to 'bind', If you rather have only the Single Nucleotide Polymorphisms that match simultaneously all criteria provided, then set set_operation to 'intersection'.

    ```Python
    from pandasgwas.get_variants import get_variants_by_variant_id
    snps = get_variants(variant_id='rs7744020')
    ```

    Args:
        study_id:
        association_id: Association identifier, associationId in Association
        variant_id: Single Nucleotide Polymorphism identifier, rsId in Single Nucleotide Polymorphism
        efo_id: EFO Trait identifier, shortForm in EFO Trait
        pubmed_id: PubMed identifier
        genomic_range: A List of three elements. These elements are: 'chromosome', 'start' and 'end' in function [get_variants_by_genomic_range][pandasgwas.get_variants.get_variants_by_genomic_range]
        gene_name: Gene names
        efo_trait: Trait description
        reported_trait: Trait are reported by the original authors of the study
        set_operation:  "bind" or "intersection"
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Variant object

    """
    if study_id is None and association_id is None and variant_id is None and efo_id is None and pubmed_id is None and genomic_range is None and gene_name is None and efo_trait is None and reported_trait is None:
        return Variant(
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
        return Variant(all_data)
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
        return Variant(intersection_result)
