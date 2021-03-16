#!/usr/bin/env python3
'''Asynch function alter wait_n'''
from typing import List
import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Asynch function alter wait_n'''
    # this feels gross and unpythonic but gather() just won't work
    list_of_times = [task_wait_random(max_delay) for i in range(n)]
    return [await i for i in asyncio.as_completed(list_of_times)]
