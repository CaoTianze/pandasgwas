# get_variants

Get Single Nucleotide Polymorphism function based on different search criteria

## *function* get_variants_by_study_id(study_id: str, interactive: bool = True) -> Variant
Get GWAS Catalog Single Nucleotide Polymorphisms by Study identifier

```Python
from pandasgwas.get_variants import get_variants_by_study_id

snps = get_variants_by_study_id('GCST000854')
```
### param study_id
Study identifier, accessionId in Study
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_variants_by_association_id(association_id: str, interactive: bool = True) -> Variant
Get GWAS Catalog Single Nucleotide Polymorphisms by by their Association identifier

```Python
from pandasgwas.get_variants import get_variants_by_association_id

snps = get_variants_by_association_id('16603')
```
### param association_id
Association identifier, associationId in Association
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_variants_by_variant_id(variant_id: str, interactive: bool = True) -> Variant
Get GWAS Catalog Single Nucleotide Polymorphisms by Single Nucleotide Polymorphism identifier

```Python
from pandasgwas.get_variants import get_variants_by_variant_id

snps = get_variants_by_variant_id('rs7744020')
```
### param variant_id
Single Nucleotide Polymorphism identifier, rsId in Single Nucleotide Polymorphism
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_variants_by_efo_id(efo_id: str, interactive: bool = True) -> Variant
Get GWAS Catalog Single Nucleotide Polymorphisms by their EFO Trait identifier

```Python
from pandasgwas.get_variants import get_variants_by_efo_id

snps = get_variants_by_efo_id('EFO_0001065')
```
### param efo_id
EFO Trait identifier, shortForm in EFO Trait
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_variants_by_pubmed_id(pubmed_id: str, interactive: bool = True) -> Variant
Get GWAS Catalog Single Nucleotide Polymorphisms by PubMed identifiers

```Python
from pandasgwas.get_variants import get_variants_by_pubmed_id

snps = get_variants_by_pubmed_id('21041247')
```
### param pubmed_id
PubMed identifier
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_variants_by_genomic_range(chromosome: str, start: int, end: int, interactive: bool = True) -> Variant
Get GWAS Catalog Single Nucleotide Polymorphisms

```Python
from pandasgwas.get_variants import get_variants_by_genomic_range

snps = get_variants_by_genomic_range('1', 2300001, 5300000)
```
### param chromosome
Human chromosome names: autosomal and sexual chromosomes only, i.e., 1--22, X and Y
### param start
Start position of range (starts at 1).
### param end
End position of range (inclusive).
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_variants_by_cytogenetic_band(cytogenetic_band: str, interactive: bool = True) -> Variant
Get GWAS Catalog Single Nucleotide Polymorphisms

```Python
from pandasgwas.get_variants import get_variants_by_cytogenetic_band

snps = get_variants_by_cytogenetic_band('1p36.32')
```
### param cytogenetic_band
Cytogenetic bands of the form '1p36.11'
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_variants_by_gene_name(gene_name: str, interactive: bool = True) -> Variant
Get GWAS Catalog Single Nucleotide Polymorphisms

```Python
from pandasgwas.get_variants import get_variants_by_gene_name

snps = get_variants_by_gene_name('KIAA0319')
```
### param gene_name
Gene names
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_variants_by_efo_trait(efo_trait: str, interactive: bool = True) -> Variant
Get GWAS Catalog Single Nucleotide Polymorphisms that match trait description

```Python
from pandasgwas.get_variants import get_variants_by_efo_trait

snps = get_variants_by_efo_trait('MHPG measurement')
```
### param efo_trait
Trait description
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_variants_by_reported_trait(reported_trait: str, interactive: bool = True) -> Variant
Get GWAS Catalog Single Nucleotide Polymorphisms that match the reported traits, as reported by the original authors of the study.

```Python
from pandasgwas.get_variants import get_variants_by_reported_trait

snps = get_variants_by_reported_trait("Dupuytren's disease")
```
### param reported_trait
Trait are reported by the original authors of the study
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_variants_all(interactive: bool = True) -> Variant
Get all Single Nucleotide Polymorphisms

```Python
from pandasgwas.get_variants import get_variants_all

snps = get_variants_all()
```
### param interactive
Indicates whether to run in interactive mode, when the value is True and the query data is divided into many pages, the function will prompt whether to continue the download.
## *function* get_variants(study_id: str = None, association_id: str = None, variant_id: str = None, efo_id: str = None, pubmed_id: str = None, genomic_range: List[int] = None, gene_name: str = None, efo_trait: str = None, reported_trait: str = None, set_operation: str = 'bind', interactive: bool = True) -> Variant
Retrieves Single Nucleotide Polymorphisms via the NHGRI-EBI GWAS Catalog REST API. The REST API is queried multiple times with the criteria passed as arguments. By default all Single Nucleotide Polymorphisms that match the criteria supplied in the arguments are retrieved: this corresponds to the default set_operation set to 'bind', If you rather have only the Single Nucleotide Polymorphisms that match simultaneously all criteria provided, then set set_operation to 'intersection'.
