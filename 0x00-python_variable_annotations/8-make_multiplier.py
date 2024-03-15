#!/usr/bin/env python3
"""Module for the make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""
    def callable_multiplier(new_multiplier: float) -> float:
        return new_multiplier * multiplier

    return callable_multiplier
