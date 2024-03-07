"""
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
"""
from typing import Union

from pandasgwas.Association import Association
from pandasgwas.Variant import Variant
from pandasgwas.Study import Study
from pandasgwas.Trait import Trait


def bind(a: Union[Association, Variant, Study, Trait],
         b: Union[Association, Variant, Study, Trait]) -> Union[
    Association, Variant, Study, Trait]:
    """
    Binds together GWAS Catalog objects of the same class. Note that bind() preserves duplicates whereas union() does not.

    Args:
        a: An object of the pandasGWAS custom class.
        b: An object of the same type as a.

    Returns:
        An object of the same type as a.

    """
    return a + b


def intersect(a: Union[Association, Variant, Study, Trait],
              b: Union[Association, Variant, Study, Trait]) -> Union[
    Association, Variant, Study, Trait]:
    """
    Returns the data common to both A and B, with no repetitions

    Args:
        a: An object of the pandasGWAS custom class.
        b: An object of the same type as a.

    Returns:
        An object of the same type as a.

    """
    return a & b


def set_diff(a: Union[Association, Variant, Study, Trait],
             b: Union[Association, Variant, Study, Trait]) -> Union[
    Association, Variant, Study, Trait]:
    """
    Returns the data in A that is not in B, with no repetitions

    Args:
        a: An object of the pandasGWAS custom class.
        b: An object of the same type as a.

    Returns:
        An object of the same type as a.

    """
    return a - b


def set_xor(a: Union[Association, Variant, Study, Trait],
            b: Union[Association, Variant, Study, Trait]) -> Union[
    Association, Variant, Study, Trait]:
    """
    Returns the data of A and B that are not in their intersection (the symmetric difference), with no repetitions

    Args:
        a: An object of the pandasGWAS custom class.
        b: An object of the same type as a.

    Returns:
        An object of the same type as a.

    """
    return a ^ b


def union(a: Union[Association, Variant, Study, Trait],
          b: Union[Association, Variant, Study, Trait]) -> Union[
    Association, Variant, Study, Trait]:
    """
    Returns the combined data from A and B with no repetitions

    Args:
        a: An object of the pandasGWAS custom class.
        b: An object of the same type as a.

    Returns:
        An object of the same type as a.

    """
    return a | b


def set_equal(a: Union[Association, Variant, Study, Trait],
              b: Union[Association, Variant, Study, Trait]) -> bool:
    """
    Check if the raw data of a and b are equal

    Args:
        a: An object of the pandasGWAS custom class.
        b: An object of the same type as a.

    Returns:
        True or False.

    """
    return a == b