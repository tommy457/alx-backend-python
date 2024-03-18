#!/usr/bin/env python3
"""
Module for the wait_random function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Waits a random time between 0 and max_delay, and returns the awaited time
    """
    seconds_to_wait: float = random.uniform(0, max_delay)
    await asyncio.sleep(seconds_to_wait)
    return seconds_to_wait
