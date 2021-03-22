#!/usr/bin/python3
'''This module contains a basic caching class'''
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    '''This inherits from basecaching'''
    def __init__(self):
        '''Init function with inheritence'''
        super().__init__()

    def put(self, key, item):
        '''Basic put function'''
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # removes first itme
                the_key = [i for i in self.cache_data.keys()][0]
                pop = self.cache_data.pop(the_key, None)
                print("DISCARD: {}".format(the_key))
                # assignes new item value
                self.cache_data[key] = item
            else:
                self.cache_data[key] = item

    def get(self, key):
        '''Basic get function'''
        if key is not None and self.cache_data.get(key) is not None:
            return self.cache_data.get(key)
