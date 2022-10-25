# SingleNucleotidePolymorphism
## *class* SingleNucleotidePolymorphism.SingleNucleotidePolymorphism()

Python class to represent a set of GWAS Catalog Single Nucleotide Polymorphism. For more information, see "[GWAS CATALOG API Guide](https://www.ebi.ac.uk/gwas/rest/docs/api)"

```Python
# get Single Nucleotide Polymorphism by study_id
from pandasgwas.get_SNPs import get_variants

snps = get_variants(study_id='GCST000854')
```
### *property* single_nucleotide_polymorphisms
type: pandas.DataFrame  
A DataFrame to represent all queried Single Nucleotide Polymorphisms from GWAS Catalog REST API

### *property* locations
type: pandas.DataFrame  
A DataFrame to represent column locations from single_nucleotide_polymorphisms

### *property* genomic_contexts
type: pandas.DataFrame  
A DataFrame to represent column genomicContexts from single_nucleotide_polymorphisms

### *property* ensembl_gene_ids
type: pandas.DataFrame  
A DataFrame to represent column gene.ensemblGeneIds from genomic_contexts

### *property* entrez_gene_ids
type: pandas.DataFrame  
A DataFrame to represent column gene.entrezGeneIds from genomic_contexts