#!/usr/bin/env python3
'''Asynch function create task'''
import asyncio


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int):
    '''Asynch function create task'''
    return asyncio.create_task(wait_random(max_delay))
