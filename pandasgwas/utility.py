from typing import List

from pandasgwas import client
from requests.adapters import HTTPAdapter
import requests

s = requests.Session()
s.mount('https://', HTTPAdapter(max_retries=5))


def get_child_efo(efo_id: str, interactive: bool = True) -> List[str]:
    """
    Get all child terms of this trait in the EFO hierarchy

    ```Python
    from pandasgwas import get_child_efo
    child_list1=get_child_efo('EFO_0004884')#['EFO_0009393']
    child_list2=get_child_efo('EFO_0005299')#[]
    child_list3=get_child_efo('EFO_0009640')#['EFO_0600083', 'EFO_0005606', 'EFO_0008346', 'EFO_0006953']
    ```

    Args:
        efo_id: EFO identifiers
        interactive: Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

    Returns:
        EFO identifiers

    """
    terms = client.get_child_efo('https://www.ebi.ac.uk/ols/api/ontologies/efo/descendants?id=%s' % efo_id,
                                 interactive=interactive)
    ids = []
    for term in terms:
        ids.append(term.get('short_form'))
    return ids


def is_API_available() -> bool:
    """
    Test if the API is available. If the return value is not True, it means that the API is not available.

    ```Python
    from pandasgwas import is_API_available
    is_available = is_API_available()
    ```

    Returns:
        True or False
    """
    try:
        r = s.get("https://www.ebi.ac.uk/gwas/rest/api/efoTraits")
        if r.status_code == 200:
            return True
        return False
    except:
        return False


def clear_cache() -> None:
    """
    Clear cache of API requests.

    Returns:
        None

    """
    client.cache_get.cache_clear()
