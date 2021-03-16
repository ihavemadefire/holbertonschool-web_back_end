#!/usr/bin/env python3
'''Asynch function timing'''
import time
from asyncio import run


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Asynch function timing'''
    t1 = time.time()
    run(wait_n(n, max_delay))
    t2 = time.time()
    return ((t2 - t1) / n)
