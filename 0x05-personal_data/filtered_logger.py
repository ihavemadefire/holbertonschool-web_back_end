#!/usr/bin/env python3
'''This is the module that constains the filter datum function'''
from typing import List
import re


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    '''Returns a log message obfuscated'''
    for field in fields:
        regex = field + f'[^{separator}]*'
        message = re.sub(regex, f"{field}={redaction}", message)
    return message
