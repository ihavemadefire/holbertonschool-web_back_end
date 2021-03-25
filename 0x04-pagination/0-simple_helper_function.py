#!/usr/bin/env python3
"""
This module creates a helper function
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple:
    '''simple helper function'''
    return ((page - 1) * page_size, page * page_size)
