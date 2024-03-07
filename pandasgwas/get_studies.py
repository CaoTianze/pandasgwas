from pandasgwas.Study import Study
from pandasgwas import client
from functools import reduce


def get_studies_by_study_id(study_id: str, interactive: bool = True) -> Study:
    """
    Get GWAS Catalog Studies by Study identifier

    ```Python
    from pandasgwas.get_studies import get_studies_by_study_id
    studies = get_studies_by_study_id('GCST000854')

    ```

    Args:
        study_id: Study identifier, accessionId in Study
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Study object

    """
    return Study(
        client.get_studies('https://www.ebi.ac.uk/gwas/rest/api/studies/%s' % study_id, interactive=interactive))


def get_studies_by_association_id(association_id: str, interactive: bool = True) -> Study:
    """
    Get GWAS Catalog Studies by by their Association identifier


    ```Python
    from pandasgwas.get_studies import get_studies_by_association_id
    studies = get_studies_by_association_id('16510553')

    ```

    Args:
        association_id: Association identifier, associationId in Association
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Study object

    """
    return Study(client.get_studies('https://www.ebi.ac.uk/gwas/rest/api/associations/%s/study' % association_id,
                                    interactive=interactive))


def get_studies_by_variant_id(variant_id: str, interactive: bool = True) -> Study:
    """
    Get GWAS Catalog Studies by Single Nucleotide Polymorphism identifier

    ```Python
    from pandasgwas.get_studies import get_studies_by_variant_id
    studies = get_studies_by_variant_id('rs7329174')

    ```

    Args:
        variant_id: Single Nucleotide Polymorphism identifier, rsId in Single Nucleotide Polymorphism
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Study object

    """
    return Study(client.get_studies(
        'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/%s/studies' % variant_id,
        interactive=interactive))


def get_studies_by_efo_id(efo_id: str, interactive: bool = True) -> Study:
    """
    Get GWAS Catalog Studies by their EFO Trait identifier

    ```Python
    from pandasgwas.get_studies import get_studies_by_efo_id
    studies = get_studies_by_efo_id('EFO_0005133')

    ```

    Args:
        efo_id: EFO Trait identifier, shortForm in EFO Trait
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Study object

    """
    return Study(client.get_studies("https://www.ebi.ac.uk/gwas/rest/api/efoTraits/%s/studies" % efo_id,
                                    interactive=interactive))


def get_studies_by_pubmed_id(pubmed_id: str, interactive: bool = True) -> Study:
    """
    Get GWAS Catalog Studies by PubMed identifiers

    ```Python
    from pandasgwas.get_studies import get_studies_by_pubmed_id
    studies = get_studies_by_pubmed_id('21041247')

    ```

    Args:
        pubmed_id: PubMed identifier
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Study object

    """
    return Study(client.get_studies(
        "https://www.ebi.ac.uk/gwas/rest/api/studies/search/findByPublicationIdPubmedId?pubmedId=%s" % pubmed_id,
        interactive=interactive))


def get_studies_by_user_requested(user_requested: bool, interactive: bool = True) -> Study:
    """
    Get GWAS Catalog Studies that have been requested by users or not

    ```Python
    from pandasgwas.get_studies import get_studies_by_user_requested
    studies = get_studies_by_user_requested('True')

    ```

    Args:
        user_requested: Whether the addition of this study to the Catalog was requested by a user
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Study object

    """
    return Study(client.get_studies(
        "https://www.ebi.ac.uk/gwas/rest/api/studies/search/findByUserRequested?userRequested=%s" % user_requested,
        interactive=interactive))


def get_studies_by_full_pvalue_set(full_pvalue_set: bool, interactive: bool = True) -> Study:
    """
    Get GWAS Catalog Studies by full summary statistics criterion

    ```Python
    from pandasgwas.get_studies import get_studies_by_full_pvalue_set
    studies = get_studies_by_full_pvalue_set('False')

    ```

    Args:
        full_pvalue_set: Whether full summary statistics are available for this study
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Study object

    """
    return Study(client.get_studies(
        "https://www.ebi.ac.uk/gwas/rest/api/studies/search/findByFullPvalueSet?fullPvalueSet=%s" % full_pvalue_set,
        interactive=interactive))


def get_studies_by_efo_uri(efo_uri: str, interactive: bool = True) -> Study:
    """
    Get GWAS Catalog Studies by EFO URI

    ```Python
    from pandasgwas.get_studies import get_studies_by_efo_uri
    studies = get_studies_by_efo_uri('http://www.ebi.ac.uk/efo/EFO_0005133')

    ```

    Args:
        efo_uri: EFO URI
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Study object

    """
    return Study(client.get_studies("https://www.ebi.ac.uk/gwas/rest/api/studies/search/findByEfoUri?uri=%s" % efo_uri,
                                    interactive=interactive))


def get_studies_by_efo_trait(efo_trait: str, interactive: bool = True) -> Study:
    """
    Get GWAS Catalog Studies that match trait description

    ```Python
    from pandasgwas.get_studies import get_studies_by_efo_trait
    studies = get_studies_by_efo_trait('MHPG measurement')

    ```

    Args:
        efo_trait: Trait description
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Study object

    """
    return Study(
        client.get_studies("https://www.ebi.ac.uk/gwas/rest/api/studies/search/findByEfoTrait?efoTrait=%s" % efo_trait,
                           interactive=interactive))


def get_studies_by_reported_trait(reported_trait: str, interactive: bool = True) -> Study:
    """
    Gets studies that match the reported traits, as reported by the original authors of the study.

    ```Python
    from pandasgwas.get_studies import get_studies_by_reported_trait
    studies = get_studies_by_reported_trait('Vitamin D levels')

    ```

    Args:
        reported_trait: Trait are reported by the original authors of the study
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Study object

    """
    return Study(client.get_studies(
        "https://www.ebi.ac.uk/gwas/rest/api/studies/search/findByDiseaseTrait?diseaseTrait=%s" % reported_trait,
        interactive=interactive))


def get_studies_all(interactive: bool = True) -> Study:
    """
    Gets all Studies

    ```Python
    from pandasgwas.get_studies import get_studies_all
    studies = get_studies_all()

    ```

    Args:
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Study object

    """
    return Study(client.get_studies("https://www.ebi.ac.uk/gwas/rest/api/studies", interactive=interactive))


def get_studies(study_id: str = None, association_id: str = None, variant_id: str = None, efo_id: str = None,
                pubmed_id: str = None, user_requested: bool = None,
                full_pvalue_set: bool = None, efo_uri: str = None, efo_trait: str = None, reported_trait: str = None,
                set_operation: str = 'bind',
                interactive: bool = True) -> Study:
    """
    Retrieves Studies via the NHGRI-EBI GWAS Catalog REST API. The REST API is queried multiple times with the criteria passed as arguments. By default all Studies that match the criteria supplied in the arguments are retrieved: this corresponds to the default set_operation set to 'bind', If you rather have only the Studies that match simultaneously all criteria provided, then set set_operation to 'intersection'.

    ```Python
    from pandasgwas.get_studies import get_studies_by_study_id
    studies = get_studies(study_id='GCST000854')

    ```

    Args:
        study_id: Study identifier, accessionId in Study
        association_id: Association identifier, associationId in Association
        variant_id: Single Nucleotide Polymorphism identifier, rsId in Single Nucleotide Polymorphism
        efo_id: EFO Trait identifier, shortForm in EFO Trait
        pubmed_id: PubMed identifier
        user_requested: Whether the addition of this study to the Catalog was requested by a user
        full_pvalue_set: Whether full summary statistics are available for this study
        efo_uri:  EFO URI
        efo_trait: Trait description
        reported_trait:  Trait are reported by the original authors of the study
        set_operation: "bind" or "intersection"
        interactive:  Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Study object

    """
    if study_id is None and association_id is None and variant_id is None and efo_id is None and pubmed_id is None and user_requested is None and full_pvalue_set is None and efo_uri is None and efo_trait is None and reported_trait is None:
        return Study(client.get_studies('https://www.ebi.ac.uk/gwas/rest/api/studies', interactive=interactive))
    studies = {}
    if study_id is not None:
        studies['study_id'] = client.get_studies('https://www.ebi.ac.uk/gwas/rest/api/studies/%s' % study_id,
                                                 interactive=interactive)
    if association_id is not None:
        studies['association_id'] = client.get_studies(
            'https://www.ebi.ac.uk/gwas/rest/api/associations/%s/study' % association_id,
            interactive=interactive)
    if variant_id is not None:
        studies['variant_id'] = client.get_studies(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/%s/studies' % variant_id,
            interactive=interactive)
    if efo_id is not None:
        studies['efo_id'] = client.get_studies("https://www.ebi.ac.uk/gwas/rest/api/efoTraits/%s/studies" % efo_id,
                                               interactive=interactive)
    if pubmed_id is not None:
        studies['pubmed_id'] = client.get_studies(
            "https://www.ebi.ac.uk/gwas/rest/api/studies/search/findByPublicationIdPubmedId?pubmedId=%s" % pubmed_id,
            interactive=interactive)
    if user_requested is not None:
        studies['user_requested'] = client.get_studies(
            "https://www.ebi.ac.uk/gwas/rest/api/studies/search/findByUserRequested?userRequested=%s" % user_requested,
            interactive=interactive)
    if full_pvalue_set is not None:
        studies['full_pvalue_set'] = client.get_studies(
            "https://www.ebi.ac.uk/gwas/rest/api/studies/search/findByFullPvalueSet?fullPvalueSet=%s" % full_pvalue_set,
            interactive=interactive)
    if efo_uri is not None:
        studies['efo_uri'] = client.get_studies(
            "https://www.ebi.ac.uk/gwas/rest/api/studies/search/findByEfoUri?uri=%s" % efo_uri, interactive=interactive)
    if efo_trait is not None:
        studies['efo_trait'] = client.get_studies(
            "https://www.ebi.ac.uk/gwas/rest/api/studies/search/findByEfoTrait?efoTrait=%s" % efo_trait,
            interactive=interactive)
    if reported_trait is not None:
        studies['reported_trait'] = client.get_studies(
            "https://www.ebi.ac.uk/gwas/rest/api/studies/search/findByDiseaseTrait?diseaseTrait=%s" % reported_trait,
            interactive=interactive)
    if set_operation == 'bind':
        all_data = []
        for singe_get in studies.values():
            all_data.extend(singe_get)
        return Study(all_data)
    else:
        accessionId_dict = {}
        accessionId_sets = []
        for singe_get in studies.values():
            temp_set = set()
            for i in singe_get:
                accessionId_dict[i.get('accessionId')] = i
                temp_set.add(i.get('accessionId'))
            accessionId_sets.append(temp_set)
        intersection_accessionId = reduce(lambda x, y: x.intersection(y), accessionId_sets)
        intersection_result = []
        for k in intersection_accessionId:
            intersection_result.append(accessionId_dict.get(k))
        return Study(intersection_result)
