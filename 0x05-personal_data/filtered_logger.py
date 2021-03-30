#!/usr/bin/env python3
'''This is the module that constains the filter datum function'''
from typing import List
import re
import logging


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    '''Returns a log message obfuscated'''
    for field in fields:
        regex = field + f'[^{separator}]*'
        message = re.sub(regex, f"{field}={redaction}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        '''Init function to create instances'''
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = list(fields)

    def format(self, record: logging.LogRecord) -> str:
        '''Formating function To format what needs formatting'''
        return filter_datum(
            self.fields, self.REDACTION, super().format(record),
            self.SEPARATOR)
