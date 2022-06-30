# set_operation
Set operations for objects of same class
```Python
# set operation in EFO Trait
from pandasgwas.get_traits import get_traits
from pandasgwas.set_operation import *
traits1 = get_traits(study_id='GCST000854', efo_id='EFO_0001065')
traits2 = get_traits(study_id='GCST000854', efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133')
#Equivalent to traits3 = traits1 + traits2
traits3 = bind(traits1, traits2)
traits1 = get_traits(study_id='GCST000854', efo_id='EFO_0001065')
traits2 = get_traits(study_id='GCST000854', efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133')
#Equivalent to traits3 = traits1 & traits2
traits3 = intersect(traits1, traits2)
traits1 = get_traits(study_id='GCST000854', efo_id='EFO_0001065')
traits2 = get_traits(study_id='GCST000854', efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133')
#Equivalent to traits3 = traits1 - traits2
traits3 = set_diff(traits1, traits2)
traits1 = get_traits(study_id='GCST000854', efo_id='EFO_0001065')
traits2 = get_traits(study_id='GCST000854', efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133')
#Equivalent to traits3 = traits1 ^ traits2
traits3 = set_xor(traits1, traits2)
traits1 = get_traits(study_id='GCST000854', efo_id='EFO_0001065')
traits2 = get_traits(study_id='GCST000854', efo_uri='http://www.ebi.ac.uk/efo/EFO_0005133')
#Equivalent to traits3 = traits1 | traits2
traits3 = union(traits1, traits2)
traits1 = get_traits(study_id='GCST000854')
traits2 = get_traits(study_id='GCST000854')
#Equivalent to traits1 == traits2
set_equal(traits1, traits2)
```
## *function* bind(a,b)->c
Binds together GWAS Catalog objects of the same class. Note that bind() preserves duplicates whereas union() does not.
## *function* intersect(a,b)->c
Returns the data common to both A and B, with no repetitions
## *function* set_diff(a,b)->c
returns the data in A that is not in B, with no repetitions
## *function* set_xor(a,b)->c
returns the data of A and B that are not in their intersection (the symmetric difference), with no repetitions
## *function* union(a,b)->c
returns the combined data from A and B with no repetitions
## *function* set_equal(a,b)->bool
Check if the raw data of a and b are equal
