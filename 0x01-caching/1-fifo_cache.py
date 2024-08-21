#!/usr/bin/env python3
""" Function that implements a FIFO caching
system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache is a caching system that inherits from BaseCaching.

    This class implements a FIFO (First In, First Out) caching system.
    When the cache exceeds its maximum capacity, the oldest item (the
    first one put in) is discarded.
    """

    def __init__(self):
        """Initialize the FIFOCache."""
        super().__init__()
        self.order = []  # List to maintain the order of keys for FIFO

    def put(self, key, item):
        """Add an item to the cache using the FIFO strategy.

        If the cache exceeds its maximum size, the first item added
        is removed.

        Args:
            key: The key associated with the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            if key not in self.cache_data:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    first_key = self.order.pop(0)
                    # Get and remove the first key
                    del self.cache_data[first_key]
                    # Remove it from the cache
                    print(f"DISCARD: {first_key}")

            self.cache_data[key] = item
            self.order.append(key)  # Add the key to the end of the list

    def get(self, key):
        """Retrieve an item from the cache by its key.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The item associated with the key, or None if the key doesn't exist.
        """
        return self.cache_data.get(key)
