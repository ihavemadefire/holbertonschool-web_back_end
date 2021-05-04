#!/usr/bin/env python3
""" This module Lists whatever """


def list_all(mongo_collection):
    """ Get a real database you idiot. SQL is the way the way! """
    count_functions = mongo_collection.count()
    if count_functions == 0:
        return []
    all_documents = mongo_collection.find()
    return all_documents
