# pandasGWAS: a Python package for easy retrieval of GWAS Catalog data
## Dependencies
python: 3.8  
pandas: 1.4.3  
requests: 2.28.1  
progressbar2: 4.0.0
## Documentation
See [pandasGWAS Documentation](https://caotianze.github.io/pandasgwas/)
## Licensing Information
### Source Code
MIT License
### Data from NHGRI-EBI GWAS Catalog
The NHGRI-EBI GWAS Catalog and all its contents are available under the general [Terms of Use for EMBL-EBI Services](https://www.ebi.ac.uk/about/terms-of-use). Summary statistics are made available under [CC0](https://creativecommons.org/publicdomain/zero/1.0/) unless [otherwise stated](https://www.ebi.ac.uk/gwas/docs/faq#faq-H7).
## Development Environment
OS: Windows10 Professional  
IDE: PyCharm 2022.1 (Community Edition)
## Installation
`pip install pandasgwas`
## Example
Get studies related to triple-negative breast cancer:
```Python
from pandasgwas import get_studies
studies = get_studies(efo_trait = 'triple-negative breast cancer')
studies.studies[0:4]
#                  initialSampleSize                    gxe    gxg   snpCount  qualifier  imputed  pooled studyDesignComment  accessionId   fullPvalueSet  userRequested            platforms                                ancestries                                   genotypingTechnologies                             replicationSampleSize                                diseaseTrait.trait                 publicationInfo.pubmedId publicationInfo.publicationDate publicationInfo.publication               publicationInfo.title                publicationInfo.author.fullname publicationInfo.author.orcid
#0  1,529 European ancestry cases, 3,399 European ...  False  False        NaN    None     True     False        None           GCST002305      False          False      [{'manufacturer': 'Illumina'}]  [{'type': 'replication', 'numberOfIndividuals'...  [{'genotypingTechnology': 'Genome-wide genotyp...  2,148 European ancestry cases, 1,309 European ...  Breast cancer (estrogen-receptor negative, pro...         24325915                    2013-12-09                    Carcinogenesis      Genome-wide association study identifies 25 kn...           Purrington KS              0000-0002-5710-1692    
#1  8,602 European ancestry triple negative cases,...  False  False  9.700e+06       ~     True     False        None           GCST010100      False           True      [{'manufacturer': 'Illumina'}]  [{'type': 'initial', 'numberOfIndividuals': 11...  [{'genotypingTechnology': 'Genome-wide genotyp...                                                 NA  Breast cancer (estrogen-receptor negative, pro...         32424353                    2020-05-18                         Nat Genet      Genome-wide association study identifies 32 no...                 Zhang H                             None    
#2                5,631 European ancestry individuals  False  False  1.000e+07    None     True     False        None         GCST90029052      False          False                                  []  [{'type': 'initial', 'numberOfIndividuals': 56...  [{'genotypingTechnology': 'Genome-wide genotyp...                                                 NA  15-year breast cancer-specific survival (ER ne...         34407845                    2021-08-18                 Breast Cancer Res      Association of germline genetic variants with ...                 Morra A                             None
```
Find associated variants with study GCST002305:

```Python
from pandasgwas import get_variants
variants = get_variants(study_id='GCST002305')
variants.variants[['rsId', 'functionalClass']]
#      rsId      functionalClass   
# 0   rs4245739  3_prime_UTR_variant
# 1   rs2363956     missense_variant
# 2  rs10069690       intron_variant
# 3   rs3757318       intron_variant
# 4  rs10771399   intergenic_variant
```
Aggregate queried results using mathematical symbols
```Python
from pandasgwas.get_studies import get_studies
study1=get_studies(reported_trait='Suicide risk')
study2=get_studies(reported_trait="Dupuytren's disease")
study3=get_studies(reported_trait="Triglycerides")
study4=get_studies(reported_trait="Retinal vascular caliber")
study5=get_studies(reported_trait="Non-small cell lung cancer (survival)")
all_studies=study1+study2+study3+study4+study5
```
## Similar projects
R package [gwasrapidd](https://github.com/ramiromagno/gwasrapidd) by Ramiro Magno