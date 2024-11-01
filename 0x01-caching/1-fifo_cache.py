#!/usr/bin/python3
""" FIFOCache module
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ FIFOCache defines a FIFO caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.order = []  # To keep track of the order of keys

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            # If key already exists, update the value and maintain order
            if key in self.cache_data:
                self.cache_data[key] = item
                return

            # Add new item and update order
            self.cache_data[key] = item
            self.order.append(key)

            # If over capacity, remove the first added item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.order.pop(0)
                del self.cache_data[first_key]
                print("DISCARD:", first_key)

    def get(self, key):
        """ Get an item by key """
        return self.cache_data.get(key, None)
