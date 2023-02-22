#!/usr/bin/env python3
"""LIFOCache class
"""


from base_caching import BaseCaching
from collections import OrderedDict


class LIFOCache(BaseCaching):
    """ This class inherits from BaseCaching
        it is a caching class
    """

    def __init__(self):
        """Initialize
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add new item into cache
        """

        if not(key and item):
            return
        
        
        if len(self.cache_data) + 1 > self.MAX_ITEMS:
            k = self.cache_data.popitem()[0]
            print("DISCARD: {}".format(k))
        
        self.cache_data[key] = item
    def get(self, key):
        """Return the value in self.cache_data linked to key
        """

        if not key:
            return None
        return self.cache_data.get(key)
