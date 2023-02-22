#!/usr/bin/env python3
"""LRUCache class
"""


from collections import OrderedDict, deque
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ This class inherits from BaseCaching classs
        and it caching system
    """

    def __init__(self):
        """Initialize the class
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.access_order = deque()

    def put(self, key, item):
        """Add an item in the cache
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            self.cache_data[key] = item

        self.cache_data[key] = item
        self.access_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            recent = self.access_order[-2]
            print("DISCARD: {}".format(recent))
            del self.cache_data[recent]
            self.access_order.remove(recent)

    def get(self, key):
        """Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        self.access_order.remove(key)
        self.access_order.append(key)
        return self.cache_data[key]
