#!/usr/bin/env python3
"""
Module for the async_comprehension function.
"""
from typing import List 

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """coroutine will collect 10 random numbers,
    using an async comprehensing over async_generator and return them.
    """
    return [number async for number in async_generator()]
