# Study
## *class* Study.Study()

Python class to represent a set of GWAS Catalog Study. For more information, see "[GWAS CATALOG API Guide](https://www.ebi.ac.uk/gwas/rest/docs/api)"

```Python
# get Study by study_id
from pandasgwas.get_studies import get_studies

studies = get_studies(study_id='GCST000854')

```
### *property* studies
type: pandas.DataFrame  
A DataFrame to represent all queried Studies from GWAS Catalog REST API

### *property* platforms
type: pandas.DataFrame  
A DataFrame to represent column platforms from studies

### *property* ancestries
type: pandas.DataFrame  
A DataFrame to represent column ancestries from studies

### *property* genotypingTechnologies
type: pandas.DataFrame  
A DataFrame to represent column genotypingTechnologies from studies

### *property* ancestralGroups
type: pandas.DataFrame  
A DataFrame to represent column ancestralGroups from ancestries

### *property* countriesOfOrigin
type: pandas.DataFrame  
A DataFrame to represent column countriesOfOrigin from ancestries

### *property* countriesOfRecruitment
type: pandas.DataFrame  
A DataFrame to represent column countriesOfOrigin from ancestries