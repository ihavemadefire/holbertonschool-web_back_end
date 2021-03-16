#!/usr/bin/env python3
'''Asynch function concurence'''
from typing import List
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Asynch function concurence'''
    # this feels gross and unpythonic but gather() just won't work
    list_of_times = [wait_random(max_delay) for i in range(n)]
    return [await i for i in asyncio.as_completed(list_of_times)]
