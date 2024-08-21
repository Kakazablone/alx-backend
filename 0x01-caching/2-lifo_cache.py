#!/usr/bin/env python3
""" Function that implements a FIFO caching
system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache is a caching system that inherits from BaseCaching.

    This class implements a LIFO (Last In, First Out) caching system.
    When the cache exceeds its maximum capacity, the most recently added item
    is discarded.
    """

    def __init__(self):
        """Initialize the LIFOCache."""
        super().__init__()
        self.last_key = None  # Track the last key added for LIFO

    def put(self, key, item):
        """Add an item to the cache using the LIFO strategy.

        If the cache exceeds its maximum size, the most recently added item
        is removed.

        Args:
            key: The key associated with the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")

            self.cache_data[key] = item
            self.last_key = key  # Update the last key to the current one

    def get(self, key):
        """Retrieve an item from the cache by its key.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The item associated with the key, or None if the key doesn't exist.
        """
        return self.cache_data.get(key)
