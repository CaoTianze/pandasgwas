from pandasgwas.Trait import Trait
from pandasgwas import client
from functools import reduce


def get_traits_by_study_id(study_id: str, interactive: bool = True) -> Trait:
    return Trait(client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/studies/%s/efoTraits' % study_id,
                                   interactive=interactive))


def get_traits_by_association_id(association_id: str, interactive: bool = True) -> Trait:
    return Trait(client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/associations/%s/efoTraits' % association_id,
                                   interactive=interactive))


def get_traits_by_efo_id(efo_id: str, interactive: bool = True) -> Trait:
    return Trait(
        client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/efoTraits/%s' % efo_id, interactive=interactive))


def get_traits_by_pubmed_id(pubmed_id: str, interactive: bool = True) -> Trait:
    return Trait(client.get_traits(
        'https://www.ebi.ac.uk/gwas/rest/api/efoTraits/search/findByPubmedId?pubmedId=%s' % pubmed_id,
        interactive=interactive))


def get_traits_by_efo_uri(efo_uri: str, interactive: bool = True) -> Trait:
    return Trait(
        client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/efoTraits/search/findByEfoUri?uri=%s' % efo_uri,
                          interactive=interactive))


def get_traits_by_efo_trait(efo_trait: str, interactive: bool = True) -> Trait:
    return Trait(
        client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/efoTraits/search/findByEfoTrait?trait=%s' % efo_trait,
                          interactive=interactive))


def get_traits_all(interactive: bool = True) -> Trait:
    return Trait(client.get_traits('https://www.ebi.ac.uk/gwas/rest/api/efoTraits', interactive=interactive))


def get_traits(study_id: str = None, association_id: str = None, efo_id=None, pubmed_id: str = None,
               efo_uri: str = None, efo_trait: str = None, set_operation: str = 'bind',
               interactive: bool = True) -> Trait:
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