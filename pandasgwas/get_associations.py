from pandasgwas.Association import Association
from pandasgwas import client
from functools import reduce


def get_associations_by_study_id(study_id: str, interactive: bool = True) -> Association:
    return Association(
        client.get_associations('https://www.ebi.ac.uk/gwas/rest/api/studies/%s/associations' % study_id,
                                interactive=interactive))


def get_associations_by_association_id(association_id: str, interactive: bool = True) -> Association:
    return Association(client.get_associations('https://www.ebi.ac.uk/gwas/rest/api/associations/%s' % association_id,
                                               interactive=interactive))


def get_associations_by_variant_id(variant_id: str, interactive: bool = True) -> Association:
    return Association(client.get_associations(
        'https://www.ebi.ac.uk/gwas/rest/api/singleNucleotidePolymorphisms/%s/associations' % variant_id,
        interactive=interactive))


def get_associations_by_efo_id(efo_id: str, interactive: bool = True) -> Association:
    return Association(
        client.get_associations('https://www.ebi.ac.uk/gwas/rest/api/efoTraits/%s/associations' % efo_id,
                                interactive=interactive))


def get_associations_by_pubmed_id(pubmed_id: str, interactive: bool = True) -> Association:
    return Association(client.get_associations(
        'https://www.ebi.ac.uk/gwas/rest/api/associations/search/findByPubmedId?pubmedId=%s' % pubmed_id,
        interactive=interactive))


def get_associations_by_efo_trait(efo_trait: str, interactive: bool = True) -> Association:
    return Association(client.get_associations(
        'https://www.ebi.ac.uk/gwas/rest/api/associations/search/findByEfoTrait?efoTrait=%s' % efo_trait,
        interactive=interactive))


def get_associations_all(interactive: bool = True) -> Association:
    return Association(
        client.get_associations('https://www.ebi.ac.uk/gwas/rest/api/associations', interactive=interactive))


def get_associations(study_id: str = None, association_id: str = None, variant_id: str = None, efo_id: str = None,
                     pubmed_id: str = None, efo_trait: str = None, set_operation: str = 'bind',
                     interactive: bool = True) -> Association:
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
