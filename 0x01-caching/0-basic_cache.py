#!/usr/bin/env python3

# Importing the BaseCaching class from the base_caching module
from base_caching import BaseCaching

class BasicCache(BaseCaching):
    """ BasicCache class that inherits from BaseCaching
        This caching system has no limit
    """

    def put(self, key, item):
        """ Add an item in the cache
            If key or item is None, do nothing
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
            If key is None or doesn't exist, return None
        """
        return self.cache_data.get(key, None)
