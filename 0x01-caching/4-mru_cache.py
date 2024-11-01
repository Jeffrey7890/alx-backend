#!/usr/bin/python3
""" MRUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class MRUCache(BaseCaching):
    """ MRUCache defines an MRU caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_data = OrderedDict()  # To maintain MRU order

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            if key in self.cache_data:
                del self.cache_data[key]

            # Add the item to cache and mark it as most recently used
            self.cache_data[key] = item

            # If over capacity, remove the most recently used item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                most_recent_key, _ = self.cache_data.popitem(last=True)
                print("DISCARD:", most_recent_key)

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Move accessed key to the end to mark it as most recently used
        item = self.cache_data.pop(key)
        self.cache_data[key] = item
        return item
