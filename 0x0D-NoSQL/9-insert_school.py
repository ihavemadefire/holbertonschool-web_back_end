  
#!/usr/bin/env python3
""" This module does some stuff. I doesn't like to talk about it"""


def insert_school(mongo_collection, **kwargs):
    """ I start my new dev job tomorrow. God Save me from it. """
    new = {}
    for k, v in kwargs.items():
        new[k] = v
    add = mongo_collection.insert_one(new)
    return add.inserted_id
