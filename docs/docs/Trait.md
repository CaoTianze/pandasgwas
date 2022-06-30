# Trait
## *class* Trait.Trait()

Python class to represent a set of GWAS Catalog EFO Trait. For more information, see "[GWAS CATALOG API Guide](https://www.ebi.ac.uk/gwas/rest/docs/api)"

```Python
# get Tait by study_id
from pandasgwas.get_traits import get_traits

traits = get_traits(study_id='GCST000854')

```
### *property* efo_traits
type: pandas.DataFrame  
A DataFrame to represent all queried EFO Traits from GWAS Catalog REST API