#!/usr/bin/python3
""" LFUCache module
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """ LFUCache defines an LFU caching system """

    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_data = {}
        self.frequency = {}
        self.usage_order = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.usage_order.move_to_end(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                min_freq = min(self.frequency.values())
                least_freq_keys = [
                        k for k,
                        freq in self.frequency.items() if freq == min_freq
                ]

                if len(least_freq_keys) > 1:
                    for k in self.usage_order:
                        if k in least_freq_keys:
                            key_to_discard = k
                            break
                else:
                    key_to_discard = least_freq_keys[0]
                del self.cache_data[key_to_discard]
                del self.frequency[key_to_discard]
                del self.usage_order[key_to_discard]
                print("DISCARD:", key_to_discard)
            self.cache_data[key] = item
            self.frequency[key] = 1
            self.usage_order[key] = None

    def get(self, key):
        """ Get an item by key """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency and mark as recently used
        self.frequency[key] += 1
        self.usage_order.move_to_end(key)
        return self.cache_data[key]
