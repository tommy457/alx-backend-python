#!/usr/bin/env python3
"""Module for the sum_mixed_list function"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of all the mxd_lst elements"""
    return sum(mxd_lst)
