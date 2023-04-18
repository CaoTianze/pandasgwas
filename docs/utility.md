# utility
## *function*  get_child_efo(efo_id: str, interactive: bool = True) -> list[str] 
Get all child terms of this trait in the EFO hierarchy
```Python
from pandasgwas import get_child_efo
child_list1=get_child_efo('EFO_0004884')#['EFO_0009393']
child_list2=get_child_efo('EFO_0005299')#[]
child_list3=get_child_efo('EFO_0009640')#['EFO_0600083', 'EFO_0005606', 'EFO_0008346', 'EFO_0006953']
```
### param efo_id
EFO identifiers
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.

## *function*  is_API_available() -> bool
Test if the API is available. If the return value is not True, it means that the API is not available.
```Python
from pandasgwas import is_API_available
is_available = is_API_available()
```
## *function*  clear_cache() -> None
Clear cache of API requests.