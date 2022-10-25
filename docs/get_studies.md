# get_studies

Get Study function based on different search criteria

## *function* get_studies_by_study_id(study_id: str, interactive: bool = True) -> Study
Get GWAS Catalog Studies by Study identifier
```Python
from pandasgwas.get_studies import get_studies_by_study_id
studies = get_studies_by_study_id('GCST000854')
```
### param study_id
Study identifier, accessionId in Study
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_studies_by_association_id(association_id: str, interactive: bool = True) -> Study
Get GWAS Catalog Studies by by their Association identifier
```Python
from pandasgwas.get_studies import get_studies_by_association_id
studies = get_studies_by_association_id('16510553')
```
### param association_id
Association identifier, associationId in Association
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_studies_by_variant_id(variant_id: str, interactive: bool = True) -> Study
Get GWAS Catalog Studies by Single Nucleotide Polymorphism identifier
```Python
from pandasgwas.get_studies import get_studies_by_variant_id
studies = get_studies_by_variant_id('rs7329174')
```
### param variant_id
Single Nucleotide Polymorphism identifier, rsId in Single Nucleotide Polymorphism
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_studies_by_efo_id(efo_id: str, interactive: bool = True) -> Study
Get GWAS Catalog Studies by their EFO Trait identifier
```Python
from pandasgwas.get_studies import get_studies_by_efo_id
studies = get_studies_by_efo_id('EFO_0005133')
```
### param efo_id
EFO Trait identifier, shortForm in EFO Trait
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_studies_by_pubmed_id(pubmed_id: str, interactive: bool = True) -> Study
Get GWAS Catalog Studies by PubMed identifiers
```Python
from pandasgwas.get_studies import get_studies_by_pubmed_id
studies = get_studies_by_pubmed_id('21041247')
```
### param pubmed_id
PubMed identifier
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_studies_by_user_requested(user_requested: bool, interactive: bool = True) -> Study
Get GWAS Catalog Studies that have been requested by users or not
```Python
from pandasgwas.get_studies import get_studies_by_user_requested
studies = get_studies_by_user_requested('True')
```
### param user_requested
Whether the addition of this study to the Catalog was requested by a user
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_studies_by_full_pvalue_set(full_pvalue_set: bool, interactive: bool = True) -> Study
Get GWAS Catalog Studies by full summary statistics criterion
```Python
from pandasgwas.get_studies import get_studies_by_full_pvalue_set
studies = get_studies_by_full_pvalue_set('False')
```
### param full_pvalue_set
Whether full summary statistics are available for this study
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_studies_by_efo_uri(efo_uri: str, interactive: bool = True) -> Study
Get GWAS Catalog Studies by EFO URI
```Python
from pandasgwas.get_studies import get_studies_by_efo_uri
studies = get_studies_by_efo_uri('http://www.ebi.ac.uk/efo/EFO_0005133')
```
### param efo_uri
EFO URI
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_studies_by_efo_trait(efo_trait: str, interactive: bool = True) -> Study
Get GWAS Catalog Studies that match trait description
```Python
from pandasgwas.get_studies import get_studies_by_efo_trait
studies = get_studies_by_efo_trait('MHPG measurement')
```
### param efo_trait
Trait description
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_studies_by_reported_trait(reported_trait: str, interactive: bool = True) -> Study
Gets studies that match the reported traits, as reported by the original authors of the study.
```Python
from pandasgwas.get_studies import get_studies_by_reported_trait
studies = get_studies_by_reported_trait('Vitamin D levels')
```
### param reported_trait
Trait are reported by the original authors of the study
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_studies_all(interactive: bool = True) -> Study
Gets all Studies
```Python
from pandasgwas.get_studies import get_studies_all
studies = get_studies_all()
```
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_studies(study_id: str = None, association_id: str = None, variant_id: str = None, efo_id: str = None,pubmed_id: str = None, user_requested: bool = None,full_pvalue_set: bool = None, efo_uri: str = None, efo_trait: str = None, reported_trait: str = None,set_operation: str = 'bind',interactive: bool = True) -> Study
Retrieves Studies via the NHGRI-EBI GWAS Catalog REST API. The REST API is queried multiple times with the criteria passed as arguments. By default all Studies that match the criteria supplied in the arguments are retrieved: this corresponds to the default set_operation set to 'bind', If you rather have only the Studies that match simultaneously all criteria provided, then set set_operation to 'intersection'.