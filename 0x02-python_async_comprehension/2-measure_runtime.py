#!/usr/bin/env python3
'''Basic Async measure '''
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    '''Basic Async measure '''
    t1 = time.time()

    await asyncio.gather(async_comprehension(), async_comprehension(),
                    async_comprehension(), async_comprehension())

    t2 = time.time()

    return t2 - t1
