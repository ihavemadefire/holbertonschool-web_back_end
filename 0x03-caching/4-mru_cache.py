#!/usr/bin/python3
'''This module contains a basic caching class'''
from collections import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    '''This inherits from basecaching'''
    def __init__(self):
        '''Init function with inheritence'''
        super().__init__()
        self.cache_data = OrderedDict()
        self.last_visited = ""

    def put(self, key, item):
        '''Basic put function'''
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if key in self.cache_data:
                    self.cache_data.update({key: item})
                    self.last_visited = key
                else:
                    the_key = self.last_visited
                    del self.cache_data[the_key]
                    print("DISCARD: {}".format(the_key))
                    self.cache_data[key] = item
                    self.last_visited = key
            else:
                self.cache_data[key] = item
                self.last_visited = key

    def get(self, key):
        '''Basic get function'''
        if key is not None and self.cache_data.get(key) is not None:
            self.last_visited = key
            return self.cache_data.get(key)
