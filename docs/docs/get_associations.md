# get_associations

Get Association function based on different search criteria

## *function* get_associations_by_study_id(study_id: str, interactive: bool = True) -> Association
Get GWAS Catalog Associations by Study identifier
```Python
from pandasgwas.get_associations import *
associations = get_associations_by_study_id('GCST000854') 
```
### param study_id
Study identifier, accessionId in Study
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_associations_by_association_id(association_id: str, interactive: bool = True) -> Association
Get GWAS Catalog Associations by their Association identifier
```Python
from pandasgwas.get_associations import *
associations = get_associations_by_association_id('16603')
```
### param association_id
Association identifier, associationId in Association
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_associations_by_variant_id(variant_id: str, interactive: bool = True) -> Association
Get GWAS Catalog Associations by their Single Nucleotide Polymorphism identifier
```Python
from pandasgwas.get_associations import *
associations = get_associations_by_variant_id('rs6538678')
```
### param variant_id
Single Nucleotide Polymorphism identifier, rsId in Single Nucleotide Polymorphism
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_associations_by_efo_id(efo_id: str, interactive: bool = True) -> Association
Get GWAS Catalog Associations by their EFO Trait identifier
```Python
from pandasgwas.get_associations import *
associations = get_associations_by_efo_id('EFO_0001065')
```
### param efo_id
EFO Trait identifier, shortForm in EFO Trait
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_associations_by_pubmed_id(pubmed_id: str, interactive: bool = True) -> Association
Get GWAS Catalog associations by PubMed identifiers
```Python
from pandasgwas.get_associations import *
associations = get_associations_by_pubmed_id('21041247')
```
### param pubmed_id
PubMed identifier
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_associations_by_efo_trait(efo_trait: str, interactive: bool = True) -> Association
Gets associations that match trait description
```Python
from pandasgwas.get_associations import *
associations = get_associations_by_efo_trait('MHPG measurement')
```
### param efo_trait
Trait description
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_associations_all(interactive: bool = True) -> Association
Gets all associations
```Python
from pandasgwas.get_associations import *
associations = get_associations_all()
```
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_associations(study_id: str = None, association_id: str = None, variant_id: str = None, efo_id: str = None,pubmed_id: str = None, efo_trait: str = None, set_operation: str = 'bind',interactive: bool = True) -> Association
Retrieves Associations via the NHGRI-EBI GWAS Catalog REST API. The REST API is queried multiple times with the criteria passed as arguments. By default all Associations that match the criteria supplied in the arguments are retrieved: this corresponds to the default set_operation set to 'bind', If you rather have only the Associations that match simultaneously all criteria provided, then set set_operation to 'intersection'.