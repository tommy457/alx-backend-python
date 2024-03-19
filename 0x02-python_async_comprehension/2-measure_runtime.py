#!/usr/bin/env python3
"""
Module for the measure_runtime function.
"""
import asyncio
from asyncio import Task
from typing import List
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """coroutine that will execute async_comprehension four times in parallel,
    and return total runtime.
    """
    tasks: List[Task] = [async_comprehension() for _ in range(4)]
    start: float = time.time()
    await asyncio.gather(*tasks)
    return time.time() - start
