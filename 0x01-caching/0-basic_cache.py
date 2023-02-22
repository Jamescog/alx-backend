#!/usr/bin/env python
"""BasicCache class
"""


from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ This class inherts from BaseCaching class
        - it is caching system
    """

    def put(self, key, item):
        """Add an item to cache
        """
        if not (key and item):
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Return the value in self.cache_data
            linked to key
        """
        if not key:
            return None
        return self.cache_data.get(key)
