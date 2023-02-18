from pandasgwas import client


def get_child_efo(efo_id: str, interactive: bool = True) -> list[str]:
    terms = client.get_child_efo('https://www.ebi.ac.uk/ols/api/ontologies/efo/descendants?id=%s' % efo_id,
                                 interactive=interactive)
    ids = []
    for term in terms:
        ids.append(term.get('short_form'))
    return ids
