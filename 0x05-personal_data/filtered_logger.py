#!/usr/bin/env python3
'''This is the module that constains the filter datum function'''
from typing import List
import re
import os
import mysql.connector
import logging
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


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


def get_logger() -> logging.Logger:
    '''Gets a log and logs it'''
    logger = logging.getLogger('user_data')
    logger.setLevel(logging.INFO)
    logger.propagate = False
    x = logging.StreamHandler()
    x.setLevel(logging.INFO)
    x.setFormatter(RedactingFormatter)
    logger.addHandler(x)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    '''Establishes connection with database'''
    host = os.environ["PERSONAL_DATA_DB_HOST"]
    user = os.environ["PERSONAL_DATA_DB_USERNAME"]
    passwd = os.environ["PERSONAL_DATA_DB_PASSWORD"]
    db = os.environ["PERSONAL_DATA_DB_NAME"]
    conn = mysql.connector.connect(
            host=host,
            user=user,
            passwd=passwd,
            database=db
    )
    return conn
