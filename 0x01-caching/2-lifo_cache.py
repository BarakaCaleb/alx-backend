#!/usr/bin/env python3
# Importing the BaseCaching class from the base_caching module
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """ LIFOCache class that inherits from BaseCaching
        Implements a caching system with LIFO (Last-In-First-Out) strategy
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()  # Call the parent class's init method
        self.stack = []  # To keep track of the insertion order

    def put(self, key, item):
        """ Add an item in the cache
            If key or item is None, do nothing
        """
        if key is None or item is None:
            return

        # If key already exists, remove it from the stack to update its position
        if key in self.cache_data:
            self.stack.remove(key)
        
        # Add the new key to the stack and the cache
        self.cache_data[key] = item
        self.stack.append(key)

        # If the cache exceeds MAX_ITEMS, remove the last item added (LIFO)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop(-2)  # The last one before the current
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """ Get an item by key
            If key is None or doesn't exist, return None
        """
        return self.cache_data.get(key, None)
