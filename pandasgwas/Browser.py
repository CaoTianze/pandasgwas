"""
A set of helper functions for accessing web links
"""
import webbrowser


def open_in_pubmed(pubmed_id: str) -> bool:
    """
    This function launches the web browser and opens a tab for PubMed citation
    ```Python
    from pandasgwas.Browser import *
    open_in_pubmed('26301688')
    ```

    Args:
        pubmed_id: A PubMed identifier

    Returns:

    """
    return webbrowser.open_new_tab('https://pubmed.ncbi.nlm.nih.gov/%s' % pubmed_id)


def open_in_dbsnp(variant_id: str) -> bool:
    """
    This function launches the web browser at dbSNP and opens a tab for SNP identifier
    ```Python
    from pandasgwas.Browser import *
    open_in_dbsnp('rs56261590')
    ```

    Args:
        variant_id: A variant(Single Nucleotide Polymorphism) identifier

    Returns:

    """
    return webbrowser.open_new_tab('https://www.ncbi.nlm.nih.gov/snp/%s' % variant_id)


def open_in_gtex(variant_id: str) -> bool:
    """
    This function launches the web browser at the GTEx Portal and opens a tab for SNP identifier.
    ```Python
    from pandasgwas.Browser import *
    open_in_gtex('rs56261590')
    ```

    Args:
        variant_id: A variant(Single Nucleotide Polymorphism) identifier

    Returns:

    """
    return webbrowser.open_new_tab('https://gtexportal.org/home/snp/%s' % variant_id)


def open_study_in_gwas_catalog(study_id: str) -> bool:
    """
    Browse GWAS Catalog entitie Study from the GWAS Web Graphical User Interface
    ```Python
    from pandasgwas.Browser import *
    open_study_in_gwas_catalog('GCST000016')
    ```

    Args:
        study_id: A Study identifier

    Returns:

    """
    return webbrowser.open_new_tab('https://www.ebi.ac.uk/gwas/studies/%s' % study_id)


def open_variant_in_gwas_catalog(variant_id: str) -> bool:
    """
    Browse GWAS Catalog entitie Single Nucleotide Polymorphism from the GWAS Web Graphical User Interface
    ```Python
    from pandasgwas.Browser import *
    open_variant_in_gwas_catalog('rs146992477')
    ```

    Args:
        variant_id: A variant(Single Nucleotide Polymorphism) identifier

    Returns:

    """
    return webbrowser.open_new_tab('https://www.ebi.ac.uk/gwas/variants/%s' % variant_id)


def open_trait_in_gwas_catalog(efo_id: str) -> bool:
    """
    Browse GWAS Catalog entitie Trait from the GWAS Web Graphical User Interface
    ```Python
    from pandasgwas.Browser import *
    open_trait_in_gwas_catalog('EFO_0004884')
    ```

    Args:
        efo_id: An EFO Trait identifier

    Returns:

    """
    return webbrowser.open_new_tab('https://www.ebi.ac.uk/gwas/efotraits/%s' % efo_id)


def open_gene_in_gwas_catalog(gene_name: str) -> bool:
    """
    Browse GWAS Catalog entitie Gene from the GWAS Web Graphical User Interface
    ```Python
    from pandasgwas.Browser import *
    open_gene_in_gwas_catalog('DPP6')
    ```

    Args:
        gene_name: Gene name

    Returns:

    """
    return webbrowser.open_new_tab('https://www.ebi.ac.uk/gwas/genes/%s' % gene_name)


def open_region_in_gwas_catalog(region_name_or_location: str) -> bool:
    """
    Browse GWAS Catalog entitie Region from the GWAS Web Graphical User Interface
    ```Python
    from pandasgwas.Browser import *
    #region_name
    open_region_in_gwas_catalog('2q37.1')
    #location
    open_region_in_gwas_catalog('chr2:230100001-234700000')
    ```

    Args:
        region_name_or_location: Region name or chromosome and base pair location on the reference genome

    Returns:

    """
    return webbrowser.open_new_tab('https://www.ebi.ac.uk/gwas/regions/%s' % region_name_or_location)


def open_publication_in_gwas_catalog(pubmed_id: str) -> bool:
    """
    Browse GWAS Catalog entitie Publication from the GWAS Web Graphical User Interface
    ```Python
    from pandasgwas.Browser import *
    open_publication_in_gwas_catalog('25533513')
    ```

    Args:
        pubmed_id: A PubMed identifier

    Returns:

    """
    return webbrowser.open_new_tab('https://www.ebi.ac.uk/gwas/publications/%s' % pubmed_id)
