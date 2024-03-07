from pandasgwas.Association import Association
from pandasgwas import client
from functools import reduce


def get_associations_by_study_id(study_id: str, interactive: bool = True) -> Association:
    """
    Get GWAS Catalog Associations by Study identifier
    ```Python
    from pandasgwas.get_associations import *
    associations = get_associations_by_study_id('GCST000854')
    ```

    Args:
        study_id: Study identifier, accessionId in Study
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        An Association object

    """
    return Association(
        client.get_associations('https://www.ebi.ac.uk/gwas/rest/api/studies/%s/associations' % study_id,
                                interactive=interactive))


def get_associations_by_association_id(association_id: str, interactive: bool = True) -> Association:
    """
    Get GWAS Catalog Associations by their Association identifier

    ```Python
    from pandasgwas.get_associations import *
    associations = get_associations_by_association_id('16603')
    ```

    Args:
        association_id: Association identifier, associationId in Association
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        An Association object

    """
    return Association(client.get_associations('https://www.ebi.ac.uk/gwas/rest/api/associations/%s' % association_id,
                                               interactive=interactive))


def get_associations_by_variant_id(variant_id: str, interactive: bool = True) -> Association:
    """
    Get GWAS Catalog Associations by their Single Nucleotide Polymorphism identifier

    ```Python
    from pandasgwas.get_associations import *
    associations = get_associations_by_variant_id('rs6538678')
    ```

    Args:
        variant_id: Single Nucleotide Polymorphism identifier, rsId in Single Nucleotide Polymorphism
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        An Association object

    """
    return Association(client.get_associations(
        'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/%s/associations' % variant_id,
        interactive=interactive))


def get_associations_by_efo_id(efo_id: str, interactive: bool = True) -> Association:
    """
    Get GWAS Catalog Associations by their EFO Trait identifier

    ```Python
    from pandasgwas.get_associations import *
    associations = get_associations_by_efo_id('EFO_0001065')
    ```

    Args:
        efo_id: EFO Trait identifier, shortForm in EFO Trait
        interactive: indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        An Association object

    """
    return Association(
        client.get_associations('https://www.ebi.ac.uk/gwas/rest/api/efoTraits/%s/associations' % efo_id,
                                interactive=interactive))


def get_associations_by_pubmed_id(pubmed_id: str, interactive: bool = True) -> Association:
    """
    Get GWAS Catalog associations by PubMed identifiers

    ```Python
    from pandasgwas.get_associations import *
    associations = get_associations_by_pubmed_id('21041247')
    ```

    Args:
        pubmed_id: PubMed identifier
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        An Association object

    """
    return Association(client.get_associations(
        'https://www.ebi.ac.uk/gwas/rest/api/associations/search/findByPubmedId?pubmedId=%s' % pubmed_id,
        interactive=interactive))


def get_associations_by_efo_trait(efo_trait: str, interactive: bool = True) -> Association:
    """
    Gets associations that match trait description

    ```Python
    from pandasgwas.get_associations import *
    associations = get_associations_by_efo_trait('MHPG measurement')
    ```

    Args:
        efo_trait: Trait description
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        An Association object

    """
    return Association(client.get_associations(
        'https://www.ebi.ac.uk/gwas/rest/api/associations/search/findByEfoTrait?efoTrait=%s' % efo_trait,
        interactive=interactive))


def get_associations_all(interactive: bool = True) -> Association:
    """
    Gets all associations

    ```Python
    from pandasgwas.get_associations import *
    associations = get_associations_all()
    ```

    Args:
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        An Association object

    """
    return Association(
        client.get_associations('https://www.ebi.ac.uk/gwas/rest/api/associations', interactive=interactive))


def get_associations(study_id: str = None, association_id: str = None, variant_id: str = None, efo_id: str = None,
                     pubmed_id: str = None, efo_trait: str = None, set_operation: str = 'bind',
                     interactive: bool = True) -> Association:
    """
    Retrieves Associations via the NHGRI-EBI GWAS Catalog REST API. The REST API is queried multiple times with the criteria passed as arguments. By default all Associations that match the criteria supplied in the arguments are retrieved: this corresponds to the default set_operation set to 'bind', If you rather have only the Associations that match simultaneously all criteria provided, then set set_operation to 'intersection'.

    ```Python
    from pandasgwas.get_associations import *
    associations = get_associations(association_id='16603')
    ```

    Args:
        study_id: Study identifier, accessionId in Study
        association_id: Association identifier, associationId in Association
        variant_id: Single Nucleotide Polymorphism identifier, rsId in Single Nucleotide Polymorphism
        efo_id:  EFO Trait identifier, shortForm in EFO Trait
        pubmed_id: PubMed identifier
        efo_trait: Trait description
        set_operation: "bind" or "intersection"
        interactive:  Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        An Association object

    """
    if study_id is None and association_id is None and variant_id is None and efo_id is None and pubmed_id is None and efo_trait is None:
        return Association(
            client.get_associations('https://www.ebi.ac.uk/gwas/rest/api/associations', interactive=interactive))
    associations = {}
    if study_id is not None:
        associations['study_id'] = client.get_associations(
            'https://www.ebi.ac.uk/gwas/rest/api/studies/%s/associations' % study_id,
            interactive=interactive)

    if association_id is not None:
        associations['association_id'] = client.get_associations(
            'https://www.ebi.ac.uk/gwas/rest/api/associations/%s' % association_id,
            interactive=interactive)

    if variant_id is not None:
        associations['associations'] = client.get_associations(
            'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/%s/associations' % variant_id,
            interactive=interactive)

    if efo_id is not None:
        associations['associations'] = client.get_associations(
            'https://www.ebi.ac.uk/gwas/rest/api/efoTraits/%s/associations' % efo_id,
            interactive=interactive)

    if pubmed_id is not None:
        associations['pubmed_id'] = client.get_associations(
            'https://www.ebi.ac.uk/gwas/rest/api/associations/search/findByPubmedId?pubmedId=%s' % pubmed_id,
            interactive=interactive)

    if efo_trait is not None:
        associations['efo_trait'] = client.get_associations(
            'https://www.ebi.ac.uk/gwas/rest/api/associations/search/findByEfoTrait?efoTrait=%s' % efo_trait,
            interactive=interactive)
    if set_operation == 'bind':
        all_data = []
        for singe_get in associations.values():
            all_data.extend(singe_get)
        return Association(all_data)
    else:
        associationId_dict = {}
        associationId_sets = []
        for singe_get in associations.values():
            temp_set = set()
            for i in singe_get:
                associationId_dict[i.get('associationId')] = i
                temp_set.add(i.get('associationId'))
            associationId_sets.append(temp_set)
        intersection_associationId = reduce(lambda x, y: x.intersection(y), associationId_sets)
        intersection_result = []
        for k in intersection_associationId:
            intersection_result.append(associationId_dict.get(k))
        return Association(intersection_result)
