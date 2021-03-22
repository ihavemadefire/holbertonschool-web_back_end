#!/usr/bin/python3
'''This module contains a basic caching class'''
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    '''This inherits from basecaching'''
    def __init__(self):
        '''Init function with inheritence'''
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        '''Basic put function'''
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                popped = self.cache_data.popitem(last=False)
                print('DISCARD: {}'.format(popped[0]))

    def get(self, key):
        '''Basic get function'''
        if key is not None and self.cache_data.get(key) is not None:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
