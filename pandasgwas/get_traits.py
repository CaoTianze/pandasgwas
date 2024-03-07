from pandasgwas.Trait import Trait
from pandasgwas import client
from functools import reduce


def get_traits_by_study_id(study_id: str, interactive: bool = True) -> Trait:
    """

    ```Python
    from pandasgwas.get_traits import get_traits_by_study_id
    traits = get_traits_by_study_id('GCST000854')
    ```

    Args:
        study_id: Study identifier, accessionId in Study
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Trait object

    """
    return Trait(client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/studies/%s/efoTraits' % study_id,
                                   interactive=interactive))


def get_traits_by_association_id(association_id: str, interactive: bool = True) -> Trait:
    """
    Get GWAS Catalog EFO Traits by their Association identifier

    ```Python
    from pandasgwas.get_traits import get_traits_by_association_id
    traits = get_traits_by_association_id('16603')

    ```

    Args:
        association_id: Association identifier, associationId in Association
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Trait object

    """
    return Trait(client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/associations/%s/efoTraits' % association_id,
                                   interactive=interactive))


def get_traits_by_efo_id(efo_id: str, interactive: bool = True) -> Trait:
    """
    Get GWAS Catalog EFO Traits by their EFO Trait identifier

    ```Python
    from pandasgwas.get_traits import get_traits_by_efo_id
    traits = get_traits_by_efo_id('EFO_0001065')

    ```

    Args:
        efo_id: EFO Trait identifier, shortForm in EFO Trait
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Trait object

    """
    return Trait(
        client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/efoTraits/%s' % efo_id, interactive=interactive))


def get_traits_by_pubmed_id(pubmed_id: str, interactive: bool = True) -> Trait:
    """
    Get GWAS Catalog EFO Traits by PubMed identifiers

    ```Python
    from pandasgwas.get_traits import get_traits_by_pubmed_id
    traits = get_traits_by_pubmed_id('21041247')

    ```

    Args:
        pubmed_id: PubMed identifier
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Trait object

    """
    return Trait(client.get_traits(
        'https://www.ebi.ac.uk/gwas/rest/api/efoTraits/search/findByPubmedId?pubmedId=%s' % pubmed_id,
        interactive=interactive))


def get_traits_by_efo_uri(efo_uri: str, interactive: bool = True) -> Trait:
    """
    Get GWAS Catalog EFO Traits by EFO URI

    ```Python
    from pandasgwas.get_traits import get_traits_by_efo_uri
    traits = get_traits_by_efo_uri('http://www.ebi.ac.uk/efo/EFO_0005133')

    ```

    Args:
        efo_uri: EFO URI
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Trait object

    """
    return Trait(
        client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/efoTraits/search/findByEfoUri?uri=%s' % efo_uri,
                          interactive=interactive))


def get_traits_by_efo_trait(efo_trait: str, interactive: bool = True) -> Trait:
    """
    Get GWAS Catalog EFO Traits that match trait description

    ```Python
    from pandasgwas.get_traits import get_traits_by_efo_trait
    traits = get_traits_by_efo_trait('MHPG measurement')

    ```

    Args:
        efo_trait: Trait description
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Trait object

    """
    return Trait(
        client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/efoTraits/search/findByEfoTrait?trait=%s' % efo_trait,
                          interactive=interactive))


def get_traits_all(interactive: bool = True) -> Trait:
    """
    Gets all EFO Trats

    ```Python
    from pandasgwas.get_traits import get_traits_all
    traits = get_traits_all()

    ```

    Args:
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Trait object

    """
    return Trait(client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/efoTraits', interactive=interactive))


def get_traits(study_id: str = None, association_id: str = None, efo_id:str =None, pubmed_id: str = None,
               efo_uri: str = None, efo_trait: str = None, set_operation: str = 'bind',
               interactive: bool = True) -> Trait:
    """
    Retrieves EFO Traits via the NHGRI-EBI GWAS Catalog REST API. The REST API is queried multiple times with the criteria passed as arguments. By default all EFO Traits that match the criteria supplied in the arguments are retrieved: this corresponds to the default set_operation set to 'bind', If you rather have only the EFO Traits that match simultaneously all criteria provided, then set set_operation to 'intersection'.

    ```Python
    from pandasgwas.get_traits import get_traits_by_efo_id
    traits = get_traits(efo_id='EFO_0001065')

    ```

    Args:
        study_id: Study identifier, accessionId in Study
        association_id: Association identifier, associationId in Association
        efo_id: EFO Trait identifier, shortForm in EFO Trait
        pubmed_id: PubMed identifier
        efo_uri: EFO URI
        efo_trait:  Trait description
        set_operation:  "bind" or "intersection"
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        A Trait object

    """
    if study_id is None and association_id is None and efo_id is None and pubmed_id is None and efo_uri is None and efo_trait is None:
        return Trait(client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/efoTraits', interactive=interactive))
    traits = {}
    if study_id is not None:
        traits['study_id'] = client.get_traits(
            'https://www.ebi.ac.uk/gwas/rest/api/studies/%s/efoTraits' % study_id, interactive=interactive)
    if association_id is not None:
        traits['association_id'] = client.get_traits(
            'https://www.ebi.ac.uk/gwas/rest/api/associations/%s/efoTraits' % association_id,
            interactive=interactive)
    if efo_id is not None:
        traits['efo_id'] = client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/efoTraits/%s' % efo_id,
                                             interactive=interactive)
    if pubmed_id is not None:
        traits['pubmed_id'] = client.get_traits(
            'https://www.ebi.ac.uk/gwas/rest/api/efoTraits/search/findByPubmedId?pubmedId=%s' % pubmed_id,
            interactive=interactive)
    if efo_uri is not None:
        traits['efo_uri'] = client.get_traits(
            'https://www.ebi.ac.uk/gwas/rest/api/efoTraits/search/findByEfoUri?uri=%s' % efo_uri,
            interactive=interactive)
    if efo_trait is not None:
        traits['efo_trait'] = client.get_traits(
            'https://www.ebi.ac.uk/gwas/rest/api/efoTraits/search/findByEfoTrait?trait=%s' % efo_trait,
            interactive=interactive)
    if set_operation == 'bind':
        all_data = []
        for singe_get in traits.values():
            all_data.extend(singe_get)
        return Trait(all_data)
    else:
        shortForm_dict = {}
        shotForm_sets = []
        for singe_get in traits.values():
            temp_set = set()
            for i in singe_get:
                shortForm_dict[i.get('shortForm')] = i
                temp_set.add(i.get('shortForm'))
            shotForm_sets.append(temp_set)
        intersection_shotForm = reduce(lambda x, y: x.intersection(y), shotForm_sets)
        intersection_result = []
        for k in intersection_shotForm:
            intersection_result.append(shortForm_dict.get(k))
        return Trait(intersection_result)