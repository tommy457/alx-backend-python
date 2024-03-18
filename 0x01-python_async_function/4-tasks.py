#!/usr/bin/env python3
"""
Module for the task_wait_n function
"""
import asyncio
from asyncio import Task
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    return the list of all the delays
    """
    tasks: List[Task] = []
    delays: List[float] = []

    for _ in range(n):
        task: Task = task_wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay: float = await task
        delays.append(delay)

    return delays
