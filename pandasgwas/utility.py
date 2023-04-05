from typing import List

from pandasgwas import client
from requests.adapters import HTTPAdapter
import requests

s = requests.Session()
s.mount('https://', HTTPAdapter(max_retries=5))


def get_child_efo(efo_id: str, interactive: bool = True) -> List[str]:
    terms = client.get_child_efo('https://www.ebi.ac.uk/ols/api/ontologies/efo/descendants?id=%s' % efo_id,
                                 interactive=interactive)
    ids = []
    for term in terms:
        ids.append(term.get('short_form'))
    return ids


def is_API_available() -> bool:
    try:
        r = s.get("https://www.ebi.ac.uk/gwas/rest/api/efoTraits")
        if r.status_code == 200:
            return True
        return False
    except:
        return False
