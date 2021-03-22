#!/usr/bin/python3
'''This module contains a basic caching class'''
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    '''This inherits from basecaching'''
    def __init__(self):
        '''Init function with inheritence'''
        super().__init__()
        self.last_in = ""

    def put(self, key, item):
        '''Basic put function'''
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # updating value
                if key in self.cache_data:
                    self.cache_data.update({key: item})
                    self.last_in = key
                else:
                    the_key = self.last_in
                    del self.cache_data[the_key]
                    print("DISCARD: {}".format(the_key))
                    self.cache_data[key] = item
                    self.last_in = key
            else:
                self.cache_data[key] = item
                self.last_in = key

    def get(self, key):
        '''Basic get function'''
        if key is not None and self.cache_data.get(key) is not None:
            return self.cache_data.get(key)
