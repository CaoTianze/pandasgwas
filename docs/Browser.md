# Browser

A set of helper functions for accessing web links

## *function* open_in_pubmed(pubmed_id: str) -> bool
This function launches the web browser and opens a tab for PubMed citation
```Python
from pandasgwas.Browser import *
open_in_pubmed('26301688')
```
### param pubmed_id
A PubMed identifier
## *function* open_in_dbsnp(variant_id: str) -> bool
This function launches the web browser at dbSNP and opens a tab for SNP identifier
```Python
from pandasgwas.Browser import *
open_in_dbsnp('rs56261590')
```
### param variant_id
A variant(Single Nucleotide Polymorphism) identifier
## *function* open_in_gtex(variant_id: str) -> bool
This function launches the web browser at the GTEx Portal and opens a tab for SNP identifier.
```Python
from pandasgwas.Browser import *
open_in_gtex('rs56261590')
```
### param variant_id
A variant(Single Nucleotide Polymorphism) identifier
## *function* open_study_in_gwas_catalog(study_id: str) -> bool
Browse GWAS Catalog entitie Study from the GWAS Web Graphical User Interface
```Python
from pandasgwas.Browser import *
open_study_in_gwas_catalog('GCST000016')
```
### param study_id
A Study identifier
## *function* open_variant_in_gwas_catalog(variant_id: str) -> bool
Browse GWAS Catalog entitie Single Nucleotide Polymorphism from the GWAS Web Graphical User Interface
```Python
from pandasgwas.Browser import *
open_variant_in_gwas_catalog('rs146992477')
```
### param variant_id
A variant(Single Nucleotide Polymorphism) identifier
## *function* open_trait_in_gwas_catalog(efo_id: str) -> bool
Browse GWAS Catalog entitie Trait from the GWAS Web Graphical User Interface
```Python
from pandasgwas.Browser import *
open_trait_in_gwas_catalog('EFO_0004884')
```
### param efo_id
An EFO Trait identifier
## *function* open_gene_in_gwas_catalog(gene_name: str) -> bool
Browse GWAS Catalog entitie Gene from the GWAS Web Graphical User Interface
```Python
from pandasgwas.Browser import *
open_gene_in_gwas_catalog('DPP6')
```
### param gene_name
Gene name
## *function* open_region_in_gwas_catalog(region_name_or_location: str) -> bool
Browse GWAS Catalog entitie Region from the GWAS Web Graphical User Interface
```Python
from pandasgwas.Browser import *
#region_name
open_region_in_gwas_catalog('2q37.1')
#location
open_region_in_gwas_catalog('chr2:230100001-234700000')
```
### param region_name_or_location
Region name or chromosome and base pair location on the reference genome
## *function* open_publication_in_gwas_catalog(pubmed_id: str) -> bool
Browse GWAS Catalog entitie Publication from the GWAS Web Graphical User Interface
```Python
from pandasgwas.Browser import *
open_publication_in_gwas_catalog('25533513')
```
### param pubmed_id
A PubMed identifier