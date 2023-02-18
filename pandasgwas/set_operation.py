from typing import Union

from pandasgwas.Association import Association
from pandasgwas.Variant import Variant
from pandasgwas.Study import Study
from pandasgwas.Trait import Trait


def bind(a: Union[Association, Variant, Study, Trait],
         b: Union[Association, Variant, Study, Trait]) -> Union[
    Association, Variant, Study, Trait]:
    return a + b


def intersect(a: Union[Association, Variant, Study, Trait],
              b: Union[Association, Variant, Study, Trait]) -> Union[
    Association, Variant, Study, Trait]:
    return a & b


def set_diff(a: Union[Association, Variant, Study, Trait],
             b: Union[Association, Variant, Study, Trait]) -> Union[
    Association, Variant, Study, Trait]:
    return a - b


def set_xor(a: Union[Association, Variant, Study, Trait],
            b: Union[Association, Variant, Study, Trait]) -> Union[
    Association, Variant, Study, Trait]:
    return a ^ b


def union(a: Union[Association, Variant, Study, Trait],
          b: Union[Association, Variant, Study, Trait]) -> Union[
    Association, Variant, Study, Trait]:
    return a | b


def set_equal(a: Union[Association, Variant, Study, Trait],
              b: Union[Association, Variant, Study, Trait]) -> bool:
    return a == b