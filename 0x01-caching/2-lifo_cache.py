#!/usr/bin/env python3
# Importing the BaseCaching class from the base_caching module
"""
Create a class LIFOCache that inherits from BaseCaching and is a caching system:

    You must use self.cache_data - dictionary from the parent class BaseCaching
    You can overload def __init__(self): but don’t forget to call the parent init: super().__init__()
    def put(self, key, item):
        Must assign to the dictionary self.cache_data the item value for the key key.
        If key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher that BaseCaching.MAX_ITEMS:
            you must discard the last item put in cache (LIFO algorithm)
            you must print DISCARD: with the key discarded and following by a new line
    def get(self, key):
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data, return None.
"""
from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFOCache class that inherits from BaseCaching
    Implements a caching system with LIFO (Last-In-First-Out) strategy"""

    def __init__(self):
        """ Initialize the class """
        super().__init__()  # Call the parent class's init method
        self.stack = []  # To keep track of the insertion order

    def put(self, key, item):
        """
        Add an item in the cache
        If key or item is None, do nothing"""
        if key is None or item is None:
            return
        
        if key in self.cache_data:
            self.stack.remove(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.stack.pop(-2)  # The last one before the current
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")
        
        def get(self, key):
            """
            Get an item by key
            If item is None or key is none return none"""
            return self.cache_data.get(key, None)
