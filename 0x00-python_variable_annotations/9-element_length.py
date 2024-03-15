#!/usr/bin/env python3
"""Module for the element_length function"""
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples of two values,
    first value is iterable and second value is int"""
    return [(i, len(i)) for i in lst]
