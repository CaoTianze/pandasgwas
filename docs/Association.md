# Association
## *class* Association.Association()

Python class to represent a set of GWAS Catalog Association. For more information, see "[GWAS CATALOG API Guide](https://www.ebi.ac.uk/gwas/rest/docs/api)"

```Python
# get Association by study_id
from pandasgwas.get_associations import get_associations

associations = get_associations(study_id='GCST000854')

```
### *property* associations
type: pandas.DataFrame  
A DataFrame to represent all queried Associations from GWAS Catalog REST API

### *property* loci
type: pandas.DataFrame  
A DataFrame to represent column loci from associations

### *property* strongest_risk_alleles
type: pandas.DataFrame  
A DataFrame to represent column strongest_risk_alleles from loci

### *property* author_reported_genes
type: pandas.DataFrame  
A DataFrame to represent column author_reported_genes from loci

### *property* entrez_gene_ids
type: pandas.DataFrame  
A DataFrame to represent column entrez_gene_ids from author_reported_genes

### *property* ensembl_gene_ids
type: pandas.DataFrame  
A DataFrame to represent column entrez_gene_ids from author_reported_genes