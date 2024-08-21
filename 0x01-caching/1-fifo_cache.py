#!/usr/bin/env python3
# Importing the BaseCaching class from the base_caching module
from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """ FIFOCache class that inherits from BaseCaching
        Implements a caching system with FIFO (First-In-First-Out) strategy
    """

    def __init__(self):
        """ Initialize the class """
        super().__init__()  # Call the parent class's init method
        self.queue = []  # To keep track of the order in which keys are added

    def put(self, key, item):
        """ Add an item in the cache
            If key or item is None, do nothing
        """
        if key is None or item is None:
            return

        # If key already exists, remove it from the queue to update its position
        if key in self.cache_data:
            self.queue.remove(key)
        # Add the new key to the queue and the cache
        self.cache_data[key] = item
        self.queue.append(key)

        # If the cache exceeds MAX_ITEMS, remove the first item added (FIFO)
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            first_key = self.queue.pop(0)  # The first item inserted
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """ Get an item by key
            If key is None or doesn't exist, return None
        """
        return self.cache_data.get(key, None)
