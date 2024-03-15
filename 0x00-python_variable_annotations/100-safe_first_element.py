#!/usr/bin/env python3
"""Module for the safe_first_element function"""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element of the input,
    or None if input is empty or None
    """
    if lst:
        return lst[0]
    else:
        return None
