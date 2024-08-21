#!/usr/bin/env python3
""" Function that implements the Least
Recently used caching system
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRUCache is a caching system that inherits from BaseCaching.

    This class implements an LRU (Least Recently Used) caching system.
    When the cache exceeds its maximum capacity, the least recently used
    item is discarded.
    """

    def __init__(self):
        """Initialize the LRUCache."""
        super().__init__()
        self.access_order = []
        # List to maintain the access order of keys for LRU

    def put(self, key, item):
        """Add an item to the cache using the LRU strategy.

        If the cache exceeds its maximum size, the least recently used item
        is removed.

        Args:
            key: The key associated with the item.
            item: The item to be cached.
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                # Update the position of the key in the access order
                self.access_order.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Discard the least recently used item
                lru_key = self.access_order.pop(0)
                del self.cache_data[lru_key]
                print(f"DISCARD: {lru_key}")

            # Add the new key-value pair to the cache
            #  and update the access order
            self.cache_data[key] = item
            self.access_order.append(key)

    def get(self, key):
        """Retrieve an item from the cache by its key.

        If the key exists, it will be marked as recently used.

        Args:
            key: The key for the item to retrieve.

        Returns:
            The item associated with the key, or None if the key doesn't exist.
        """
        if key is not None and key in self.cache_data:
            # Update the position of the key in the access order
            self.access_order.remove(key)
            self.access_order.append(key)
            return self.cache_data[key]
        return None
