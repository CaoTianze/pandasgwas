# get_traits

Get EFO Trait function based on different search criteria

## *function* get_traits_by_study_id(study_id: str, interactive: bool = True) -> Trait
Get GWAS Catalog EFO Traits by Study identifier
```Python
from pandasgwas.get_traits import get_traits_by_study_id
traits = get_traits_by_study_id('GCST000854') 
```
### param study_id
Study identifier, accessionId in Study
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_traits_by_association_id(association_id: str, interactive: bool = True) -> Trait
Get GWAS Catalog EFO Traits by their Association identifier
```Python
from pandasgwas.get_traits import get_traits_by_association_id
traits = get_traits_by_association_id('16603') 
```
### param association_id
Association identifier, associationId in Association
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_traits_by_efo_id(efo_id: str, interactive: bool = True) -> Trait
Get GWAS Catalog EFO Traits by their EFO Trait identifier
```Python
from pandasgwas.get_traits import get_traits_by_efo_id
traits = get_traits_by_efo_id('EFO_0001065') 
```
### param efo_id
EFO Trait identifier, shortForm in EFO Trait
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_traits_by_pubmed_id(pubmed_id: str, interactive: bool = True) -> Trait
Get GWAS Catalog EFO Traits by PubMed identifiers
```Python
from pandasgwas.get_traits import get_traits_by_pubmed_id
traits = get_traits_by_pubmed_id('21041247') 
```
### param pubmed_id
PubMed identifier
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_traits_by_efo_uri(efo_uri: str, interactive: bool = True) -> Trait
Get GWAS Catalog EFO Traits by EFO URI
```Python
from pandasgwas.get_traits import get_traits_by_efo_uri
traits = get_traits_by_efo_uri('http://www.ebi.ac.uk/efo/EFO_0005133') 
```
### param efo_uri
EFO URI
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_traits_by_efo_trait(efo_trait: str, interactive: bool = True) -> Trait
Get GWAS Catalog EFO Traits that match trait description
```Python
from pandasgwas.get_traits import get_traits_by_efo_trait
traits = get_traits_by_efo_trait('MHPG measurement')
```
### param efo_trait
Trait description
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download. 
## *function* get_traits_all(interactive: bool = True) -> Trait
Gets all EFO Trats
```Python
from pandasgwas.get_traits import get_traits_all
traits = get_traits_all()
```
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_traits(study_id: str = None, association_id: str = None, efo_id=None, pubmed_id: str = None,efo_uri: str = None, efo_trait: str = None, set_operation: str = 'bind',interactive: bool = True) -> Trait
Retrieves EFO Traits via the NHGRI-EBI GWAS Catalog REST API. The REST API is queried multiple times with the criteria passed as arguments. By default all EFO Traits that match the criteria supplied in the arguments are retrieved: this corresponds to the default set_operation set to 'bind', If you rather have only the EFO Traits that match simultaneously all criteria provided, then set set_operation to 'intersection'.