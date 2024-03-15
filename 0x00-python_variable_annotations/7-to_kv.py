#!/usr/bin/env python3
"""Module for the to_kv function"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return the tuple of first input and the square of the second input"""
    return (k, v*v)
