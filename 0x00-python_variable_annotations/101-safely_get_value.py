#!/usr/bin/env python3
"""Module for the safely_get_value function"""
from typing import Union, Any, TypeVar, Mapping

T = TypeVar("T")


def safely_get_value(
        dct: Mapping,
        key: Any,
        default: Union[T, None] = None
        ) -> Union[Any, T]:
    """Return a value from a dict if a key exist otherwise a default value"""
    if key in dct:
        return dct[key]
    else:
        return default
