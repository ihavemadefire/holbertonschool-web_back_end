#!/usr/bin/env python3
'''Asynch function basics'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''Asynch function basics'''
    delay = random.uniform(0.0, max_delay)
    await asyncio.sleep(delay)
    return float(delay)
