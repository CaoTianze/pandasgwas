from typing import Union

from pandasgwas.Association import Association
from pandasgwas.SingleNucleotidePolymorphism import SingleNucleotidePolymorphism
from pandasgwas.Study import Study
from pandasgwas.Trait import Trait


def bind(a: Union[Association, SingleNucleotidePolymorphism, Study, Trait],
         b: Union[Association, SingleNucleotidePolymorphism, Study, Trait]) -> Union[
    Association, SingleNucleotidePolymorphism, Study, Trait]:
    return a + b


def intersect(a: Union[Association, SingleNucleotidePolymorphism, Study, Trait],
              b: Union[Association, SingleNucleotidePolymorphism, Study, Trait]) -> Union[
    Association, SingleNucleotidePolymorphism, Study, Trait]:
    return a & b


def set_diff(a: Union[Association, SingleNucleotidePolymorphism, Study, Trait],
             b: Union[Association, SingleNucleotidePolymorphism, Study, Trait]) -> Union[
    Association, SingleNucleotidePolymorphism, Study, Trait]:
    return a - b


def set_xor(a: Union[Association, SingleNucleotidePolymorphism, Study, Trait],
            b: Union[Association, SingleNucleotidePolymorphism, Study, Trait]) -> Union[
    Association, SingleNucleotidePolymorphism, Study, Trait]:
    return a ^ b


def union(a: Union[Association, SingleNucleotidePolymorphism, Study, Trait],
            b: Union[Association, SingleNucleotidePolymorphism, Study, Trait]) -> Union[
    Association, SingleNucleotidePolymorphism, Study, Trait]:
    return a | b


def set_equal(a: Union[Association, SingleNucleotidePolymorphism, Study, Trait],
            b: Union[Association, SingleNucleotidePolymorphism, Study, Trait]) -> bool:
    return a == b