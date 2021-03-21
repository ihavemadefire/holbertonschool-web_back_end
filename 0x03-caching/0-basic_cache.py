#!/usr/bin/python3
'''This module contains a basic caching class'''
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    '''This inherits from basecaching'''
    def __init__(self):
        '''Init function with inheritence'''
        super().__init__()

    def put(self, key, item):
        '''Basic put function'''
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        '''Basic get function'''
        if key is None or self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data.get(key)
