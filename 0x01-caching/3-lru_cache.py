#!/usr/bin/env python3
"""LRUCache class
"""


from collections import OrderedDict, deque
from base_caching import BaseCaching


class LRUCache(BaseCaching):
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
        """ Add new item to the cache
        """

        if not (key and item):
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.access_order.remove(key)

        else:
            self.cache_data[key] = item

        self.access_order.append(key)

        if len(self.cache_data) > self.MAX_ITEMS:
            k = self.access_order.popleft()
            del self.cache_data[k]
            print("DISCARD: {}".format(k))

    def get(self, key):
        if key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]

        else:
            return None
