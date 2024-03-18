#!/usr/bin/env python3
"""
Module for the measure_time function.
"""
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    return the total execution time for wait_n divided by n.
    """
    start_time: float = time.time()
    asyncio.run(wait_n(n, max_delay))

    return (time.time() - start_time) / n
