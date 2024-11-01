#!/usr/bin/python3
""" LIFOCache module
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFOCache defines a LIFO caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.last_key = None  # To keep track of the last added key

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            # Add the item to the cache
            self.cache_data[key] = item

            # If key is new, update last_key
            if key != self.last_key:
                self.last_key = key

            # If over capacity, remove the last added item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key in self.cache_data:
                    print("DISCARD:", self.last_key)
                    del self.cache_data[self.last_key]
                self.last_key = key

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
