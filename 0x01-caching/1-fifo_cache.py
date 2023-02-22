#!/usr/bin/env python3
"""FIFOCache class
"""


from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ This class inherits from BaseCaching
        and it is a caching systerm
    """

    def __init__(self):
        """Initialize the class
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Adds new cache
            If the number of number of items in self.cache_data
            is greater than BaseCaching.MAX_ITEMS:
                it will disgard the first item put in cache(FIFO Algorithm)
        """
        if not (key and item):
            return
        self.cache_data[key] = item
        if len(self.cache_data) > self.MAX_ITEMS:
            key = self.cache_data.popitem(last=False)
            print("DISCARD:{}\n".format(key[0]))

    def get(self, key):
        """Return the value in self.cache_data linked to key
        """
        if not key:
            return None
        return self.cache_data.get(key)
