#!/usr/bin/env python3
"""
Module for the wait_n function
"""
import asyncio
from asyncio import Task
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays
    """
    tasks: List[Task] = []
    delays: List[float] = []

    for _ in range(n):
        task: Task = asyncio.create_task(wait_random(max_delay))
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay: float = await task
        delays.append(delay)

    return delays
