#!/usr/bin/env python3
"""LFUCache class
"""


from collections import OrderedDict, deque
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """ This class inherits from BaseCaching classs
        and it caching system
    """

    def __init__(self):
        """Initialize the class
        """
        super().__init__()
        self.cache_data = OrderedDict()
        self.access_order = deque()
        self.access_count = {}

    def put(self, key, item):
        """ Add new item to the cache
        """

        if not (key and item):
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.access_order.remove(key)
            self.access_count[key] += 1
        self.cache_data[key] = item
        self.access_order.append(key)
        self.access_count[key] = 1

        if len(self.cache_data) > self.MAX_ITEMS:
            # Find the item with the lowest access count
            min_count = min(self.access_count.values())
            items_with_min_count = [
                                    k for k, v in self.access_count.items()
                                    if v == min_count
                                  ]
            # If there is only one item with the lowest count,
            # remove it from the cache
            if len(items_with_min_count) == 1:
                del self.cache_data[items_with_min_count[0]]
                del self.access_count[items_with_min_count[0]]
                self.access_order.remove(items_with_min_count[0])
            else:
                # If there are multiple items with the same lowest count,
                # remove the least recently used item
                lru_key = None
                for key in self.access_order:
                    if key in items_with_min_count:
                        lru_key = key
                        break
                if lru_key:
                    del self.cache_data[lru_key]
                    del self.access_count[lru_key]
                    self.access_order.remove(lru_key)
                    print("DISCARD: {}".format(lru_key))

    def get(self, key):
        """ Return the value of the key in self.cache_data
        """
        if key in self.cache_data:
            self.access_order.remove(key)
            self.access_order.append(key)
            self.access_count[key] += 1
            return self.cache_data[key]

        else:
            return None
